import unittest

from cartio import CartIO
from cfg import NwdTestConfig

class TestCartIO(unittest.TestCase):
  def setUp(self):
    self.tcfg = NwdTestConfig()

  def test_should_enshrine_AWLWA_carteography(self):
    # TODO: from Grey Iron Prison days, chart by speaker
    # should implement all those tables and enshrine
    # their reproduction in various formats
    # (YES, this is an open ended goal, mod this test 
    # and create others as we proceed, 
    # storing a flash of insight for later)
    # TODO: also: include this particular task 
    # somewhere in the Pomodoro Roll (where apropos)
    is_implemented = False
    self.assertTrue(is_implemented)

  def test_should_respect_AWLWA_tree(self):
    # TODO: 3D == [2,1]; 3ID == [2,1]
    is_implemented = False
    self.assertTrue(is_implemented)

  def test_should_respect_AWLWA_valknut(self):
    # TODO: make these true

    # 9D == [
    #         [8,1],
    #         [2,7],
    #         [6,3],
    #         [4,5],
    #       ]

    # 9ID == [
    #         [4,5],
    #         [6,3],
    #         [2,7],
    #         [8,1],
    #       ]
    is_implemented = False
    self.assertTrue(is_implemented)

  def test_should_translate_AWLWA_terminology(self):
    # TODO: make these true, should translate both ways
    # 3D == "Tree Delta",
    # 3ID == "Tree Inverse Delta", 
    # 9D == "Nigh Delta", 
    # 9ID == "Nigh Inverse Delta" 
    is_implemented = False
    self.assertTrue(is_implemented)
    

  def test_should_check_for_cartographer_folder(self):
    cg = CartIO()
    self.assertTrue(cg.verify_folder())

  def test_should_look_for_cets_file(self):
    cg = CartIO()
    self.assertTrue(cg.verify_cets_file())

  def test_should_get_release_names(self):
    cg = CartIO()
    self.assertIn("LMS24A", cg.get_release_file_names())

  def test_should_get_cart_files(self):
    cg = CartIO()
    self.assertIn(self.tcfg.cart_test_file_no_cards(), cg.get_cart_files())
    
  def test_should_get_release_name_from_line(self):
    cg = CartIO()
    name = cg.get_release_file_name_from_line("- [ ] [[LMS24A]]")
    self.assertEqual(name, "LMS24A")

  def test_should_get_myrkis(self):
    cg = CartIO()
    cg.select_file(self.tcfg.cart_test_file_some_cards())
    myrkis = cg.get_myrkis()
    self.assertIn("SERPENT", myrkis)

  def test_should_get_related_myrkis(self):
    cg = CartIO()
    cg.select_file(self.tcfg.cart_test_file_some_cards())
    myrkis = cg.get_related_myrkis()
    self.assertIn("DIMENSION", myrkis)

  def test_should_get_unconnected_myrkis(self):
    cg = CartIO()
    cg.select_file(self.tcfg.cart_test_file_some_cards())
    myrkis = cg.get_unconnected_myrkis()
    
    # NB: ALL MYRKIS SHOULD BE IN BOTH COLUMNS 
    # AT LEAST ONCE, so testing from both sides

    # test for "related myrki" not in "myrki" column
    self.assertIn("UNICORN", myrkis)
    
    # test for "myrki" not in "related myrkis" column
    self.assertIn("SERPENT", myrkis)

  def test_should_get_card(self):
    cg = CartIO()
    cg.select_file(self.tcfg.cart_test_file_some_cards())
    star_card = cg.get_card("STAR")

    star_card_values = {
      "MYRKI" : "STAR",
      "Card Text" : "tha SILVER STAR inTha MIRROR ovTha DEPTHS",
      "Related MYRKIS" : "SILVER, MIRROR, DEPTH",
      "Card Id": "",
      "Canva Link": ""
    }


    self.assertEqual(star_card, star_card_values)

  def test_should_select_file(self):
    cg = CartIO()
    # lists should be empty
    self.assertEqual(len(cg.get_myrkis()), 0)
    self.assertEqual(len(cg.get_related_myrkis()), 0)

    # file should load here
    cg.select_file(self.tcfg.cart_test_file_some_cards())

    # lists should be populated
    self.assertNotEqual(len(cg.get_myrkis()), 0)
    self.assertNotEqual(len(cg.get_related_myrkis()), 0)

    # should have cards loaded to dict keyed to myrki
    star_card = cg.get_card("STAR")
    self.assertEqual(star_card["MYRKI"], "STAR")
