def upload_to(instance, filename):
    extension_index = filename.rfind('.')
    return f'images/{filename[:extension_index]}/{filename}'
