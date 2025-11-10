import re
import os
from myr_frag import MyrFrag

# Myriad Files are more than "mere files" :)
# the class name is a play on words
# much like MyrKis are more than "mere keys"
class MyrFile():
  def __init__(self):
    self.main_fragment = MyrFrag()

  def get_lines(self):
    return self.main_fragment.get_lines()

  def load_from_lines_arr(self, lines):
    self.main_fragment.load_from_lines_arr(lines)

  def load_from_string_path(self, str_path):
    self.file_name = os.path.basename(str_path)

  def get_main_text_lines(self):
    return self.main_fragment.get_main_text_lines()
  
  def get_comment_lines(self):
    return self.main_fragment.get_comment_lines()

  def get_wikilinks(self):
    return self.main_fragment.get_wikilinks()

  def get_embedded_lines(self, strip_embedding=False):
    return self.main_fragment.get_embedded_lines()