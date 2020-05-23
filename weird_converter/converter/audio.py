import math

from functools import reduce
import numpy as np

from PIL import Image
from scipy.io import wavfile


def to_image(input_file_path: str, output_file_path: str) -> str:
    """
    Converts an existing audio file to an image.
    :param input_file_path: Existing file path pointing to an audio file.
    :param output_file_path: Output file path.
    :return: File path pointing to the generated output image.
    """
    # Read WAV file for converting into a numpy array
    try:
        fs, data = wavfile.read(input_file_path)
    except ValueError:
        raise ValueError('Parsing could not be possible maybe because it is not an audio. Try again with another file.')

    # Copying data to a new non-read-only numpy array
    audio_array = np.empty_like(data)
    audio_array[:] = data

    image_dimensions = int(math.sqrt(audio_array.size / 3))  # Compute ideal image dimensions
    amount_values = pow(image_dimensions, 2) * 3  # Compute needed values from audio array

    audio_array = audio_array.reshape(reduce(lambda x, y: x * y, audio_array.shape))  # Flatten audio array
    audio_array = np.random.choice(audio_array, size=amount_values)  # Get the needed amount values
    audio_array = audio_array.reshape(image_dimensions, image_dimensions, 3)  # Reshape to the image shape
    audio_array = audio_array.astype('float64')  # Cast to the image type
    audio_array *= (255.0 / audio_array.max())  # Normalize to RGB [0-255]

    # Save as an image
    img = Image.fromarray(audio_array, 'RGB')
    img.save(output_file_path, quality=95)

    return output_file_path
