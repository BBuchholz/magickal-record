import os

class MDIO():
  def __init__(self):
    pass

  def ensure_folder(self, folder_path):
    folder_path = os.path.expanduser(folder_path)
    os.makedirs(folder_path, exist_ok=True)