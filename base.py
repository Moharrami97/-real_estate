from abc import ABC


class BaseClass(ABC):
    id = 0
    object_list = None

    def __init__(self):
        self.id = self.generate_id()
        self.store(self)

    @classmethod
    def generate_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def store(cls, obj):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(obj)
