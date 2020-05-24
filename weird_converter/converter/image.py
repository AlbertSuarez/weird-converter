import numpy as np

from PIL import Image


def to_audio(input_file_path: str, output_file_path: str) -> str:
    """
    Converts an existing image file to an audio.
    :param input_file_path: Existing file path pointing to an image file.
    :param output_file_path: Output file path.
    :return: File path pointing to the generated output audio.
    """
    image = Image.open(input_file_path).convert('RGB')
    image_array = np.array(image)

    return output_file_path
