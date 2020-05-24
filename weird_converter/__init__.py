from weird_converter.config import EXTENSION_IMAGE, EXTENSION_AUDIO
from weird_converter.converter import audio, image
from weird_converter.helper import verifier, file_manager


def audio_to_image(input_file_path: str, output_file_path: str = None) -> str:
    """
    Converts from an input audio file into an image.
    :param input_file_path: Existing file path pointing to an audio file.
    :param output_file_path: Optional output file path.
    :return: File path pointing to the generated output image.
    """
    verifier.must_file_exist(input_file_path)
    verifier.is_audio(input_file_path)
    output_file_path: str = file_manager.generate_file_path(input_file_path, EXTENSION_IMAGE, output_file_path)
    verifier.must_not_directory_exist(output_file_path)
    return audio.to_image(input_file_path, output_file_path)


def image_to_audio(input_file_path: str, output_file_path: str = None) -> str:
    """
    Converts from an input image file into an audio.
    :param input_file_path: Existing file path pointing to an image file.
    :param output_file_path: Optional output file path.
    :return: File path pointing to the generated output audio.
    """
    verifier.must_file_exist(input_file_path)
    verifier.is_image(input_file_path)
    output_file_path: str = file_manager.generate_file_path(input_file_path, EXTENSION_AUDIO, output_file_path)
    verifier.must_not_directory_exist(output_file_path)
    return image.to_audio(input_file_path, output_file_path)
