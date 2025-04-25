import os

class Config():
  def __init__(self):
    self.nwd_folder = os.path.expanduser("~/nwd")
    self.CONFIG_FOLDER = ""
    self.CARTOGRAPHER_FOLDER = ""
    self.CETS_FILE = ""

class TestingConfig():
  def __init__(self):
    self.nwd_folder = os.path.expanduser("~/nwd/test")
    self.TEST_FOLDER = ""
    self.CART_TEST_FILE_NO_CARDS = ""
    self.CART_TEST_FILE_SOME_CARDS = ""
    self.OBSIDIAN_TEST_FOLDER = ""
    self.OBSIDIAN_TEST_VAULT_ONE = ""
    self.OBSIDIAN_TEST_VAULT_TWO = ""
    self.BASIC_MYR_FILE_TEST_PATH = ""
    self.DSV_TEST_FOLDER = ""
    self.NONEXISTANT_FOLDER = ""
    self.EXISTANT_FILE = ""
    self.NONEXISTANT_FILE = ""