import unittest
from obsidio import ObsidIO
from cfg import NwdTestConfig

class TestObsidIO(unittest.TestCase):
  def setUp(self):
    self.tcfg = NwdTestConfig()
    self.obio = ObsidIO(self.tcfg)

  def test_should_have_class(self):
    self.assertIsNotNone(self.obio)

  def test_should_load_vaults(self):
    md_file = self.obio.get_cfg_files()[0]
    self.obio.load_vaults(md_file)
    vault_count = len(self.obio.loaded_vaults)
    self.assertEqual(vault_count, 1)

  def test_should_get_cfg_files(self):
    cfg_files = self.obio.get_cfg_files()
    self.assertTrue(len(cfg_files) > 0)
    