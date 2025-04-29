import unittest
import os

from crawler import Crawler
# from constants import (
#   OBSIDIAN_TEST_VAULT_ONE,
#   OBSIDIAN_TEST_VAULT_TWO,
# )
from cfg import NwdTestConfig

class TestCrawler(unittest.TestCase):
  def test_get_adjacent_folders(self):
    tcfg = NwdTestConfig()
    vault_one = tcfg.obsidian_test_vault_one()
    vault_two = tcfg.obsidian_test_vault_two()
    crwlr = Crawler(vault_one)
    adjacent_folders = crwlr.get_adjacent_folders()
    testVaultTwo = os.path.expanduser(vault_two)
    self.assertIn(testVaultTwo, adjacent_folders)
