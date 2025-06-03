# import os
from cfg import Config

class MDIO():
  def __init__(self, cfg: Config):
    self.cfg = cfg

  ### Removing: Does Not Belong Here
  # def ensure_folder(self, folder_path):
  #   folder_path = os.path.expanduser(folder_path)
  #   os.makedirs(folder_path, exist_ok=True)

  