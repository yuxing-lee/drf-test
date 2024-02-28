import cv2
import numpy as np

from imagep.abstract import ImageProcess


class CV2(ImageProcess):

    required_params = []
    optional_params = []

    def __init__(self):
        self.image = None
        self.result = None
        self.params = None

    def loadImage(self, image: np.ndarray) -> None:
        self.image = image
        self.result = None

    def loadImageFromPath(self, path: str) -> None:
        self.image = cv2.imread(path)
        self.result = None

    def setParams(self, params: dict) -> None:
        self.params = params
        self.result = None

    def checkParams(self) -> bool:
        param_keys = self.params.keys()
        # check required params
        for param in self.required_params:
            if param not in param_keys:
                return False
        return True

    def getResult(self) -> np.ndarray:
        if self.result is None:
            self.process()
        return self.result

    def saveResult(self, path: str) -> None:
        if self.result is None:
            self.process()
        cv2.imwrite(path, self.result)

    def process(self) -> None:
        raise NotImplementedError
