class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def __str__(self):
        return f"Manager: {self._class}"

    def search(self, **kwargs):
        results = list()
        for keys, value in kwargs.items():
            if keys.endswith("__min"):
                keys = keys[:-5]
                compare_key = "min"

            elif keys.endswith("__max"):
                keys = keys[:-5]
                compare_key = "max"

            else:
                compare_key = "equal"

            for obj in self._class.object_list:
                if hasattr(obj, keys):
                    if compare_key == "min":
                        result = bool(getattr(obj, keys) >= value)

                    elif compare_key == "max":
                        result = bool(getattr(obj, keys) <= value)

                    else:
                        result = bool(getattr(obj, keys) == value)

                    if result:
                        results.append(obj)
        return results

    def get(self, **kwargs):
        results = list()
        for keys, value in kwargs.items():
            if keys.endswith("__min"):
                keys = keys[:-5]
                compare_key = "min"

            elif keys.endswith("__max"):
                keys = keys[:-5]
                compare_key = "max"

            else:
                compare_key = "equal"

            for obj in self._class.object_list:
                if hasattr(obj, keys):
                    if compare_key == "min":
                        result = bool(getattr(obj, keys) >= value)

                    elif compare_key == "max":
                        result = bool(getattr(obj, keys) <= value)

                    else:
                        result = bool(getattr(obj, keys) == value)

                    if result:
                        results.append(obj)
        return results

    def count(self):
        return len(self._class.object_list)