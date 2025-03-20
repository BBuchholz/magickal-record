from constants import TEST_FOLDER
from files import folder_exists

class MagickalRecord:
  def __init__(self, folder_path=None):
    if folder_path is not None:
      self.folder_path = folder_path
    else:
      self.folder_path = TEST_FOLDER

  def folder_exists(self):
    return folder_exists(self.folder_path)
