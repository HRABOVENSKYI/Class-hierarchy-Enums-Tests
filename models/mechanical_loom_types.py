from .loom_types import MechanicalLoom, OriginCountry, Shape


class WrapweightedLoom(MechanicalLoom):
    def __init__(self, originCountry: OriginCountry, price: float, power_in_watts: float,
                 width_of_the_formed_tissue: int, material_of_the_produced_fabric: str,
                 construction: Shape):
        super().__init__(originCountry, price, power_in_watts, width_of_the_formed_tissue,
                         material_of_the_produced_fabric, construction)

    def __del__(self):
        pass

    def __str__(self):
        return f"WRAPWEIGHTEDLOOM\n" \
               f"Origin country: {self._originCountry}\n" \
               f"Price: {self._price}\n" \
               f"Power in watts: {self._power_in_watts}\n" \
               f"Width of the formed tissue: {self._width_of_the_formed_tissue}\n" \
               f"Material of the produced fabric: {self._material_of_the_produced_fabric}\n" \
               f"Construction: {self.construction}"

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

    @property
    def construction(self):
        return self._construction

    @construction.setter
    def construction(self, construction: Shape):
        self._construction = construction


class DrawLoom(WrapweightedLoom):
    def __str__(self):
        return f"DRAWLOOM\n" \
               f"Origin country: {self._originCountry}\n" \
               f"Price: {self._price}\n" \
               f"Power in watts: {self._power_in_watts}\n" \
               f"Width of the formed tissue: {self._width_of_the_formed_tissue}\n" \
               f"Material of the produced fabric: {self._material_of_the_produced_fabric}\n" \
               f"Construction: {self.construction}"


class FlyingLoom(WrapweightedLoom):
    def __str__(self):
        return f"FLYINGLOOM\n" \
               f"Origin country: {self._originCountry}\n" \
               f"Price: {self._price}\n" \
               f"Power in watts: {self._power_in_watts}\n" \
               f"Width of the formed tissue: {self._width_of_the_formed_tissue}\n" \
               f"Material of the produced fabric: {self._material_of_the_produced_fabric}\n" \
               f"Construction: {self.construction}"
