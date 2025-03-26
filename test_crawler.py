import unittest
import os

from crawler import Crawler
from constants import (
  OBSIDIAN_TEST_VAULT_ONE,
  OBSIDIAN_TEST_VAULT_TWO,
)

class TestCrawler(unittest.TestCase):
  def test_get_adjacent_folders(self):
    crwlr = Crawler(OBSIDIAN_TEST_VAULT_ONE)
    adjacent_folders = crwlr.get_adjacent_folders()
    testVaultTwo = os.path.expanduser(OBSIDIAN_TEST_VAULT_TWO)
    self.assertIn(testVaultTwo, adjacent_folders)
