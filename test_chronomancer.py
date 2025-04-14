import unittest

from chronomancer import Chronomancer

class TestChronomancer(unittest.TestCase):
  def test_should_have_class(self):
    cm = Chronomancer()
    self.assertIsNotNone(cm)