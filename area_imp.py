from typing import Dict, List

from chain import Context, CoRWorker
from ship import Ship


class Areas:
    def __init__(self, workers: List[CoRWorker]):
        self.areas: Dict["Areas", list] = {}
        self.context = Context()
        self.workers = workers

    def add_area(self, locality: "Areas"):
        self.areas[locality] = []

    def add_obj_to_area(self, locality: "Areas", obj: Ship):
        self.areas[locality].append(obj)

    def remove_obj_from_area(self, locality, obj: Ship):
        self.areas[locality].remove(obj)

    def find_obj_area(self, obj: Ship):
        for key, value in self.areas:
            if obj in value:
                return self.areas[key]

    def change_obj_area(self, obj, new_area):
        if obj.area != (old_area := self.find_obj_area(obj)):
            self.remove_obj_from_area(old_area, obj)
            self.add_obj_to_area(new_area, obj)
            obj.area = new_area
            for worker in self.workers:
                worker.execute()

    def get_objects(self, locality: "Areas"):
        return self.areas[locality]

