import unittest
from cfg import NwdTestConfig
from myr_file import MyrFile
from constants_md import (
  LINES_STAR_LTH25,
  MAIN_TEXT_STAR_LTH25,
  COMMENT_ONE_STAR_LTH25,
  COMMENT_TWO_STAR_LTH25,
  IMAGE_EMBED_STAR_LTH25,
  LINES_APPLE_LTH25,
  MAIN_TEXT_APPLE_LTH25,
  COMMENT_ONE_APPLE_LTH25,
  COMMENT_TWO_APPLE_LTH25,
  IMAGE_EMBED_APPLE_LTH25,
)
from files import (
  get_lines_from,
)

class TestMyrFile(unittest.TestCase):
  def setUp(self):
    self.mf_star_lth25 = MyrFile()
    self.mf_star_lth25.load_from_lines_arr(LINES_STAR_LTH25)
    self.mf_apple_lth25 = MyrFile()
    self.mf_apple_lth25.load_from_lines_arr(LINES_APPLE_LTH25)

  def test_should_load_from_lines_array(self):
    tcfg = NwdTestConfig()
    lines = get_lines_from(tcfg.basic_myr_file_test_path())
    mf = MyrFile()
    self.assertEqual(len(mf.get_lines()), 0)
    mf.load_from_lines_arr(lines)
    self.assertEqual(len(mf.get_lines()), 5)

  def test_should_get_main_text_lines(self):
    # STAR
    main_text_lines = self.mf_star_lth25.get_main_text_lines()
    main_text = "\n".join(main_text_lines)
    self.assertEqual(main_text, MAIN_TEXT_STAR_LTH25)

    # APPLE
    main_text_lines = self.mf_apple_lth25.get_main_text_lines()
    main_text = "\n".join(main_text_lines)
    self.assertEqual(main_text, MAIN_TEXT_APPLE_LTH25)

  def test_should_get_wikilinks(self):
    # TODO: STAR AND APPLE BOTH HAVE SOME, IMPLEMENT
    implemented = False
    self.assertTrue(implemented)

  def test_should_get_embedded_lines(self):
    # STAR
    image_embeds = self.mf_star_lth25.get_embedded_lines()
    images = "\n".join(image_embeds)
    self.assertEqual(images, IMAGE_EMBED_STAR_LTH25)
    
    # APPLE
    image_embeds = self.mf_apple_lth25.get_embedded_lines()
    images = "\n".join(image_embeds)
    self.assertEqual(images, IMAGE_EMBED_APPLE_LTH25)

  def test_should_get_comment_lines(self):
    # STAR
    comment_lines = self.mf_star_lth25.get_comment_lines()
    expected_comments = [
      COMMENT_ONE_STAR_LTH25,
      COMMENT_TWO_STAR_LTH25,
    ]
    comments_join = "\n".join(comment_lines)
    expected_join = "\n".join(expected_comments)
    self.assertEqual(comments_join, expected_join)

    # APPLE
    comment_lines = self.mf_apple_lth25.get_comment_lines()
    expected_comments = [
      COMMENT_ONE_APPLE_LTH25,
      COMMENT_TWO_APPLE_LTH25,
    ]
    comments_join = "\n".join(comment_lines)
    expected_join = "\n".join(expected_comments)
    self.assertEqual(comments_join, expected_join)

  def test_file_should_loaded_same_either_way(self):
    # The goal is to test that a file loaded 
    # from a file system .md file is identical 
    # to one loaded from a lines array with the 
    # same values so we can build our test suite 
    # around hard coded lines arrays but ultimately 
    # trust that files loaded from the file system 
    # will behave uniformly, as our support for 
    # various file features becomes more complicated 
    # we can add additional test cases to this test 
    # to verify that this always remains true
    #
    # FOR NOW, just using two examples of
    # existing files in the ecosystem and hard coding
    # a version of them manually to start this test
    # pattern
    tcfg = NwdTestConfig()
    mf_from_file_system = MyrFile()
    
    # STAR
    lines = get_lines_from(tcfg.file_path_star_lth25_md())
    mf_from_file_system.load_from_lines_arr(lines)

    self.assertEqual(len(lines), len(LINES_STAR_LTH25))
    self.assertEqual(lines, LINES_STAR_LTH25)
    self.assertEqual(self.mf_star_lth25, mf_from_file_system)
    
    # APPLE
    lines = get_lines_from(tcfg.file_path_apple_lth25_md())
    mf_from_file_system.load_from_lines_arr(lines)

    self.assertEqual(len(lines), len(LINES_APPLE_LTH25))
    self.assertEqual(lines, LINES_APPLE_LTH25)
    self.assertEqual(self.mf_apple_lth25, mf_from_file_system)
    

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
