import unittest

from myr_file import MyrFile
from constants import (
  BASIC_MYR_FILE_TEST_PATH,
)
from files import (
  get_lines_from,
)

class TestMyrFile(unittest.TestCase):
  def test_should_load_from_lines_array(self):
    lines = get_lines_from(BASIC_MYR_FILE_TEST_PATH)
    mf = MyrFile()
    self.assertEqual(len(mf.get_lines()), 0)
    mf.load_from_lines_arr(lines)
    self.assertEqual(len(mf.get_lines()), 5)
