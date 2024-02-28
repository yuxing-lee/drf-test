import cv2


def imageProcess(image_path, data):
    if image_path:
        media_index = image_path.index("media/")
        image_path = image_path[media_index:]
    if data['function'] != "":
        # image process
        image = cv2.imread(image_path)
        function = globals()[data['function']]
        image = function(image, data['params'])
        # export image
        image_name = image_path.split('/')[2]
        output_image_path = "media/images/{0}/{0}_{1}.png".format(image_name, data["id"])
        cv2.imwrite(output_image_path, image)
        data['image_url'] = "/" + output_image_path
    for child in data['child']:
        child = imageProcess(data['image_url'], child)
    return data


def bgr2gray(image, params):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def binary(image, params):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary_image = cv2.threshold(gray_image, params["threshold"], 255, cv2.THRESH_BINARY)
    return binary_image


def reverse(image, params):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.bitwise_not(gray_image)


def sobel(image, params):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=params["ksize"])
    y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=params["ksize"])
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


def canny(image, params):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray_image, params["threshold1"], params["threshold2"])


def laplacian(image, params):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray_image, cv2.CV_64F, ksize=params["ksize"])
