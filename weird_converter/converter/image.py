import numpy as np

from PIL import Image
from scipy.io import wavfile


def to_audio(input_file_path: str, output_file_path: str) -> str:
    """
    Converts an existing image file to an audio.
    :param input_file_path: Existing file path pointing to an image file.
    :param output_file_path: Output file path.
    :return: File path pointing to the generated output audio.
    """
    # Read image file for converting into a numpy array
    image = Image.open(input_file_path).convert('RGB')
    image_array = np.array(image)
    image.close()

    samples_per_second = 44100  # Default samples per second on a WAV file
    image_array = image_array.reshape(image_array.size)  # Flatten image array
    image_array = 2. * (image_array - np.min(image_array)) / np.ptp(image_array) - 1  # Normalize to [-1, 1]
    image_array = np.int16(image_array / np.max(np.abs(image_array)) * 32767)  # Cast to int16

    # Save as an audio
    wavfile.write(output_file_path, samples_per_second, image_array)

    return output_file_path
