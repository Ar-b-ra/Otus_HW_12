from abc import ABC, abstractmethod
from typing import Callable, List, Any


class CollisionCheck(ABC):
    # Необходимо использовать этот класс как базовый
    # для создания собственной проверки коллизий
    @abstractmethod
    def check_collision(self, *args, **kwargs) -> bool:
        return True
class ICoRWorker(ABC):
    @abstractmethod
    def execute(self, context: Context) -> None:
        pass


IOn = Callable[[Context], bool]
IHandler = Callable[[Context], None]
IEHandler = Callable[[Context, Exception], None]


class CoRWorker(ICoRWorker):
    def __init__(self, on: IOn, handler: IHandler, ehandler: IEHandler) -> None:
        self._on = on
        self._handler = handler
        self._ehandler = ehandler

    def execute(self, context: Context) -> None:
        if self._on(context):
            try:
                self._handler(context)
            except Exception as e:
                self._ehandler(context, e)


class CoRChain(CoRWorker):
    def __init__(self, workers: List[ICoRWorker]) -> None:
        self._workers = workers

    def execute(self, context: Context) -> None:
        for worker in self._workers:
            worker.execute(context)
