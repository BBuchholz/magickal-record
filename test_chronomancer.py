import unittest

from chronomancer import Chronomancer

class TestChronomancer(unittest.TestCase):
  def test_should_have_class(self):
    cm = Chronomancer()
    self.assertIsNotNone(cm)

  def test_should_get_sabbat_by_letter_code(self):
    cm = Chronomancer()
    sbt = cm.get_sabbat("LTH25")
    self.assertEqual("Litha 2025", str(sbt))