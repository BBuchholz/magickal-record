import os

class Crawler:
  def __init__(self, folder_path):
    self.folder_path = os.path.expanduser(folder_path)

  def get_subfolders(self, directory):
    """
    Returns a list of subfolders in the given directory.
    """
    # return [name for name in os.listdir(directory)
    #         if os.path.isdir(os.path.join(directory, name))]
    subfolders = []
    for name in os.listdir(directory):
      path = os.path.join(directory, name)
      if os.path.isdir(path):
        subfolders.append(path)
    return subfolders

  def get_adjacent_folders(self):
    adjacent_folders = []
    parent = os.path.dirname(self.folder_path)
    for path in self.get_subfolders(parent):
      if path is not self.folder_path:
        adjacent_folders.append(path)
    return adjacent_folders