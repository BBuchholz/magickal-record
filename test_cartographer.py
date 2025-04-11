import unittest

from cartographer import Cartographer
from constants import (
  CARTOGRAPHER_FOLDER,
  CART_TEST_FILE_NO_CARDS,
  CART_TEST_FILE_SOME_CARDS,
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
    self.assertIn(CART_TEST_FILE_NO_CARDS, cg.get_cart_files())
    
  def test_should_get_release_name_from_line(self):
    cg = Cartographer()
    name = cg.get_release_file_name_from_line("- [ ] [[LMS24A]]")
    self.assertEqual(name, "LMS24A")

  def test_should_get_myrkis(self):
    cg = Cartographer()
    cg.selected_file = CART_TEST_FILE_SOME_CARDS
    myrkis = cg.get_myrkis()
    self.assertIn("SERPENT", myrkis)

  def test_should_get_related_myrkis(self):
    cg = Cartographer()
    cg.selected_file = CART_TEST_FILE_SOME_CARDS
    myrkis = cg.get_related_myrkis()
    self.assertIn("DIMENSION", myrkis)

  def test_should_get_unconnected_myrkis(self):
    cg = Cartographer()
    cg.selected_file = CART_TEST_FILE_SOME_CARDS
    myrkis = cg.get_unconnected_myrkis()
    self.assertIn("UNICORN", myrkis)