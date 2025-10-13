from wxrd_type import WxrdType
from wxrd import Wxrd
from myr_file import MyrFile
from folder_wxrd import FolderWxrd
import os

class Profiler:
  def __init__(self):
    self.wxrd_types: list[WxrdType] = []
    self.file_types = []
    self.folder_types = []
    self.initialize_wxrd_types()

  def initialize_wxrd_types(self):
    wrd = Wxrd()
    self.file_types.append(wrd.get_wxrd_type())
    mf = MyrFile()
    self.file_types.append(mf.get_wxrd_type())
    fldr = FolderWxrd()
    self.folder_types.append(fldr.get_wxrd_type())
    
  def profile(self, string_path) -> list[str]:
    wxrd_types = []
    string_path = os.path.expanduser(string_path)
    print(f"profiling path: {string_path}")
    if os.path.isdir(string_path):
      for some_folder_type in self.folder_types:
        if some_folder_type.matches(string_path):
          wxrd_types.append(some_folder_type.name())
    else:
      print(f"path is not a directory")
    if os.path.isfile(string_path):
      mf = MyrFile()
      mf.load_from_string_path(string_path)
      count = len(self.file_types)
      print(f"testing {count} file types against path {string_path}")
      for some_file_type in self.file_types:
        print(f"testing file type: {some_file_type}")
        if some_file_type.matches(mf):
          print(f"{mf.file_name} is type {some_file_type}")
          wxrd_types.append(some_file_type.name())
        else:
          print(f"{mf.file_name} is not type {some_file_type}")
    else:
      print(f"path is not a file")
    return wxrd_types
  

  # def is_wxrd_type(self, wxrd: Wxrd, wt: WxrdType):
  #   # TODO: implement
  #   return True;