from wxrd_type import WxrdType
from myr_file import MyrFile

class WxrdTypeMyrkiInstance(WxrdType):
  def __init__(self):
    super().__init__("MyrkiInstance")

  def matches(self, myr_file: MyrFile):
    name = myr_file.file_name
    if " " in name:
      return False
    elif "-" in name:
      return True
    else:
      return False