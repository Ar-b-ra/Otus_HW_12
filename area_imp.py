from typing import Dict, List

from chain import CoRWorker, CoRChain
from ship import Ship


class Areas:
    def __init__(self, checkers: List = None):
        self.areas: Dict["Areas", set] = {}
        self.checkers = checkers

    def add_area(self, locality: "Areas"):
        if locality not in self.areas.keys():
            self.areas[locality] = set()

    def add_obj_to_area(self, locality: "Areas", obj: Ship):
        self.areas[locality].add(obj)
        obj.area = locality

    def remove_obj_from_area(self, locality, obj: Ship):
        self.areas[locality].remove(obj)
        obj.area = None

    def find_obj_area(self, obj: Ship):
        for key, value in self.areas.items():
            if obj in value:
                return key
        self.unable_to_change_obj(obj, KeyError)

    def change_obj_area(self, obj, new_area):
        if obj.area != new_area:
            old_area = self.find_obj_area(obj)
            self.remove_obj_from_area(old_area, obj)
            self.add_obj_to_area(new_area, obj)
            workers = []
            for checker in self.checkers:
                _checker = checker(locality=[old_area, new_area], ship=obj, ships_to_check=self.areas[new_area])
                _worker = CoRWorker(on=lambda _chk: True,
                                    handler=_checker.check_collision,
                                    ehandler=_checker.handle_collision)
                workers.append(_worker)
            executer = CoRChain(workers)
            executer.execute(new_area)
        return True

    def get_objects(self, locality: "Areas"):
        return self.areas[locality]

    def unable_to_change_obj(self, obj, exc):
        raise exc(f"{obj} unable to find area")
