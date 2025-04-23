import unittest
from mdio import MDIO
from chronio import ChronIO
from files import get_path_in_folder
import os

class TestMDIO(unittest.TestCase):
  def setUp(self):
    self.mdio = MDIO()

  def test_should_ensure_folder(self):
    cm = ChronIO()
    timestamp = cm.get_timestamp()
    folder_path = get_path_in_folder("~/nwd/test", timestamp)
    self.assertFalse(os.path.exists(folder_path))
    self.mdio.ensure_folder(folder_path)
    self.assertTrue(os.path.exists(folder_path))
