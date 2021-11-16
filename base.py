from abc import ABC, abstractmethod


class BaseClass(ABC):
    id = 0
    object_list = list()

    def __init__(self):
        self._id = self.generate_id()
        self.store(self)

    @classmethod
    def generate_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def store(cls, obj):
        return cls.object_list.append(obj)
