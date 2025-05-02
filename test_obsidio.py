import unittest
from obsidio import ObsidIO
from chronio import ChronIO
from cfg import NwdTestConfig
from os import path
from files import (
  get_path_in_folder,
  get_lines_from
)

class TestObsidIO(unittest.TestCase):
  def setUp(self):
    self.tcfg = NwdTestConfig()
    self.obio = ObsidIO(self.tcfg)
    self.chron = ChronIO()

  def test_should_have_class(self):
    self.assertIsNotNone(self.obio)

  def test_should_load_vaults(self):
    cfg_files = self.obio.get_cfg_files()
    self.assertTrue(len(cfg_files) > 0)
    md_file = cfg_files[0]
    self.obio.load_vaults(md_file)
    vault = self.obio.loaded_vault
    self.assertIsNotNone(vault)

  def test_should_get_cfg_files(self):
    cfg_files = self.obio.get_cfg_files()
    self.assertTrue(len(cfg_files) > 0)
    
  def test_cfg_test_files_should_be_in_test_folder(self):
    expected = "~/nwd/test/config/ConfigTestVault.md"
    expected = path.expanduser(expected)
    print(f"expecting path: {expected}")
    self.assertTrue(path.exists(expected))

  def test_create_vault_config(self):
    print("Generating vault folder")
    sfx = self.chron.get_suffix()
    o_flder = self.tcfg.obsidio_folder()
    fldr = "test_vault" + sfx
    folder_path = get_path_in_folder(o_flder, fldr)
    while path.exists(folder_path):
      sfx = self.chron.get_suffix(sfx)
      fldr = "test_vault" + sfx
      folder_path = get_path_in_folder(o_flder, fldr)
    print(f"generated folder {folder_path}")
    self.assertTrue(path.exists(folder_path))
    print(f"creating vault config for: {fldr}")
    self.obio.create_vault_config(fldr, folder_path)
    file_name = "Config" + fldr + ".md"
    file_path = self.tcfg.get_config_file(file_name)
    self.assertTrue(path.exists(file_path))
    lines = get_lines_from(file_path)
    self.assertIn(folder_path, lines[0])