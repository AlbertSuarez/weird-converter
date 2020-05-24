import os
import unittest

from weird_converter import image_to_audio
from weird_converter.config import TEST_FOLDER_EXAMPLES, TEST_FOLDER_IMAGE, TEST_FILE_IMAGE_LIST


class ImageToAudioTest(unittest.TestCase):

    def setUp(self):
        self.input_file_path_list: list = [
            os.path.join(TEST_FOLDER_EXAMPLES, TEST_FOLDER_IMAGE, file_name)
            for file_name in TEST_FILE_IMAGE_LIST
        ]

    def test_to_audio(self):
        for input_file_path in self.input_file_path_list:
            output_file_path: str = image_to_audio(input_file_path)
            self.assertIsNotNone(output_file_path)
            self.assertEqual(os.path.dirname(input_file_path), os.path.dirname(output_file_path))
