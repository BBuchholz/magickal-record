from crsl_crtr import CarouselCreator
from menus import SubMenu
from cfg import Config, NwdTestConfig
from op_lst_crsl import ListMyrCarouselFilesOp
from op_crsl_mis import CarouselMyrkiInstancesOp

class MyrCarouselMenu(SubMenu):
  def __init__(self, cfg: Config):
    print(f"loading MyrCarousel configuration: {cfg.status}")
    self.crtr = CarouselCreator(cfg)

  def key(self):
    return "crsl"
  
  def desc(self):
    return "MyrCarousel Creator"
  
  def get_ops(self):
    ops = []
    ops.append(ListMyrCarouselFilesOp(self.crtr))
    ops.append(CarouselMyrkiInstancesOp(self.crtr))
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  main = MyrCarouselMenu(tcfg)
  main.show_menu()