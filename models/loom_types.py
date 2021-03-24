from .loom import OriginCountry, Loom
from enum import Enum, auto
from abc import ABC, abstractmethod


# HandLoom
class Status(Enum):
    FUNCTIONAL = auto()
    INEFFECTIVE = auto()


class HandLoom(Loom):
    def __init__(self, originCountry: OriginCountry, price: float, power_in_watts: float,
                 width_of_the_formed_tissue: int, material_of_the_produced_fabric: str,
                 manufacture_century: int, status: Status):
        super().__init__(originCountry, price, power_in_watts, width_of_the_formed_tissue,
                         material_of_the_produced_fabric)
        self.__manufacture_century = manufacture_century
        self.status = status

    def __del__(self):
        pass

    def __str__(self):
        return f"HANDLOOM\n" \
               f"Manufacture century: {self.__manufacture_century}\n" \
               f"Status: {self.status}\n" \
               f"Origin country: {self._originCountry}\n" \
               f"Price: {self._price}\n" \
               f"Power in watts: {self._power_in_watts}\n" \
               f"Width of the formed tissue: {self._width_of_the_formed_tissue}\n" \
               f"Material of the produced fabric: {self._material_of_the_produced_fabric}\n"

    @property
    def manufacture_century(self):
        return self.__manufacture_century

    @manufacture_century.setter
    def manufacture_century(self, manufacture_century: int):
        self.__manufacture_century = manufacture_century

    @property
    def originCountry(self):
        return self._originCountry

    @originCountry.setter
    def originCountry(self, originCountry: OriginCountry):
        self._originCountry = originCountry

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price

    @property
    def power_in_watts(self):
        return self._power_in_watts

    @power_in_watts.setter
    def power_in_watts(self, power_in_watts: float):
        self._power_in_watts = power_in_watts

    @property
    def width_of_the_formed_tissue(self):
        return self._width_of_the_formed_tissue

    @width_of_the_formed_tissue.setter
    def width_of_the_formed_tissue(self, width_of_the_formed_tissue: int):
        self._width_of_the_formed_tissue = width_of_the_formed_tissue

    @property
    def material_of_the_produced_fabric(self):
        return self._material_of_the_produced_fabric

    @material_of_the_produced_fabric.setter
    def material_of_the_produced_fabric(self, material_of_the_produced_fabric: str):
        self._material_of_the_produced_fabric = material_of_the_produced_fabric


# MechanicalLoom
class Shape(Enum):
    FLAT = auto()
    CIRCULAR = auto()
    SQUARE = auto()


class MechanicalLoom(Loom, ABC):
    @abstractmethod
    def __init__(self, originCountry: OriginCountry, price: float, power_in_watts: float,
                 width_of_the_formed_tissue: int, material_of_the_produced_fabric: str,
                 construction: Shape):
        super().__init__(originCountry, price, power_in_watts, width_of_the_formed_tissue,
                         material_of_the_produced_fabric)
        self._construction = construction

    @property
    @abstractmethod
    def construction(self):
        raise NotImplementedError()

    @construction.setter
    @abstractmethod
    def construction(self, construction: Shape):
        raise NotImplementedError()
