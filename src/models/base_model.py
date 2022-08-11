from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseModel(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs):
        pass

