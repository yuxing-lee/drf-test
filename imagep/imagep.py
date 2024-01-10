import cv2


def imageProcess(image_path, data):
    image_url = data['image_url']
    if image_url != "":
        media_index = image_url.index("media/")
        data['image_url'] = image_url[media_index:]
    if data['function'] != "":
        image = cv2.imread(image_path)
        image = bgr2gray(image)
        image_name = image_path.split('/')[2]
        output_image_path = "media/images/{0}/{0}_{1}.png".format(image_name, data["id"])
        cv2.imwrite(output_image_path, image)
        data['image_url'] = "/" + output_image_path
    for child in data['child']:
        child = imageProcess(data['image_url'], child)
    return data


def bgr2gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
