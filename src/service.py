from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar("T")


class IService(ABC, Generic[T]):
    @abstractmethod
    def create(self) -> T:
        pass

    @abstractmethod
    def get(self) -> T:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def update(self) -> T:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass
