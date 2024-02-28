import cv2

from imagep.cv2.application import CV2


class BGR2Gray(CV2):
    def process(self) -> None:
        self.result = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


class Binary(CV2):
    required_params = ["threshold"]

    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result = cv2.threshold(gray_image, self.params["threshold"], 255, cv2.THRESH_BINARY)[-1]


class Reverse(CV2):
    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result = cv2.bitwise_not(gray_image)


class Sobel(CV2):
    required_params = ["ksize"]

    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=self.params["ksize"])
        y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=self.params["ksize"])
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        self.result = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


class Canny(CV2):
    required_params = ["threshold1", "threshold2"]

    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result = cv2.Canny(gray_image, self.params["threshold1"], self.params["threshold2"])


class Laplacian(CV2):
    required_params = ["ksize"]

    def process(self) -> None:
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.result = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=self.params["ksize"])
