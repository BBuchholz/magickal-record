from cfg import Config
from cartreg import CartRegistry
from myrreg import MyrkiRegistry
from myr_file import MyrFile

class CarouselCreator:
  def __init__(self, cfg: Config):
    self.cfg = cfg
    self.cartreg = None
    self.myrreg = None

  def get_input_files(self):
    m_inpt_fldr = self.cfg.mdio_inbox_folder()
    print(f"checking folder : {m_inpt_fldr} for CRSL files")
    files = []
    return files
  
  def load_registries(self):
    self.myrreg = MyrkiRegistry(self.cfg)
    self.myrreg.load()
    self.cartreg = self.myrreg.cartrg

  def create_myrki_file(self, myrki_string):
    mf = MyrFile()
    if self.myrreg.contains_myrki(myrki_string):
      carts = self.cartreg.get_carts_for_myrki(myrki_string)
      if len(carts) > 0:
        lines = []
        for cart in carts:
          print(f"found cart: {cart}")
          card_id = cart["Card Id"]
          wikilink = f"[[{card_id}]]"
          lines.append(wikilink)
        mf.load_from_lines_arr(lines)
    return mf