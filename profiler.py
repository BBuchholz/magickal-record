from wxrd_type import WxrdType
from myr_file import MyrFile

class Profiler:
  def __init__(self):
    self.wxrd_types = []
    self.initialize_wxrd_types()

  def initialize_wxrd_types(self):
    mf = MyrFile()
    self.wxrd_types.append(mf.get_wxrd_type())

  def profile(self, string_path) -> list[WxrdType]:
    wxrd_types = []
    mf = MyrFile()
    mf.load_from_string_path(string_path)
    for some_wt in self.wxrd_types:
      if some_wt.trues_with(mf):
        wxrd_types.append(some_wt)
    return wxrd_types