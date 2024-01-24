from typing import List

from area_imp import Areas
from chain import CollisionCheck, CollisionCheckerError
from ship import Ship


class SimpleCollisionChecker(CollisionCheck):
    def __init__(self, locality: List[Areas], ship: Ship, ships_to_check: List[Ship]):
        self.locality = locality[1]
        self.ship = ship
        self.ships_to_check = ships_to_check

    def check_collision(self, *args, **kwargs) -> bool:
        for _ship in self.ships_to_check:
            if self.locality.find_obj_area(_ship) == self.locality.find_obj_area(self.ship):
                raise CollisionCheckerError(f"{self.ship} and {_ship} are in the same area")
        return False

    def handle_collision(self, exception: BaseException, *args, **kwargs):
        print(exception)
