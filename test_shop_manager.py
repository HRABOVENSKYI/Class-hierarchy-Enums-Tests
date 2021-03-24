import unittest

from managers.shop_manager import ShopManager, SortOrder
from models.loom import OriginCountry
from models.loom_types import HandLoom, Status, Shape
from models.mechanical_loom_types import WrapweightedLoom, FlyingLoom, DrawLoom


class TestShopManager(unittest.TestCase):

    def setUp(self):
        self.l1 = HandLoom(OriginCountry.UKRAINE, 18000, 0, 1, "Cotton", 19, Status.FUNCTIONAL)
        self.l2 = WrapweightedLoom(OriginCountry.CHINA, 4500, 120, 2, "Silk", Shape.FLAT)
        self.l3 = FlyingLoom(OriginCountry.USA, 12500, 850, 6, "Wool", Shape.CIRCULAR)
        self.l4 = DrawLoom(OriginCountry.GERMANY, 14999, 1200, 8, "Wool", Shape.SQUARE)
        self.l5 = FlyingLoom(OriginCountry.USA, 9999, 750, 5, "Silk", Shape.CIRCULAR)
        self.l6 = WrapweightedLoom(OriginCountry.CHINA, 4699, 165, 6, "Wool", Shape.FLAT)
        self.l7 = HandLoom(OriginCountry.UKRAINE, 21000, 0, 6, "Wool", 19, Status.INEFFECTIVE)

        self.shopManager = ShopManager(
            [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7]
        )

    def tearDown(self):
        pass

    def test_search_by(self):
        self.assertEqual(
            self.shopManager.search_by("Wool", 6),
            [self.l3, self.l6, self.l7]
        )

    def test_sort_by_price(self):
        self.assertEqual(
            self.shopManager.sort_by_price(SortOrder.ASC),
            [self.l2, self.l6, self.l5, self.l3, self.l4, self.l1, self.l7]
        )

        self.assertEqual(
            self.shopManager.sort_by_price(SortOrder.DESC),
            [self.l7, self.l1, self.l4, self.l3, self.l5, self.l6, self.l2]
        )

    def test_sort_by_power_in_watts(self):
        self.assertEqual(
            self.shopManager.sort_by_power_in_watts(SortOrder.ASC),
            [self.l1, self.l7, self.l2, self.l6, self.l5, self.l3, self.l4]
        )

        self.assertEqual(
            self.shopManager.sort_by_power_in_watts(SortOrder.DESC),
            [self.l4, self.l3, self.l5, self.l6, self.l2, self.l1, self.l7]
        )


if __name__ == "__main__":
    unittest.main()
