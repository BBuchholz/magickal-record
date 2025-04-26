import os

class Config():
  def __init__(self):
    self._nwd_folder = os.path.expanduser("~/nwd")
    self._config_folder = "~/obsidianConfig"
    self._cartio_folder = "~/nwd/cartographer"
    self._cets_file = "~/nwd/cartographer/Cets.md"

  @property
  def nwd_folder(self):
    return self._nwd_folder

  @property
  def config_folder(self):
    return self._config_folder
  
  @property
  def cartio_folder(self):
    return self._cartio_folder

  @property
  def cets_file(self):
    return self._cets_file

class TestingConfig():
  def __init__(self):
    self._nwd_folder = os.path.expanduser("~/nwd/test")
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

  @property
  def nwd_folder(self):
    return self._nwd_folder
  
  @property
  def test_vault_config_file(self):
    folder = os.path.expanduser(self.nwd_folder)
    fname = "test_vault_config.md"
    file_path = os.path.join(folder, fname)
    return file_path