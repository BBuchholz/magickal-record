import unittest

from files import (
  get_lines_array,
  print_lines_array,
  folder_exists,
  get_xslx_files,
  get_path_in_folder,
  path_exists,
)
from cfg import (
  NwdTestConfig, 
  NwdConfig,
)
from constants import (
  # EXISTANT_FILE,
  # NONEXISTANT_FILE,
  # TEST_FOLDER,
  # NONEXISTANT_FOLDER,
  # CARTOGRAPHER_FOLDER,
  CART_TEST_FILE_NO_CARDS,
)

class TestFiles(unittest.TestCase):
  def test_get_lines_array(self):
    tcfg = NwdTestConfig()
    arr = get_lines_array(tcfg.existant_file())
    self.assertEqual(len(arr), 5)
    arr = get_lines_array(tcfg.nonexistant_file())
    self.assertEqual(len(arr), 0)
  
  def test_folder_exists(self):
    tcfg = NwdTestConfig()
    ne_folder = tcfg.nonexistant_folder()
    self.assertFalse(folder_exists(ne_folder))
    tst_folder = tcfg.test_folder()
    self.assertTrue(folder_exists(tst_folder))
  
  def test_should_get_xslx_files(self):
    tcfg = NwdTestConfig()
    tst_folder = tcfg.test_folder()
    files_found = get_xslx_files(tst_folder)
    self.assertIn("TEST_DONOTMODIFY_NoCards.xlsx", files_found)

  def test_get_path_in_folder(self):
    cfg = NwdConfig()
    file_path = get_path_in_folder(cfg.cartio_folder(), CART_TEST_FILE_NO_CARDS)
    self.assertTrue(path_exists(file_path))
   

if __name__ == '__main__':
  unittest.main()