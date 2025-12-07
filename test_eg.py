import unittest
from eg import EG

class TestEG(unittest.TestCase): 
  def setUp(self):
    self.eg = EG()

  def test_should_have_coder_builder_vhale(self):
    v = self.eg.get_vhale("CodER BuildER")
    self.assertIsNotNone(v)

  def test_should_return_none_for_undefined_vhale_names(self):
    v = self.get.get_vhale("DOESNOTEXIST")
    self.assertIsNone(v)

if __name__ == "__main__":
  unittest.main()