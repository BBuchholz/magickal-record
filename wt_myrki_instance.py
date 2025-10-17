from wxrd_type import WxrdType
from myr_file import MyrFile

class WxrdTypeMyrkiInstance(WxrdType):
  def matches(self, myr_file: MyrFile):
    return True