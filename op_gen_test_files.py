from cfg import Config, NwdTestConfig
from menus import LineOption
from chronio import ChronIO
from obsidio import ObsidIO
from os import path
from files import get_path_in_folder

class GenerateTestFiles(LineOption):
  def __init__(
      self,
      cfg: Config,
      obio: ObsidIO, 
      chron: ChronIO
      ):
    self.cfg = cfg
    self.obio = obio
    self.chron = chron

  def key(self):
    return "gen"
  
  def desc(self):
    return "Generate Test Obsidio Files"
  
  def run(self):
    print("THIS OPTION HAS BEEN DEPRECATED")
    # print("Generating vault folder")
    # sfx = self.chron.get_suffix()
    # o_flder = self.cfg.obsidio_folder()
    # fldr = "test_vault" + sfx
    # folder_path = get_path_in_folder(o_flder, fldr)
    # while path.exists(folder_path):
    #   sfx = self.chron.get_suffix(sfx)
    #   fldr = "test_vault" + sfx
    #   folder_path = get_path_in_folder(o_flder, fldr)
    # print(f"generated folder {folder_path}")
    # print(f"creating vault config for: {fldr}")
    # self.obio.create_vault_config_file(fldr, folder_path)
    

  
