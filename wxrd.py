from wxrd_type import WxrdType

class WxrdTypeWxrd(WxrdType):
  pass

class Wxrd:
  def get_wxrd_type(self) -> WxrdType:
    wtw = WxrdTypeWxrd()
    return wtw