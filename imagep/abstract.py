import abc

import numpy as np


class ImageProcess(abc.ABC):

    @abc.abstractmethod
    def loadImage(self, image: np.ndarray) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def loadImageFromPath(self, path: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def setParams(self, params: dict) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def getResult(self) -> np.ndarray:
        raise NotImplementedError

    @abc.abstractmethod
    def saveResult(self, path: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def process(self) -> None:
        raise NotImplementedError
