import os
import unittest

from weird_converter.config import TEST_FOLDER_EXAMPLES, TEST_FILE_AUDIO, TEST_FOLDER_DATA, TEST_FILE_IMAGE, \
    TEST_FOLDER_IMAGE
from weird_converter.converter import image


class ConverterImageTest(unittest.TestCase):

    def setUp(self):
        self.input_file_path: str = os.path.join(TEST_FOLDER_EXAMPLES, TEST_FOLDER_IMAGE, TEST_FILE_IMAGE)
        self.output_file_path_audio: str = os.path.join(TEST_FOLDER_DATA, TEST_FILE_AUDIO)

    def test_to_audio(self):
        output_file_path: str = image.to_audio(self.input_file_path, self.output_file_path_audio)
        self.assertIsNotNone(output_file_path)
        self.assertEqual(output_file_path, self.output_file_path_audio)
