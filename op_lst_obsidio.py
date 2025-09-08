from menus import LineOption
from obsidio import ObsidIO

class ListObsidIOFilesOp(LineOption):
  def __init__(self, obsid: ObsidIO):
    self.obsid = obsid

  def key(self):
    return "lst"
  
  def desc(self):
    return "List ObsidIO Folders"
  
  def run(self):
    files = self.obsid.list_obsidio_files()
    file_count = len(files)
    if file_count < 1:
      print("no files found")
    else:
      print(f"found {file_count} files:")
      for file in files:
        print(file)