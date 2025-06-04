from cfg import Config

class CarouselCreator:
  def __init__(self, cfg: Config):
    self.cfg = cfg

  def get_input_files(self):
    m_inpt_fldr = self.cfg.mdio_input_folder()
    print(f"checking folder : {m_inpt_fldr} for CRSL files")
    files = []
    return files