from menus import LineOption
from crsl_crtr import CarouselCreator
from myrreg import MyrkiRegistry

class CarouselMyrkiInstancesOp(LineOption):
  def __init__(self, crtr: CarouselCreator):
    self.crtr = crtr

  def key(self):
    return "mis"
  
  def desc(self):
    return "List Carousel Myrki Instance Candidates"
  
  def run(self):
    myrreg = MyrkiRegistry(self.crtr.cfg)
    print("loading myrki registry (myrreg)")
    myrreg.load(False)
    print("myrreg loaded")
    mis = myrreg.myrki_instances
    mis_count = len(mis)
    print(f"found {mis_count} myrki instances")
    for mi in mis:
      print(mi)