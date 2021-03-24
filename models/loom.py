from enum import Enum, auto
from abc import ABC, abstractmethod

list_of_looms = []

class OriginCountry(Enum):
    UKRAINE = auto()
    GERMANY = auto()
    USA = auto()
    CHINA = auto()


class Loom(ABC):
    @abstractmethod
    def __init__(self, originCountry: OriginCountry, price: float, power_in_watts: float,
                 width_of_the_formed_tissue: int, material_of_the_produced_fabric: str):
        self._originCountry = originCountry
        self._price = price
        self._power_in_watts = power_in_watts
        self._width_of_the_formed_tissue = width_of_the_formed_tissue
        self._material_of_the_produced_fabric = material_of_the_produced_fabric

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def originCountry(self):
        raise NotImplementedError()

    @originCountry.setter
    @abstractmethod
    def originCountry(self, originCountry: OriginCountry):
        raise NotImplementedError()

    @property
    @abstractmethod
    def price(self):
        raise NotImplementedError()

    @price.setter
    @abstractmethod
    def price(self, price: float):
        raise NotImplementedError()

    @property
    @abstractmethod
    def power_in_watts(self):
        raise NotImplementedError()

    @power_in_watts.setter
    @abstractmethod
    def power_in_watts(self, power_in_watts: float):
        raise NotImplementedError()

    @property
    @abstractmethod
    def width_of_the_formed_tissue(self):
        raise NotImplementedError()

    @width_of_the_formed_tissue.setter
    @abstractmethod
    def width_of_the_formed_tissue(self, width_of_the_formed_tissue: int):
        raise NotImplementedError()

    @property
    @abstractmethod
    def material_of_the_produced_fabric(self):
        raise NotImplementedError()

    @material_of_the_produced_fabric.setter
    @abstractmethod
    def material_of_the_produced_fabric(self, material_of_the_produced_fabric: str):
        raise NotImplementedError()
