from myr_file import MyrFile # can't do this, circular import

class WxrdType:
  def __init__(self, type_name="Wxrd"):
    self.wxrd_type_name = type_name

  def __str__(self):
    return self.wxrd_type_name

  def name(self) -> str:
    return self.wxrd_type_name
  
  def is_true(self, wt):
    return True
  
  def matches(self, myr_file: MyrFile):
    return True
