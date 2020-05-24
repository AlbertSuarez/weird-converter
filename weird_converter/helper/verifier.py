import os

from PIL import Image, UnidentifiedImageError

from weird_converter.config import EXTENSION_AUDIO


def must_file_exist(path: str):
    """
    Checks if a given path points to an existing file.
    :param path: Given path.
    :return: True if the path points to an existing file, False otherwise.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f'File with path [{path}] must exist.')


def must_not_directory_exist(path: str):
    """
    Checks if a given path points to an existing directory.
    :param path: Given path.
    :return: True if the path points to an existing directory, False otherwise.
    """
    if os.path.isdir(path):
        raise IsADirectoryError(f'Directory with path [{path}] must not exist.')


def is_audio(path: str):
    """
    Checks if a given path points to a valid audio file.
    :param path: Given path.
    :return: True if the path points to an audio file, False otherwise.
    """
    if os.path.splitext(os.path.basename(path))[-1].lower() != f'.{EXTENSION_AUDIO}':
        raise ValueError(f'File with path [{path}] is not a {EXTENSION_AUDIO} type of file.')


def is_image(path: str):
    """
    Checks if a given path points to a valid image file.
    :param path: Given path.
    :return: True if the path points to an image file, False otherwise.
    """
    try:
        image = Image.open(path)
        image.verify()
        image.close()
    except UnidentifiedImageError:
        raise ValueError(f'File with path [{path}] is not a image type of file.')
