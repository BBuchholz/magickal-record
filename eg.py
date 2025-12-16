from cfg import Config
from myr_file import MyrFile
from files import path_exists

class EG:
  def __init__(self, cfg: Config):
    self.cfg = cfg

  def get_vhale_fname(self, vname):
    return "Vhale - " + vname + ".md"

  def get_vhale(self, vname) -> MyrFile:
    vfname = self.get_vhale_fname(vname)
    vpath = self.cfg.get_eg_file_path(vfname)
    if path_exists(vpath):
      mf = MyrFile()
      mf.load_from_string_path(vpath)
      return mf
    else:
      return None