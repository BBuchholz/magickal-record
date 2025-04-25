import unittest
from constants import (
  TEST_FOLDER,
  CART_TEST_FILE_NO_CARDS,
  CART_TEST_FILE_SOME_CARDS,
  OBSIDIAN_TEST_FOLDER,
  OBSIDIAN_TEST_VAULT_ONE,
  OBSIDIAN_TEST_VAULT_TWO,
  BASIC_MYR_FILE_TEST_PATH,
  DSV_TEST_FOLDER,
  NONEXISTANT_FOLDER,
  EXISTANT_FILE,
  NONEXISTANT_FILE,
  CONFIG_FOLDER,
  CARTOGRAPHER_FOLDER,
  CETS_FILE,
)

from cfg import (
  TestingConfig,
  Config,
)

class TestTestingConfig(unittest.TestCase):
  def setUp(self):
    self.cfg = TestingConfig()
  
  def test_should_have_class(self):
    self.assertIsNotNone(self.cfg)

  def test_should_replace_constant_TEST_FOLDER(self):
    self.assertEqual(self.cfg.TEST_FOLDER, TEST_FOLDER)

  def test_should_replace_constant_CART_TEST_FILE_NO_CARDS(self):
    self.assertEqual(self.cfg.CART_TEST_FILE_NO_CARDS, CART_TEST_FILE_NO_CARDS)

  def test_should_replace_constant_CART_TEST_FILE_SOME_CARDS(self):
    self.assertEqual(self.cfg.CART_TEST_FILE_SOME_CARDS, CART_TEST_FILE_SOME_CARDS)

  def test_should_replace_constant_OBSIDIAN_TEST_FOLDER(self):
    self.assertEqual(self.cfg.OBSIDIAN_TEST_FOLDER, OBSIDIAN_TEST_FOLDER)

  def test_should_replace_constant_OBSIDIAN_TEST_VAULT_ONE(self):
    self.assertEqual(self.cfg.OBSIDIAN_TEST_VAULT_ONE, OBSIDIAN_TEST_VAULT_ONE)

  def test_should_replace_constant_OBSIDIAN_TEST_VAULT_TWO(self):
    self.assertEqual(self.cfg.OBSIDIAN_TEST_VAULT_TWO, OBSIDIAN_TEST_VAULT_TWO)

  def test_should_replace_constant_BASIC_MYR_FILE_TEST_PATH(self):
    self.assertEqual(self.cfg.BASIC_MYR_FILE_TEST_PATH, BASIC_MYR_FILE_TEST_PATH)

  def test_should_replace_constant_DSV_TEST_FOLDER(self):
    self.assertEqual(self.cfg.DSV_TEST_FOLDER, DSV_TEST_FOLDER)

  def test_should_replace_constant_NONEXISTANT_FOLDER(self):
    self.assertEqual(self.cfg.NONEXISTANT_FOLDER, NONEXISTANT_FOLDER)

  def test_should_replace_constant_EXISTANT_FILE(self):
    self.assertEqual(self.cfg.EXISTANT_FILE, EXISTANT_FILE)

  def test_should_replace_constant_NONEXISTANT_FILE(self):
    self.assertEqual(self.cfg.NONEXISTANT_FILE, NONEXISTANT_FILE)

class TestConfig(unittest.TestCase):
  def setUp(self):
    self.cfg = Config()
  
  def test_should_have_class(self):
    self.assertIsNotNone(self.cfg)

  def test_should_replace_constant_CONFIG_FOLDER(self):
    self.assertEqual(self.cfg.CONFIG_FOLDER, CONFIG_FOLDER)

  def test_should_replace_constant_CARTOGRAPHER_FOLDER(self):
    self.assertEqual(self.cfg.CARTOGRAPHER_FOLDER, CARTOGRAPHER_FOLDER)

  def test_should_replace_constant_CETS_FILE(self):
    self.assertEqual(self.cfg.CETS_FILE, CETS_FILE)