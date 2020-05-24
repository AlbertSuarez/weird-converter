import os
import unittest

from weird_converter import audio_to_image
from weird_converter.config import TEST_FOLDER_EXAMPLES, TEST_FOLDER_AUDIO, TEST_FILE_AUDIO_LIST


class AudioToImageTest(unittest.TestCase):

    def setUp(self):
        self.input_file_path_list: list = [
            os.path.join(TEST_FOLDER_EXAMPLES, TEST_FOLDER_AUDIO, file_name)
            for file_name in TEST_FILE_AUDIO_LIST
        ]

    def test_to_image(self):
        for input_file_path in self.input_file_path_list:
            output_file_path: str = audio_to_image(input_file_path)
            self.assertIsNotNone(output_file_path)
            self.assertEqual(os.path.dirname(input_file_path), os.path.dirname(output_file_path))
