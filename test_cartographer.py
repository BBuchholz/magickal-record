import unittest

from cartographer import Cartographer
from constants import (
  CARTOGRAPHER_FOLDER,
)

class TestCartographer(unittest.TestCase):
  def test_should_check_for_cartographer_folder(self):
    cg = Cartographer()
    self.assertTrue(cg.verify_folder())

  def test_should_look_for_cets_file(self):
    cg = Cartographer()
    self.assertTrue(cg.verify_cets_file())

  def test_should_get_release_names(self):
    cg = Cartographer()
    self.assertIn("LMS24A", cg.get_release_file_names())

  def test_should_get_cart_files(self):
    cg = Cartographer()
    self.assertIn("TEST_DONOTMODIFY_NoCards.xlsx", cg.get_cart_files())
    
  def test_should_get_release_name_from_line(self):
    cg = Cartographer()
    name = cg.get_release_file_name_from_line("- [ ] [[LMS24A]]")
    self.assertEqual(name, "LMS24A")