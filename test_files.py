import unittest

from files import (
  get_lines_array,
  print_lines_array,
  folder_exists,
)

from constants import (
  EXISTANT_FILE,
  NONEXISTANT_FILE,
  TEST_FOLDER,
  NONEXISTANT_FOLDER,
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

if __name__ == '__main__':
  unittest.main()