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
    self.assertEqual(len(mf.get_lines()), 2)
    
  def test_should_get_main_text_lines(self):
    # TODO: adapt from test_myr_file.py
    pass

  def check_for_link(self, expected_link: str, wikilinks: list):
    # TODO: adapt from test_myr_file.py
    pass

  def test_should_get_wikilinks(self):
    # TODO: adapt from test_myr_file.py
    pass

  def test_should_get_embedded_lines(self):
    mf = MyrFrag()
    lines = [
      "![[IMAGE_EXAMPLE.png]]",
      "with other lines that are not",
    ]
    mf.load_from_lines_arr(lines)
    image_lines = mf.get_embedded_lines()
    image_line_join = "\n".join(image_lines)
    expected_join = "![[IMAGE_EXAMPLE.png]]"
    self.assertEqual(image_line_join, expected_join)

  def test_should_get_comment_lines(self):
    mf = MyrFrag()
    lines = [
      "testing lines like this that ARE NOT comment lines",
      "- and lines like this that ARE comment lines",
    ]
    mf.load_from_lines_arr(lines)
    comment_lines = mf.get_comment_lines()
    expected_comments = [
      "- and lines like this that ARE comment lines",
    ]
    comments_join = "\n".join(comment_lines)
    expected_join = "\n".join(expected_comments)
    self.assertEqual(comments_join, expected_join)

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
    mf_one = MyrFrag()
    mf_one.load_from_lines_arr(lines_one)
    mf_two = MyrFrag()
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


