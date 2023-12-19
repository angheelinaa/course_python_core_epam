import re


def check_str(s: str):
    only_words = re.sub(r"[\W_]+", '', s.lower())
    first = 0
    last = len(only_words) - 1

    while first < last:
        if only_words[first] == only_words[last]:
            first += 1
            last -= 1
        else:
            return False

    return True
