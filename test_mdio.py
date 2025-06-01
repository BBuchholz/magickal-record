import unittest
from mdio import MDIO
from chronio import ChronIO
from files import get_path_in_folder
import os

class TestMDIO(unittest.TestCase):
  def setUp(self):
    self.mdio = MDIO()

  ####### NB: this test just creates too many folders, and is not needed 
  # def test_should_ensure_folder(self):
  #   debugging = False
  #   cm = ChronIO()
  #   sfx = cm.get_suffix()
  #   folder_path = get_path_in_folder("~/nwd/test", sfx)
  #   while os.path.exists(folder_path):
  #     sfx = cm.get_suffix(sfx)
  #     folder_path = get_path_in_folder("~/nwd/test", sfx)
  #   if debugging:
  #     print(f"checking if path exists: {folder_path}")
  #   self.assertFalse(os.path.exists(folder_path))
  #   if debugging:
  #     print(f"creating folder at: {folder_path}")
  #   self.mdio.ensure_folder(folder_path)
  #   self.assertTrue(os.path.exists(folder_path))
