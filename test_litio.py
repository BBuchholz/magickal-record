import unittest
from litio import LitIO
from myr_file import MyrFile

class TestLitIO(unittest.TestCase):
  def setUp(self):
    self.lio = LitIO()
    
  def test_should_have_class(self):
    self.assertIsNotNone(self.lio)

  def test_should_get_source_links_from_myr_files(self):
    mf1 = MyrFile()
    lines1 = [
      "Source: [[Some Book]]",
      "",
      "Some quote from some book",
      "",
      "Some commentatry on some quote from some book"
    ]
    mf1.load_from_lines_arr(lines1)
    self.lio.add_myr_file(mf1)
    mf2 = MyrFile()
    lines2 = [
      "Source: Another Book Title Without A Link",
      "",
      "Some quote from Another Book Title Without A Link",
      "",
      "Some commentatry on some quote from Another Book Title Without A Link"
    ]
    mf2.load_from_lines_arr(lines2)
    self.lio.add_myr_file(mf2)
    sources = self.lio.get_source_values()
    self.assertEqual(len(sources), 2)
    self.assertEqual(sources[0], "[[Some Book]]")
    self.assertEqual(sources[1], "Another Book Title Without A Link")
