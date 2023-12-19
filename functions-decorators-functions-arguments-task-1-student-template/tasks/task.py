from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    result_select = selector(data)
    for filter_func in filters:
        result_filter = filter_func(result_select)

        result_select = result_filter

    return result_filter


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def select_columns(data: DataType) -> DataType:
        searched_columns = [
            {column: dct[column] for column in columns}
            for dct in data
        ]
        return searched_columns

    return select_columns


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def filter_columns(data: DataType) -> DataType:
        filtered_columns = [
            dct for dct in data
            if dct.get(column) is not None and dct[column] in values
        ]
        return filtered_columns

    return filter_columns


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]

    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
