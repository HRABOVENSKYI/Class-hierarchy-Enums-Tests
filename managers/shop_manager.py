from enum import Enum, auto


class SortOrder(Enum):
    ASC = auto()
    DESC = auto()


class ShopManager:
    def __init__(self, looms: list):
        self.__looms = looms

    def __del__(self):
        pass

    def search_by(self, material_of_the_produced_fabric: str, width_of_the_formed_tissue: int):
        result_of_search = []
        for loom in self.__looms:
            if (loom.material_of_the_produced_fabric == material_of_the_produced_fabric and
                    loom.width_of_the_formed_tissue == width_of_the_formed_tissue):
                result_of_search.append(loom)
        return result_of_search

    def sort_by_price(self, sortOrder: SortOrder):
        if sortOrder == SortOrder.ASC:
            return sorted(self.__looms, key=lambda loom: loom.price, reverse=False)
        return sorted(self.__looms, key=lambda loom: loom.price, reverse=True)

    def sort_by_power_in_watts(self, sortOrder: SortOrder):
        if sortOrder == SortOrder.ASC:
            return sorted(self.__looms, key=lambda loom: loom.power_in_watts, reverse=False)
        return sorted(self.__looms, key=lambda loom: loom.power_in_watts, reverse=True)

    def print_all_looms(self):
        for loom in self.__looms:
            print(f"{loom}\n")

    @staticmethod
    def print_looms(looms):
        for loom in looms:
            print(f"{loom}\n")
