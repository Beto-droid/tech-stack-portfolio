from PIL import Image, ImageFilter
import os


def create_low_res_image(image_path, low_res_suffix="_low", size=(100, 100), blur_radius=5):
    """
    Create a low-resolution, blurred version of an image for use as a placeholder.

    Args:
        image_path (str): Path to the original image.
        low_res_suffix (str): Suffix for the low-res image filename.
        size (tuple): Target size for low-res image (width, height).
        blur_radius (int): Radius for Gaussian blur effect.
    """
    img = Image.open(image_path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    img = img.filter(ImageFilter.GaussianBlur(blur_radius))
    low_res_path = os.path.splitext(image_path)[0] + low_res_suffix + os.path.splitext(image_path)[1]
    img.save(low_res_path)