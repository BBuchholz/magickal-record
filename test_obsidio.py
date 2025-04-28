import unittest
from obsidio import ObsidIO
from cfg import TestingConfig

class TestObsidIO(unittest.TestCase):
  def setUp(self):
    self.tcfg = TestingConfig()
    self.obio = ObsidIO(self.tcfg)

  def test_should_have_class(self):
    self.assertIsNotNone(self.obio)

  def test_should_load_vaults(self):
    fpath = self.tcfg.test_vault_config_file
    vaults = self.obio.load_vaults(fpath)
    self.assertEqual(len(vaults), 1)

  def test_should_get_cfg_files(self):
    cfg_files = self.obio.get_cfg_files()
    self.assertTrue(len(cfg_files) > 0)
    