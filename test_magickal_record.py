import unittest

from magickal_record import MagickalRecord
from constants import (
  TEST_FOLDER,
  DSV_TEST_FOLDER,
)

class TestMagickalRecord(unittest.TestCase):
  def test_should_have_an_associated_folder(self):
    mr = MagickalRecord(DSV_TEST_FOLDER)
    self.assertIsNotNone(mr.folder_path)
    self.assertEqual(mr.folder_path, DSV_TEST_FOLDER)

  def test_should_default_to_test_folder(self):
    mr = MagickalRecord()
    self.assertIsNotNone(mr.folder_path)
    self.assertEqual(mr.folder_path, TEST_FOLDER)

  def test_should_verify_designated_folder(self):
    mr = MagickalRecord()
    self.assertTrue(mr.folder_exists())
    mr2 = MagickalRecord("~/doesNotExist")
    self.assertFalse(mr2.folder_exists())