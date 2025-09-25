import unittest
from profiler import Profiler
from profile_examples import ProfileExample
from myr_file import MyrFile

class TestProfiler(unittest.TestCase):
  def test_should_profile_md_file(self):
    prof = Profiler()
    exams = ProfileExample()
    md_file = exams.example_md_file()
    result = prof.profile(md_file)
    self.assertIn("MyrFile", result)

  def test_should_profile_folder(self):
    prof = Profiler()
    exams = ProfileExample()
    fldr = exams.example_folder()
    result = prof.profile(fldr)
    self.assertIn("Folder", result)
    self.assertNotIn("MyrFile", result)