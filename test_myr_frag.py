import unittest

from myr_frag import MyrFrag

class TestMyrFrag(unittest.TestCase):
  def test_should_load_from_lines_array(self):
    lines = [
      "some lines",
      "to test from"
    ]
    mf = MyrFrag()
    self.assertEqual(len(mf.get_lines()), 0)
    mf.load_from_lines_arr(lines)
    self.assertEqual(len(mf.get_lines()), 5)
    
# TODO: adapt all appropriate tests from test_myr_file.py