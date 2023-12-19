from typing import List


def sep_none(data, sep, max_split):
    split_lst = []
    word = ""
    count = 0
    for c in data:
        if max_split == -1 or count < max_split:
            if c not in sep:
                word += c
            else:
                if word:
                    count += 1
                    split_lst.append(word)
                word = ""
        else:
            word += c
    if word:
        split_lst.append(word.strip())
    return split_lst


def find_sep(data, sep, max_split):
    split_lst = []
    word = ""
    count = 0
    for c in data:
        if max_split == -1 or count < max_split:
            if c not in sep:
                word += c
            else:
                count += 1
                split_lst.append(word)
                word = ""
        else:
            word += c
    split_lst.append(word.strip(sep))
    return split_lst


def split(data: str, sep=None, maxsplit=-1):
    if not data:
        return []

    if sep is None:
        sep_lst = ('\n', '\r', '\t', '\f', ' ')
        return sep_none(data.strip(), sep_lst, maxsplit)

    return find_sep(data, sep, maxsplit)


if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
