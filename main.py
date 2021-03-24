from managers.shop_manager import ShopManager, SortOrder
from models.loom import OriginCountry
from models.loom_types import HandLoom, Status, Shape
from models.mechanical_loom_types import WrapweightedLoom, FlyingLoom, DrawLoom

if __name__ == "__main__":
    # List of HandLoom, WrapweightedLoom, FlyingLoom, DrawLoom objects
    # From another classes we cannot create objects because they are abstract
    list_of_looms = [HandLoom(OriginCountry.UKRAINE, 18000, 0, 1, "Cotton", 19, Status.FUNCTIONAL),
                     WrapweightedLoom(OriginCountry.CHINA, 4500, 120, 2, "Silk", Shape.FLAT),
                     FlyingLoom(OriginCountry.USA, 12500, 850, 6, "Wool", Shape.CIRCULAR),
                     DrawLoom(OriginCountry.GERMANY, 14999, 1200, 8, "Wool", Shape.SQUARE),
                     FlyingLoom(OriginCountry.USA, 9999, 750, 5, "Silk", Shape.CIRCULAR),
                     WrapweightedLoom(OriginCountry.CHINA, 4699, 165, 6, "Wool", Shape.FLAT),
                     HandLoom(OriginCountry.UKRAINE, 21000, 0, 6, "Wool", 19, Status.INEFFECTIVE)]

    # Object of ShopManager
    shopManager = ShopManager(list_of_looms)

    # # Search looms and print them
    # ShopManager.print_looms(shopManager.search_by("Wool", 6))
    #
    # # Sort looms and print them
    # ShopManager.print_looms(shopManager.sort_by_price(SortOrder.ASC))

    # # Sort looms and print them in reverse order
    # ShopManager.print_looms(shopManager.sort_by_price(SortOrder.DESC))

    # Sort looms and print them
    ShopManager.print_looms(shopManager.sort_by_power_in_watts(SortOrder.ASC))

    # # Sort looms and print them in reverse order
    # ShopManager.print_looms(shopManager.sort_by_power_in_watts(SortOrder.DESC))
