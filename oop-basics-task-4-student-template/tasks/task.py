from typing import Dict, Any


class HistoryDict:
    def __init__(self, dct: Dict[Any, Any]) -> None:
        self.dct = dct
        self.lst_keys = []

    def set_value(self, key: Any, value: Any) -> None:
        self.dct[key] = value
        self.lst_keys.append(key)

        if len(self.lst_keys) > 5:
            self.lst_keys.pop(0)

    def get_history(self):
        return self.lst_keys
