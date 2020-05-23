import os


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
    :return: True if the the path points to an existing directory, False otherwise.
    """
    if os.path.isdir(path):
        raise IsADirectoryError(f'Directory with path [{path}] must not exist.')
