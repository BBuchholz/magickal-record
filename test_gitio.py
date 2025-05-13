import unittest

from gitio import GitIO

class TestGitIO(unittest.TestCase):
  def setUp(self):
    self.gio = GitIO()

  def test_should_have_class(self):
    self.assertIsNotNone(self.gio)

  def test_should_list_repos(self):
    repo_list = self.gio.list_repos()
    expected = 0 # None configured yet
    self.assertEqual(len(repo_list), expected)

  def test_should_add_repo(self):
    repo_list = self.gio.list_repos()
    expected = len(repo_list) + 1
    short_name = "nwd"
    rel_address = "~/nwd"
    self.gio.add_repo(short_name, rel_address)

  def test_non_relative_address_raises_exception(self):
    with self.assertRaises(ValueError):
      self.gio.add_repo("Invalid", "/nwd")

  def test_non_relative_addr_exception_msg(self):
    expected = "repo addresses must be relative, ie. beginning with '~/someFolder'"
    with self.assertRaises(ValueError) as context:
      self.gio.add_repo("Invalid", "/nwd")
    self.assertEqual(str(context.exception), expected)
  