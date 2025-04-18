import unittest

from files import (
  get_lines_array,
  print_lines_array,
  folder_exists,
  get_xslx_files,
  get_path_in_folder,
  path_exists,
)

from constants import (
  EXISTANT_FILE,
  NONEXISTANT_FILE,
  TEST_FOLDER,
  NONEXISTANT_FOLDER,
  CARTOGRAPHER_FOLDER,
  CART_TEST_FILE_NO_CARDS,
)

class TestFiles(unittest.TestCase):
  def test_get_lines_array(self):
    arr = get_lines_array(EXISTANT_FILE)
    self.assertEqual(len(arr), 5)
    arr = get_lines_array(NONEXISTANT_FILE)
    self.assertEqual(len(arr), 0)
  
  def test_folder_exists(self):
    self.assertFalse(folder_exists(NONEXISTANT_FOLDER))
    self.assertTrue(folder_exists(TEST_FOLDER))
  
  def test_should_get_xslx_files(self):
    files_found = get_xslx_files(TEST_FOLDER)
    self.assertIn("TEST_DONOTMODIFY_NoCards.xlsx", files_found)

  def test_get_path_in_folder(self):
    file_path = get_path_in_folder(CARTOGRAPHER_FOLDER, CART_TEST_FILE_NO_CARDS)
    self.assertTrue(path_exists(file_path))
   

if __name__ == '__main__':
  unittest.main()