import os
import unittest

from weird_converter.config import TEST_FOLDER_EXAMPLES, TEST_FILE_AUDIO, TEST_FOLDER_DATA, TEST_FOLDER_AUDIO, \
    TEST_FILE_IMAGE
from weird_converter.helper import verifier


class HelperVerifierTest(unittest.TestCase):

    def setUp(self):
        self.existing_file_path: str = os.path.join(TEST_FOLDER_EXAMPLES, TEST_FOLDER_AUDIO, TEST_FILE_AUDIO)
        self.non_existing_file_path: str = os.path.join(TEST_FOLDER_DATA, TEST_FILE_AUDIO)
        self.directory_path: str = TEST_FOLDER_EXAMPLES
        self.non_audio_file_path: str = os.path.join(TEST_FOLDER_DATA, TEST_FILE_IMAGE)

    def test_must_file_exist_success(self):
        verifier.must_file_exist(self.existing_file_path)
        self.assertTrue(True)

    def test_must_file_exist_error(self):
        with self.assertRaises(FileNotFoundError):
            verifier.must_file_exist(self.non_existing_file_path)

    def test_must_not_directory_exist_success(self):
        verifier.must_not_directory_exist(self.existing_file_path)
        self.assertTrue(True)

    def test_must_not_directory_exist_error(self):
        with self.assertRaises(IsADirectoryError):
            verifier.must_not_directory_exist(self.directory_path)

    def test_is_audio_success(self):
        verifier.is_audio(self.existing_file_path)
        self.assertTrue(True)

    def test_is_audio_error(self):
        with self.assertRaises(ValueError):
            verifier.is_audio(self.non_audio_file_path)
