from scipy.io import wavfile


def to_image(input_file_path: str, output_file_path: str) -> str:
    """
    Converts an existing audio file to an image.
    :param input_file_path: Existing file path pointing to an audio file.
    :param output_file_path: Output file path.
    :return: File path pointing to the generated output image.
    """
    fs, data = wavfile.read(input_file_path)
    return output_file_path
