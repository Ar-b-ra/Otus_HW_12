from area_imp import Areas
from collision_checker import SimpleCollisionChecker
from ship import Ship


if __name__ == "__main__":
    checkers = [SimpleCollisionChecker]
    area_1 = Areas(checkers)
    area_2 = Areas(checkers)
    ship_1 = Ship(area_2)
    ship_2 = Ship(area_2)
    area_1.areas[area_2] = [ship_1, ship_2]
    area_1.add_obj_to_area(area_2, ship_1)
    area_2.add_obj_to_area(area_1, ship_2)
