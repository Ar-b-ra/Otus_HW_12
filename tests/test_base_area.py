import unittest

from area_imp import Areas
from ship import Ship


class TestArea(unittest.TestCase):
    def setUp(self):
        self.area = Areas()
        self.area.add_area(self.area)

    def test_check_add_object(self):
        ship = Ship(self.area)
        self.area.add_obj_to_area(self.area, ship)
        self.assertEqual(self.area.get_objects(self.area), {ship})
        self.assertEqual(ship.area, self.area)

    def test_check_remove_object(self):
        ship = Ship(self.area)
        self.area.add_obj_to_area(self.area, ship)
        self.area.remove_obj_from_area(self.area, ship)
        self.assertEqual(self.area.get_objects(self.area), set())
        self.assertNotEqual(ship.area, self.area)

    def test_find_obj_area(self):
        ship = Ship(self.area)
        with self.assertRaises(KeyError):
            self.assertNotEqual(self.area.find_obj_area(ship), self.area)
        self.area.add_obj_to_area(self.area, ship)
        self.assertEqual(self.area.find_obj_area(ship), self.area)


if __name__ == '__main__':
    unittest.main()
