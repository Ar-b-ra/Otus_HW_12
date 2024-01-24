import unittest
from unittest.mock import patch

from area_imp import Areas
from collision_checker import SimpleCollisionChecker
from ship import Ship


class TestSimpleChecker(unittest.TestCase):
    def setUp(self):
        self.checkers = [SimpleCollisionChecker]
        self.area_1 = Areas(self.checkers)
        self.area_2 = Areas(self.checkers)
        self.ship_1 = Ship(self.area_1)
        self.ship_2 = Ship(self.area_1)
        self.area_1.add_area(self.area_1)
        self.area_1.add_area(self.area_2)
        self.area_1.add_obj_to_area(self.area_1, self.ship_1)
        self.area_1.add_obj_to_area(self.area_1, self.ship_2)

    def test_objs_in_different_areas(self):
        with self.assertRaises(KeyError):
            self.area_2.change_obj_area(self.ship_1, self.area_2)

    @patch("collision_checker.SimpleCollisionChecker.check_collision", return_value=True)
    def test_objs_with_one_area(self, mock_check_collision):
        self.area_1.change_obj_area(self.ship_1, self.area_2)
        mock_check_collision.assert_called()
        # self.assertEqual(self.area_1.get_objects(self.area_2), {self.ship_1, self.ship_2})

    def test_objs_with_two_areas(self):
        self.area_1.areas[self.area_2] = {self.ship_1, self.ship_2}
        self.area_2.areas[self.area_1] = {self.ship_1, self.ship_2}
        self.assertTrue(self.area_1.change_obj_area(self.ship_1, self.area_2))
        self.assertEqual(self.area_1.get_objects(self.area_2), {self.ship_1, self.ship_2})
        self.assertEqual(self.area_2.get_objects(self.area_1), {self.ship_1, self.ship_2})
