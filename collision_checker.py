from abc import ABC, abstractmethod
from typing import List

from area_imp import Areas
from ship import Ship





class RealCollisionChecker(CollisionCheck):
    def __init__(self, locality: Areas, ships: List[Ship]):
        self.locality = locality
        self.ships = ships

    def add_object(self, ship: Ship):
        if ship not in self.ships:
            self.ships.append(ship)

    def check_collision(self, obj1: Ship, obj2: Ship) -> bool:
        if obj1.locality == obj2.locality == self.locality:
            return False
        else:
            return True
