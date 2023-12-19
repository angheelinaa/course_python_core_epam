def replacer(s: str) -> str:
    lst = []
    lst.extend(s)
    print(lst)
    for i in range(len(lst)):
        if lst[i] == "'":
            lst[i] = '"'
        elif lst[i] == '"':
            lst[i] = "'"

    result = "".join(lst)
    return result
