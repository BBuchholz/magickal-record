from wxrd import Wxrd
from wxrd_type import WxrdType

class WxrdTypeFolder(WxrdType):
  def name(self):
    return "Folder"

class FolderWxrd(Wxrd):
  def get_wxrd_type(self) -> WxrdType:
    wtf = WxrdTypeFolder()
    return wtf