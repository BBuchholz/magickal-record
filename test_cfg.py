import unittest
from os import path
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
  CARTOGRAPHER_FOLDER,
  CETS_FILE,
)

from cfg import (
  NwdTestConfig,
  NwdConfig,
)

class TestNwdTestConfig(unittest.TestCase):
  def setUp(self):
    self.cfg = NwdTestConfig()
  
  def test_should_have_class(self):
    self.assertIsNotNone(self.cfg)

  def test_should_have_xlsx_test_files(self):
    some_cards = self.cfg.cart_test_file_some_cards()
    no_cards = self.cfg.cart_test_file_no_cards()
    sc_path = self.cfg.get_cartio_file(some_cards)
    nc_path = self.cfg.get_cartio_file(no_cards)
    print(f"testing path: {sc_path}")
    self.assertTrue(path.exists(sc_path))
    print(f"testing path: {nc_path}")
    self.assertTrue(path.exists(nc_path))

  def test_should_replace_constant_TEST_FOLDER(self):
    self.assertEqual(self.cfg.test_folder(), TEST_FOLDER)

  def test_should_replace_constant_CART_TEST_FILE_NO_CARDS(self):
    self.assertEqual(self.cfg.cart_test_file_no_cards(), CART_TEST_FILE_NO_CARDS)

  def test_should_replace_constant_CART_TEST_FILE_SOME_CARDS(self):
    self.assertEqual(self.cfg.cart_test_file_some_cards(), CART_TEST_FILE_SOME_CARDS)

  def test_should_replace_constant_OBSIDIAN_TEST_FOLDER(self):
    self.assertEqual(self.cfg.obsidian_test_folder(), OBSIDIAN_TEST_FOLDER)

  def test_should_replace_constant_OBSIDIAN_TEST_VAULT_ONE(self):
    self.assertEqual(self.cfg.obsidian_test_vault_one(), OBSIDIAN_TEST_VAULT_ONE)

  def test_should_replace_constant_OBSIDIAN_TEST_VAULT_TWO(self):
    self.assertEqual(self.cfg.obsidian_test_vault_two(), OBSIDIAN_TEST_VAULT_TWO)

  def test_should_replace_constant_BASIC_MYR_FILE_TEST_PATH(self):
    self.assertEqual(self.cfg.basic_myr_file_test_path(), BASIC_MYR_FILE_TEST_PATH)

  def test_should_replace_constant_DSV_TEST_FOLDER(self):
    self.assertEqual(self.cfg.dsv_test_folder(), DSV_TEST_FOLDER)

  def test_should_replace_constant_NONEXISTANT_FOLDER(self):
    self.assertEqual(self.cfg.nonexistant_folder(), NONEXISTANT_FOLDER)

  def test_should_replace_constant_EXISTANT_FILE(self):
    self.assertEqual(self.cfg.existant_file(), EXISTANT_FILE)

  def test_should_replace_constant_NONEXISTANT_FILE(self):
    self.assertEqual(self.cfg.nonexistant_file(), NONEXISTANT_FILE)

class TestNwdConfig(unittest.TestCase):
  def setUp(self):
    self.cfg = NwdConfig()
  
  def test_should_have_class(self):
    self.assertIsNotNone(self.cfg)

  def test_should_replace_constant_CARTOGRAPHER_FOLDER(self):
    self.assertEqual(self.cfg.cartio_folder(), CARTOGRAPHER_FOLDER)

  def test_should_replace_constant_CETS_FILE(self):
    self.assertEqual(self.cfg.cets_file(), CETS_FILE)