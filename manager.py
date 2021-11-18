class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def __str__(self):
        return f"name_class: {self._class}"

    def search(self, **kwargs):
        results = list()
        for keys, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, keys) and getattr(obj, keys) == value:
                    results.append(obj)
        return results
