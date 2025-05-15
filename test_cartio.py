import unittest

from cartio import CartIO
from cfg import NwdTestConfig

class TestCartIO(unittest.TestCase):
  def setUp(self):
    self.tcfg = NwdTestConfig()

  def test_should_check_for_cartographer_folder(self):
    cg = CartIO(NwdTestConfig())
    self.assertTrue(cg.verify_folder())

  def test_should_look_for_cets_file(self):
    cg = CartIO(NwdTestConfig())
    self.assertTrue(cg.verify_cets_file())

  def test_should_get_release_names(self):
    cg = CartIO(NwdTestConfig())
    self.assertIn("LMS24A", cg.get_release_file_names())

  def test_should_get_cart_files(self):
    cg = CartIO(NwdTestConfig())
    self.assertIn(self.tcfg.cart_test_file_no_cards(), cg.get_cart_files())
    
  def test_should_get_release_name_from_line(self):
    cg = CartIO(NwdTestConfig())
    name = cg.get_release_file_name_from_line("- [ ] [[LMS24A]]")
    self.assertEqual(name, "LMS24A")

  def test_should_get_myrkis(self):
    cg = CartIO(NwdTestConfig())
    cg.select_file(self.tcfg.cart_test_file_some_cards())
    myrkis = cg.get_myrkis()
    self.assertIn("SERPENT", myrkis)

  def test_should_get_related_myrkis(self):
    cg = CartIO(NwdTestConfig())
    cg.select_file(self.tcfg.cart_test_file_some_cards())
    myrkis = cg.get_related_myrkis()
    self.assertIn("DIMENSION", myrkis)

  def test_should_get_unconnected_myrkis(self):
    cg = CartIO(NwdTestConfig())
    cg.select_file(self.tcfg.cart_test_file_some_cards())
    myrkis = cg.get_unconnected_myrkis()
    
    # NB: ALL MYRKIS SHOULD BE IN BOTH COLUMNS 
    # AT LEAST ONCE, so testing from both sides

    # test for "related myrki" not in "myrki" column
    self.assertIn("UNICORN", myrkis)
    
    # test for "myrki" not in "related myrkis" column
    self.assertIn("SERPENT", myrkis)

  def test_should_get_card(self):
    cg = CartIO(NwdTestConfig())
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

  def test_should_support_new_columns_in_current_cards(self):
    cg = CartIO(NwdTestConfig())
    cg.select_file(self.tcfg.cart_test_file_current_cards())
    apple_card = cg.get_card("APPLE")
    self.assertEqual(apple_card["Text Credit"], "Brent Buchholz")
    self.assertEqual(apple_card["Image Credit"], "Microsoft Copilot")
    self.assertEqual(apple_card["Myrki Credit"], "Brent Buchholz")


  def test_should_select_file(self):
    cg = CartIO(NwdTestConfig())
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

    