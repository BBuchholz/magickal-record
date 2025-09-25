from wxrd_type import WxrdType
from wxrd import Wxrd
from myr_file import MyrFile
from folder_wxrd import FolderWxrd

class Profiler:
  def __init__(self):
    self.wxrd_types: list[WxrdType] = []
    self.initialize_wxrd_types()

  def initialize_wxrd_types(self):
    wrd = Wxrd()
    self.wxrd_types.append(wrd.get_wxrd_type())
    mf = MyrFile()
    self.wxrd_types.append(mf.get_wxrd_type())
    fldr = FolderWxrd()
    self.wxrd_types.append(fldr.get_wxrd_type())
    
  def profile(self, string_path) -> list[str]:
    wxrd_types = []
    mf = MyrFile()
    mf.load_from_string_path(string_path)
    for some_wt in self.wxrd_types:
      if some_wt.is_true(mf):
        wxrd_types.append(some_wt.name())
    return wxrd_types