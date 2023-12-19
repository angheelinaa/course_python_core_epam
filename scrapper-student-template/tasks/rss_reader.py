# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
from xml.etree import ElementTree
import json
import requests


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        # >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        # >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        # >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    rss_channel_elements = (
        'title', 'link', 'lastBuildDate', 'pubDate', 'language',
        'category', 'managinEditor', 'description'
    )
    rss_item_elements = (
        'title', 'author', 'pubDate', 'link', 'category', 'description'
    )
    output_channel_elements = (
        'Feed', 'Link', 'Last Build Date', 'Publish Date', 'Language',
        'Categories', 'Editor', 'Description'
    )
    output_item_elements = (
        'Title', 'Author', 'Published', 'Link', 'Categories'
    )

    if limit is not None and limit < 0:
        raise UnhandledException("Limit must be >= 0")

    rss_xml_lst = []
    xml_root = ElementTree.fromstring(xml)

    if json:
        rss_xml_lst.extend(
            make_json_output(
                xml_root, limit, rss_channel_elements, rss_item_elements
            )
        )
    else:
        rss_xml_lst.extend(
            make_standard_output(
                xml_root, limit, rss_channel_elements, output_channel_elements,
                rss_item_elements, output_item_elements
            )
        )

    return rss_xml_lst


def stdout_parse_channel(channel, rss_channel_elements, output_channel_elements):
    rss_lst = []
    for i, elem in enumerate(rss_channel_elements):
        if channel.find(elem) is not None:
            if elem == 'category':
                lst_categories = [category.text for category in channel.findall(elem)]
                rss_lst.append(f"{output_channel_elements[i]}: {', '.join(lst_categories)}")
                continue

            rss_lst.append(
                f"{output_channel_elements[i]}: {channel.find(elem).text}"
            )

    rss_lst[-1] += "\n"
    return rss_lst


def stdout_parse_item(item, rss_item_elements, output_item_elements):
    rss_lst = []
    for i, elem in enumerate(rss_item_elements):
        if item.find(elem) is not None:
            if elem == 'category':
                lst_categories = [category.text for category in item.findall(elem)]
                rss_lst.append(f"{output_item_elements[i]}: {', '.join(lst_categories)}")
                continue

            if elem == 'description':
                rss_lst.append(f"\n{item.find(elem).text}\n")
                return rss_lst

            rss_lst.append(
                f"{output_item_elements[i]}: {item.find(elem).text}"
            )

    return rss_lst


def make_standard_output(
    root, limit, rss_channel_elements, output_channel_elements,
    rss_item_elements, output_item_elements
):
    rss_lst = []
    channels = root.findall('channel')
    for channel in channels:
        rss_lst.extend(
            stdout_parse_channel(
                channel, rss_channel_elements, output_channel_elements
            )
        )

        count = 0
        items = channel.findall('item')
        for item in items:
            if limit is not None and count >= limit:
                break

            rss_lst.extend(
                stdout_parse_item(
                    item, rss_item_elements, output_item_elements
                )
            )
            count += 1

    return rss_lst


def json_parse(tag, rss_tag_elements):
    rss_dct = {}
    for elem in rss_tag_elements:
        if tag.find(elem) is not None:
            if elem == 'category':
                lst_categories = [category.text for category in tag.findall(elem)]
                rss_dct[elem] = lst_categories
                continue

            rss_dct[elem] = tag.find(elem).text

    return rss_dct


def make_json_output(root, limit, rss_channel_elements, rss_item_elements):
    rss_lst = []
    channels = root.findall('channel')
    for channel in channels:
        rss_dct = {}
        rss_dct.update(json_parse(channel, rss_channel_elements))

        count = 0
        lst_items = []
        items = channel.findall('item')
        for item in items:
            if limit is not None and count >= limit:
                break

            lst_items.append(json_parse(item, rss_item_elements))
            count += 1

        if lst_items:
            rss_dct['items'] = lst_items
        rss_lst.append(json.dumps(rss_dct, indent=2))

    return rss_lst


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
