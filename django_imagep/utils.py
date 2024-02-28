import importlib


def imageProcess(image_path, data):
    if image_path:
        media_index = image_path.index("media/")
        image_path = image_path[media_index:]
    if data['function'] != "":
        # image process
        lib = importlib.import_module("imagep.cv2.process")
        module = getattr(lib, data['function'])()
        module.setParams(data['params'])
        module.loadImageFromPath(image_path)
        if not module.checkParams():
            raise ValueError("Invalid params")
        # export image
        image_name = image_path.split('/')[2]
        output_image_path = "media/images/{0}/{0}_{1}.png".format(image_name, data["id"])
        module.saveResult(output_image_path)
        data['image_url'] = "/" + output_image_path
    for child in data['child']:
        child = imageProcess(data['image_url'], child)
    return data


def upload_to(instance, filename):
    extension_index = filename.rfind('.')
    return f'images/{filename[:extension_index]}/{filename}'
