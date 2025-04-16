import unittest

from chronomancer import Chronomancer

class TestChronomancer(unittest.TestCase):
  def test_should_have_class(self):
    cm = Chronomancer()
    self.assertIsNotNone(cm)

  def test_should_get_sabbat_by_letter_code(self):
    cm = Chronomancer()

    # invalid codes should return None
    sbt = cm.get_sabbat("")
    self.assertIsNone(sbt)
    sbt = cm.get_sabbat("LTH")
    self.assertIsNone(sbt)
    sbt = cm.get_sabbat("2025")
    self.assertIsNone(sbt)
    sbt = cm.get_sabbat("Litha 2025")
    self.assertIsNone(sbt)
    sbt = cm.get_sabbat(None)
    self.assertIsNone(sbt)

    # valid codes below here
    sbt = cm.get_sabbat("BEL25")
    self.assertEqual("Beltane 2025", str(sbt))
    sbt = cm.get_sabbat("LTH25")
    self.assertEqual("Litha 2025", str(sbt))
    sbt = cm.get_sabbat("LMS25")
    self.assertEqual("Lammas 2025", str(sbt))
    sbt = cm.get_sabbat("MBN25")
    self.assertEqual("Mabon 2025", str(sbt))
    sbt = cm.get_sabbat("SMH25")
    self.assertEqual("Samhain 2025", str(sbt))
    sbt = cm.get_sabbat("YUL25")
    self.assertEqual("Yule 2025", str(sbt))
    sbt = cm.get_sabbat("IMB26")
    self.assertEqual("Imbolc 2026", str(sbt))
    sbt = cm.get_sabbat("OST26")
    self.assertEqual("Ostara 2026", str(sbt))
    sbt = cm.get_sabbat("BEL26")
    self.assertEqual("Beltane 2026", str(sbt))
    sbt = cm.get_sabbat("LTH26")
    self.assertEqual("Litha 2026", str(sbt))
    sbt = cm.get_sabbat("LMS26")
    self.assertEqual("Lammas 2026", str(sbt))
    sbt = cm.get_sabbat("MBN26")
    self.assertEqual("Mabon 2026", str(sbt))
    sbt = cm.get_sabbat("SMH26")
    self.assertEqual("Samhain 2026", str(sbt))
    sbt = cm.get_sabbat("YUL26")
    self.assertEqual("Yule 2026", str(sbt))