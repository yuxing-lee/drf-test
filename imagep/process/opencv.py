import cv2

from imagep.library import OpenCV


class BGR2Gray(OpenCV):
    def process(self) -> None:
        self.result = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


class Binary(OpenCV):
    required_params = ["threshold"]

    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result = cv2.threshold(gray_image, self.params["threshold"], 255, cv2.THRESH_BINARY)[-1]


class Reverse(OpenCV):
    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result = cv2.bitwise_not(gray_image)


class Sobel(OpenCV):
    required_params = ["ksize"]

    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=self.params["ksize"])
        y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=self.params["ksize"])
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        self.result = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


class Canny(OpenCV):
    required_params = ["threshold1", "threshold2"]

    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result = cv2.Canny(gray_image, self.params["threshold1"], self.params["threshold2"])


class Laplacian(OpenCV):
    required_params = ["ksize"]

    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=self.params["ksize"])


class GaussianBlur(OpenCV):
    required_params = ["ksize"]

    def process(self) -> None:
        self.result = cv2.GaussianBlur(self.image, (self.params["ksize"], self.params["ksize"]), 0)


class MedianBlur(OpenCV):
    required_params = ["ksize"]

    def process(self) -> None:
        self.result = cv2.medianBlur(self.image, self.params["ksize"])


class BilateralFilter(OpenCV):
    required_params = ["d", "sigmaColor", "sigmaSpace"]

    def process(self) -> None:
        self.result = cv2.bilateralFilter(self.image, self.params["d"], self.params["sigmaColor"], self.params["sigmaSpace"])


class Erosion(OpenCV):
    required_params = ["ksize", "iterations"]

    def process(self) -> None:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.params["ksize"], self.params["ksize"]))
        self.result = cv2.erode(self.image, kernel, iterations=self.params["iterations"])


class Dilation(OpenCV):
    required_params = ["ksize", "iterations"]

    def process(self) -> None:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.params["ksize"], self.params["ksize"]))
        self.result = cv2.dilate(self.image, kernel, iterations=self.params["iterations"])


class Opening(OpenCV):
    required_params = ["ksize", "iterations"]

    def process(self) -> None:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.params["ksize"], self.params["ksize"]))
        self.result = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel, iterations=self.params["iterations"])


class Closing(OpenCV):
    required_params = ["ksize", "iterations"]

    def process(self) -> None:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.params["ksize"], self.params["ksize"]))
        self.result = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel, iterations=self.params["iterations"])
