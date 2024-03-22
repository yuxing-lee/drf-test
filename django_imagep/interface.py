import abc

import numpy as np


class IProcessing(abc.ABC):

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
    def checkParams(self) -> bool:
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


class IProcessingFactory(abc.ABC):
    @abc.abstractmethod
    def createProcessing(self) -> IProcessing:
        raise NotImplementedError


class ILibraryFactory(abc.ABC):
    @abc.abstractmethod
    def openLibrary(self) -> IProcessingFactory:
        raise NotImplementedError
