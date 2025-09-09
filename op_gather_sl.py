from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import LineOption
from myr_file import MyrFile
from files import get_lines_from

import os

class GatherSeedLinks(LineOption):
  def __init__(self, obio: ObsidIO):
    self.obio = obio

  def key(self):
    return "gthrsl"
  
  def desc(self):
    return f"Gather file filters for all links found in current files in obsidio working directory at: {self.obio.obsidio_folder()}"
  
  def run(self):

    directory_path = self.obio.obsidio_folder()

    msg = f"this will gather file filters for all links found in all files in: {directory_path}"
    msg += "/nAre you sure you want to proceed?(type 'y' for yes)"

    response = input(msg)

    if response.lower().strip() == 'y':

      print("gathering seedlinks from files...") 


      for filename in os.listdir(directory_path):
          file_path = os.path.join(directory_path, filename)
          if os.path.isfile(file_path):  # Check if it's a file, not a subdirectory
              print(f"File '{file_path}' found.")
              print("loading MyrFile")
              mf = MyrFile()
              mf.load_from_lines_arr(get_lines_from(file_path))
              wikilinks = mf.get_wikilinks()
              if len(wikilinks) > 0:
                for wikilink in mf.get_wikilinks():
                  print(f"Found wikilink: {wikilink}")
                  self.obio.file_filters.append(wikilink)
              else:
                print(f"no wikilinks found at: {file_path}")


      print("done gathering seedlinks from files.")
    else:
      print("Aborting gather operation, no seedlinks gathered.")

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  main = GatherSeedLinks(obio)
  main.run()