import unittest
from eg import EG
from cfg import NwdTestConfig
from myr_frag import MyrFrag

class TestEG(unittest.TestCase): 
  def setUp(self):
    tcfg = NwdTestConfig()
    self.eg = EG(tcfg)

  def test_should_have_coder_builder_vhale(self):
    v = self.eg.get_vhale("CodER BuildER")
    self.assertIsNotNone(v)

    # should have at least one repo link
    repo_section = v.get_section("Repository Hosts")
    self.assertIsInstance(repo_section, MyrFrag)
    self.assertEqual(1, len(repo_section.get_comment_lines()))
    
    # should have at least one language link
    lang_section = v.get_section("Languages")
    self.assertIsInstance(lang_section, MyrFrag)
    self.assertEqual(1, len(lang_section.get_comment_lines()))  


  def test_should_return_none_for_undefined_vhale_names(self):
    v = self.eg.get_vhale("DOESNOTEXIST")
    self.assertIsNone(v)

if __name__ == "__main__":
  unittest.main()