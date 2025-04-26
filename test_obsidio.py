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
    