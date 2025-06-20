import unittest
from profile_examples import ProfileExample
from files import path_exists

class TestProfileExamples(unittest.TestCase):
  def setUp(self):
    self.profs = ProfileExample()

  def test_should_have_example_file(self):
    example_file = self.profs.example_file()
    self.assertTrue(path_exists(example_file))

  def test_should_have_example_folder(self):
    example_folder = self.profs.example_folder()
    self.assertTrue(path_exists(example_folder))

  def test_should_have_example_git_folder(self):
    example_git_folder = self.profs.example_git_folder()
    self.assertTrue(path_exists(example_git_folder))

  def test_should_have_example_io_folder(self):
    example_io_folder = self.profs.example_io_folder()
    self.assertTrue(path_exists(example_io_folder))

  def test_should_have_example_md_file(self):
    example_md_file = self.profs.example_md_file()
    self.assertTrue(path_exists(example_md_file))

  def test_should_have_example_myrki_instance_file(self):
    example_myrki_instance_file = self.profs.example_myrki_instance_file()
    self.assertTrue(path_exists(example_myrki_instance_file))