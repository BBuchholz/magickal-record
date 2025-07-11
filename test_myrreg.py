import unittest
from myrreg import MyrkiRegistry
from cfg import NwdTestConfig

class TestMyrkiRegistry(unittest.TestCase):
  def setUp(self):
    self.myrg = MyrkiRegistry(NwdTestConfig())

  def test_should_have_class(self):
    self.assertIsNotNone(self.myrg)

  def test_should_load(self):
    self.assertEqual(len(self.myrg.myrkis), 0)
    self.myrg.load()
    # test vault is vaultone and should have the following myrkis:
    # RF, TCTKL, SERPENT and STAR
    # other files are in there to make sure we are filtering
    self.assertEqual(len(self.myrg.myrkis), 4)
    # test vault is vaultone and should have the following: 
    # DRAGON(2), FIRE(2), LOREFUL(2), RF(4), TCTKL(16), ZAGREUS(4), SERPENT(2) and STAR(1)
    # other files are in there to make sure we are filtering
    self.assertEqual(len(self.myrg.myrki_instances), 33)

  def test_should_validate_myrki_instance(self):
    # load registry
    self.myrg.load()
    
    # VALID INSTANCES
    self.assertTrue(self.myrg.validate_myrki_instance("DRAGON-LMS25"))

    valid = "DRAGON-LTH25"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "FIRE-6265"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "FIRE-LMS25"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "LOREFUL-fe6f"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "LOREFUL-larval-e256"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "RF-0a91"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "TCTKL-0-6c4b"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "TCTKL-4b25"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "TCTKL-8-XXXX"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "TCTKL-ccf2"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "TCTKL-MATRIX-0fe4"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))

    valid = "ZAGREUS-da5f"
    self.assertTrue(self.myrg.validate_myrki_instance(valid))


    # INVALID INSTANCES
    self.assertFalse(self.myrg.validate_myrki_instance("RF-240818R1"))

    invalid = "RF-91d6 BGB Card"
    self.assertFalse(self.myrg.validate_myrki_instance(invalid))

    invalid = "RF-91d6 Canva"
    self.assertFalse(self.myrg.validate_myrki_instance(invalid))

    invalid = "RF-91d6 Components"
    self.assertFalse(self.myrg.validate_myrki_instance(invalid))

    invalid = "RF-91d6 Meta"
    self.assertFalse(self.myrg.validate_myrki_instance(invalid))

    invalid = "TCTKL-4b25 BGB Card"
    self.assertFalse(self.myrg.validate_myrki_instance(invalid))

    invalid = "TCTKL-4b25 Canva"
    self.assertFalse(self.myrg.validate_myrki_instance(invalid))

    invalid = "TCTKL-4b25 Components"
    self.assertFalse(self.myrg.validate_myrki_instance(invalid))

    invalid = "TCTKL-4b25 Meta"
    self.assertFalse(self.myrg.validate_myrki_instance(invalid))


