from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import LineOption

import os

class ClearWorkingDirectoryOp(LineOption):
  def __init__(self, obio: ObsidIO):
    self.obio = obio

  def key(self):
    return "clrwd"
  
  def desc(self):
    return f"Clear current files in obsidio working directory at: {self.obio.obsidio_folder()}"
  
  def run(self):

    directory_path = self.obio.obsidio_folder()

    msg = f"this will delete all files in: {directory_path}"
    msg += "/nAre you sure you want to proceed?(type 'y' for yes)"

    response = input(msg)

    if response.lower().strip() == 'y':

      print("clearing files...") 


      for filename in os.listdir(directory_path):
          file_path = os.path.join(directory_path, filename)
          if os.path.isfile(file_path):  # Check if it's a file, not a subdirectory
              os.remove(file_path)
              print(f"File '{file_path}' deleted successfully.")


      print("done clearing files.")
    else:
      print("Aborting clear operation, no files removed.")

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  main = ClearWorkingDirectoryOp(obio)
  main.run()