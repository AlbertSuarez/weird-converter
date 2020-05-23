import os
import unittest

from weird_converter.config import TEST_FOLDER_EXAMPLES, TEST_FILE_AUDIO, TEST_FOLDER_DATA, TEST_FILE_IMAGE
from weird_converter.converter import audio


class ConverterAudioTest(unittest.TestCase):

    def setUp(self):
        self.input_file_path: str = os.path.join(TEST_FOLDER_EXAMPLES, TEST_FILE_AUDIO)
        self.output_file_path_image: str = os.path.join(TEST_FOLDER_DATA, TEST_FILE_IMAGE)

    def test_to_image(self):
        output_file_path: str = audio.to_image(self.input_file_path, self.output_file_path_image)
        self.assertIsNotNone(output_file_path)
        self.assertEqual(output_file_path, self.output_file_path_image)
