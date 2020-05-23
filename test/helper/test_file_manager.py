import os
import unittest

from weird_converter.config import TEST_FOLDER_EXAMPLES, TEST_FILE_AUDIO, TEST_FOLDER_DATA, TEST_FILE_IMAGE, \
    EXTENSION_IMAGE
from weird_converter.helper import file_manager


class HelperFileManagerTest(unittest.TestCase):

    def setUp(self):
        self.input_file_path: str = os.path.join(TEST_FOLDER_EXAMPLES, TEST_FILE_AUDIO)
        self.extension: str = EXTENSION_IMAGE
        self.output_file_path_image: str = os.path.join(TEST_FOLDER_DATA, TEST_FILE_IMAGE)

    def test_generate_file_path_given(self):
        output_file_path: str = file_manager.generate_file_path(
            self.input_file_path, self.extension, self.output_file_path_image
        )
        self.assertIsNotNone(output_file_path)
        self.assertEqual(output_file_path, self.output_file_path_image)

    def test_generate_file_path(self):
        output_file_path: str = file_manager.generate_file_path(self.input_file_path, self.extension)
        self.assertIsNotNone(output_file_path)
        self.assertTrue(output_file_path.endswith(self.extension))
        self.assertEqual(os.path.dirname(self.input_file_path), os.path.dirname(output_file_path))
