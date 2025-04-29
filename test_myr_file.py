import unittest
from cfg import NwdTestConfig
from myr_file import MyrFile
from files import (
  get_lines_from,
)

class TestMyrFile(unittest.TestCase):
  def test_should_load_from_lines_array(self):
    tcfg = NwdTestConfig()
    lines = get_lines_from(tcfg.basic_myr_file_test_path())
    mf = MyrFile()
    self.assertEqual(len(mf.get_lines()), 0)
    mf.load_from_lines_arr(lines)
    self.assertEqual(len(mf.get_lines()), 5)

  def test_should_be_equal_if_lines_are_equal(self):
    lines_one = [
      "line 1",
      "",
      "line 3",
      "",
      "line 5"
    ]
    lines_two = [
      "line 1",
      "",
      "line 3",
      "",
      "line 5"
    ]
    mf_one = MyrFile()
    mf_one.load_from_lines_arr(lines_one)
    mf_two = MyrFile()
    mf_two.load_from_lines_arr(lines_two)
    # should be equal
    self.assertEqual(mf_one, mf_two)
    # change lines and test again
    lines_three = [
      "line 1"
    ]
    mf_two.load_from_lines_arr(lines_three)
    # should not be equal anymore
    self.assertNotEqual(mf_one, mf_two)
