import unittest
from eg import EG
from cfg import NwdTestConfig

class TestEG(unittest.TestCase): 
  def setUp(self):
    tcfg = NwdTestConfig()
    self.eg = EG(tcfg)

  def test_should_have_coder_builder_vhale(self):
    v = self.eg.get_vhale("CodER BuildER")
    self.assertIsNotNone(v)

  def test_should_return_none_for_undefined_vhale_names(self):
    v = self.eg.get_vhale("DOESNOTEXIST")
    self.assertIsNone(v)

if __name__ == "__main__":
  unittest.main()