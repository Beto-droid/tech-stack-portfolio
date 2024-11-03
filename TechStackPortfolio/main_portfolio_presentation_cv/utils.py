from PIL import Image, ImageFilter
import os
from functools import wraps

def optimize_and_create_low_res(*image_fields):
    """
    Optimize the image and create low res image decorator.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(instance, *args, **kwargs):
            func(instance, *args, **kwargs)

            for field_name in image_fields:
                image_field = getattr(instance, field_name)
                if image_field:
                    create_low_res_image(image_field.path)
                    optimize_image(image_field.path)

        return wrapper

    def create_low_res_image(image_path, low_res_suffix="_low", size=(100, 100), blur_radius=5):
        """
        Create low res image
        """
        img = Image.open(image_path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        img = img.filter(ImageFilter.GaussianBlur(blur_radius))
        low_res_path = os.path.splitext(image_path)[0] + low_res_suffix + os.path.splitext(image_path)[1]
        img.save(low_res_path)

    def optimize_image(image_path):
        """
        Optimize Image
        """
        img = Image.open(image_path)
        if img.height > 1080 or img.width > 1920:
            img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
            img.save(image_path)

    return decorator
