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
    self._test_folder = "~/nwd/test"
    self._cart_test_file_no_cards = "TEST_DONOTMODIFY_NoCards.xlsx"
    self._cart_test_file_some_cards = "TEST_DONOTMODIFY_SomeCards.xlsx"
    self._obsidian_test_folder = "~/obsidianTestFolder"
    self._obsidian_test_vault_one = "~/obsidianTestFolder/testVaultOne"
    self._obsidian_test_vault_two = "~/obsidianTestFolder/testVaultTwo"
    self._basic_myr_file_test_path = "~/nwd/test/BasicMyrFile.md"
    self._dsv_test_folder = "~/nwd/test-dsv"
    self._nonexistant_folder = "~/doesNotExist"
    self._existant_file = "BasicFile.md"
    self._nonexistant_file = "THISFILEDOESNOTEXIST.md"

  @property
  def nwd_folder(self):
    return self._nwd_folder

  @property
  def test_folder(self):
    return self._test_folder

  @property
  def cart_test_file_no_cards(self):
    return self._cart_test_file_no_cards

  @property
  def cart_test_file_some_cards(self):
    return self._cart_test_file_some_cards

  @property
  def obsidian_test_folder(self):
    return self._obsidian_test_folder

  @property
  def obsidian_test_vault_one(self):
    return self._obsidian_test_vault_one

  @property
  def obsidian_test_vault_two(self):
    return self._obsidian_test_vault_two

  @property
  def basic_myr_file_test_path(self):
    return self._basic_myr_file_test_path

  @property
  def dsv_test_folder(self):
    return self._dsv_test_folder

  @property
  def nonexistant_folder(self):
    return self._nonexistant_folder
  
  @property
  def existant_file(self):
    return self._existant_file

  @property
  def nonexistant_file(self):
    return self._nonexistant_file
  
  @property
  def test_vault_config_file(self):
    folder = os.path.expanduser(self.nwd_folder)
    fname = "test_vault_config.md"
    file_path = os.path.join(folder, fname)
    return file_path