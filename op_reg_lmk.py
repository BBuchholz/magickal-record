from menus import LineOption
from myrreg import MyrkiRegistry

class ListMyrKisOp(LineOption):
  def __init__(self, myrreg: MyrkiRegistry):
    self.myrreg = myrreg

  def key(self):
    return "lmk"
  
  def desc(self):
    return "List Myrkis"
  
  def run(self):
    print(f"Myrkis({len(self.myrreg.myrkis)}): ")
    for myrki in self.myrreg.myrkis:
      print("Myrki: ")
      print(myrki)
    