import os
from abc import ABC, abstractmethod

class Config(ABC):
  @abstractmethod
  def nwd_folder(self, expand_user=True):
    pass

  @abstractmethod
  def status(self):
    pass

  def get_obsidio_file(self, md_file):
    o_fldr = self.obsidio_folder()
    return os.path.join(o_fldr, md_file)
  
  def get_eg_file_path(self, md_fname):
    eg_fldr = self.eg_folder(True)
    return os.path.join(eg_fldr, md_fname)

  def eg_folder(self, expand_user=True):
    nwd_fldr = self.nwd_folder(expand_user)
    return os.path.join(nwd_fldr, "eg")
  
  def obsidio_folder(self, expand_user=True):
    nwd_fldr = self.nwd_folder(expand_user)
    return os.path.join(nwd_fldr, "obsidio")
  
  def get_cartio_file(self, md_file):
    c_fldr = self.cartio_folder()
    return os.path.join(c_fldr, md_file)

  def cartio_folder(self):
    nwd_fldr = self.nwd_folder()
    return os.path.join(nwd_fldr, "cartographer")
  
  def cets_folder(self, expand_user=True):
    nwd_fldr = self.nwd_folder(expand_user)
    return os.path.join(nwd_fldr, "cets")
  
  def sqlite_folder(self):
    nwd_fldr = self.nwd_folder()
    return os.path.join(nwd_fldr, "sqlite")
  
  def mdio_inbox_folder(self, expand_user=True):
    nwd_fldr = self.nwd_folder(expand_user)
    return os.path.join(nwd_fldr, "mdio/inbox")

  def audit_summary_file(self):
    c_flder = self.cartio_folder()
    return os.path.join(c_flder, "audit_file.md")
  
  def gardiner_report_file(self):
    c_flder = self.config_folder()
    return os.path.join(c_flder, "GarDinEr_RepOrT.md")
  
  def eg_ufu_md_file(self):
    eg_flder = self.eg_folder()
    return os.path.join(eg_flder, "UFU - EG.md")
  
  def verified_cart_file(self, expand_user=True):
    c_flder = self.config_folder(expand_user)
    return os.path.join(c_flder, "verified_cart_file.md")  

  def verified_vault_file(self, expand_user=True):
    c_flder = self.config_folder(expand_user)
    return os.path.join(c_flder, "verified_vault_file.md")
  
  def audit_linkages_file(self):
    o_fldr = self.obsidio_folder()
    return os.path.join(o_fldr, "audit_linkages_file.md")
  
  def myrkis_audit_file(self):
    o_fldr = self.obsidio_folder()
    return os.path.join(o_fldr, "myrkis_audit_file.md")

  def get_config_file(self, md_file):
    c_fldr = self.config_folder()
    return os.path.join(c_fldr, md_file)
  
  def config_folder(self, expand_user=True):
    nwd_fldr = self.nwd_folder(expand_user)
    return os.path.join(nwd_fldr, "config")
  
  def cets_file(self):
    c_flder = self.cartio_folder()
    return os.path.join(c_flder, "Cets.md")

class NwdConfig(Config):
  def __init__(self):
    # self._nwd_folder = os.path.expanduser("~/nwd")
    self._nwd_folder = "~/nwd"
    self._cartio_folder = "~/nwd/cartographer"
    # self._cets_file = "~/nwd/cartographer/Cets.md"

  def nwd_folder(self, expand_user=True):
    if expand_user:
      return os.path.expanduser(self._nwd_folder)
    else:
      return self._nwd_folder
  
  def status(self):
    return "NWD MODE"
  
  def cartio_folder(self):
    return self._cartio_folder


class NwdTestConfig(Config):
  def __init__(self):
    # self._nwd_folder = os.path.expanduser("~/nwd/test")
    self._nwd_folder = "~/nwd/test"
    self._test_folder = "~/nwd/test"
    self._cart_test_file_no_cards = "TEST_DONOTMODIFY_NoCards.xlsx"
    # self._cart_test_file_some_cards = "TEST_DONOTMODIFY_SomeCards.xlsx"
    self._obsidian_test_folder = "~/obsidianTestFolder"
    self._obsidian_test_vault_one = "~/obsidianTestFolder/testVaultOne"
    self._obsidian_test_vault_two = "~/obsidianTestFolder/testVaultTwo"
    self._basic_myr_file_test_path = "~/nwd/test/BasicMyrFile.md"
    self._dsv_test_folder = "~/nwd/test-dsv"
    self._nonexistant_folder = "~/doesNotExist"
    self._existant_file = "BasicFile.md"
    self._nonexistant_file = "THISFILEDOESNOTEXIST.md"

  def nwd_folder(self, expand_user=True):
    if expand_user:
      return os.path.expanduser(self._nwd_folder)
    else:
      return self._nwd_folder


  def folder_cets_lms24(self, expand_user=True):
    cets_fldr = self.cets_folder(expand_user)
    return os.path.join(cets_fldr, "LMS24")

  def status(self):
    return "TEST MODE"
  
  def file_path_star_lth25_md(self):
    t_flder = self.test_folder()
    return os.path.join(t_flder, "STAR-LTH25.md")

  def file_path_apple_lth25_md(self):
    t_flder = self.test_folder()
    return os.path.join(t_flder, "APPLE-LTH25.md")

  def test_folder(self):
    return self._test_folder

  def cart_test_file_no_cards(self):
    return self._cart_test_file_no_cards

  def cart_test_file_some_cards(self):
    # return self._cart_test_file_some_cards
    return "TEST_DONOTMODIFY_SomeCards.xlsx"
  
  def cart_test_file_current_cards(self):
    return "TEST - Current Cards - 20250515.xlsx"

  def obsidian_test_folder(self):
    return self._obsidian_test_folder

  def obsidian_test_vault_one(self):
    return self._obsidian_test_vault_one

  def obsidian_test_vault_two(self):
    return self._obsidian_test_vault_two

  def basic_myr_file_test_path(self):
    return self._basic_myr_file_test_path

  def dsv_test_folder(self):
    return self._dsv_test_folder

  def nonexistant_folder(self):
    return self._nonexistant_folder
  
  def existant_file(self):
    return self._existant_file

  def nonexistant_file(self):
    return self._nonexistant_file
  
  def test_vault_config_file(self):
    folder = os.path.expanduser(self.config_folder())
    fname = "ConfigTestVault.md"
    file_path = os.path.join(folder, fname)
    return file_path
  
  def test_vault_files(self):
    files = []
    files.append("Test One.md")
    files.append("Test Two.md")
    return files
  
  