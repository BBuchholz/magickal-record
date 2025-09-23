class WxrdType:
  def __init__(self):
    self.wxrd_type_name = "Wxrd" # default

  def name(self) -> str:
    return self.wxrd_type_name
  
  def trues_with(self, wt):
    return True