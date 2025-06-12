from menus import LineOption
from mdio import MDIO
from chronio import ChronIO
from files import (
  get_path_in_folder,
  path_exists,
  write_lines,
)

class SuggestionOp(LineOption):
  def __init__(self, mdio: MDIO):
    super().__init__()
    self.mdio = mdio
    self.chron = ChronIO()

  def key(self):
    return "sug"
  
  def desc(self):
    return "Add Suggestion"
  
  def run(self):
    sug = input("Suggestion? ")
    if len(sug.strip()) > 0:
      print(f"Saving suggestion to file system: {sug}")
      sfx = self.chron.get_suffix()
      f_name = "Suggestion - " + sfx + ".md"
      fldr_path = self.mdio.cfg.mdio_inbox_folder()
      file_path = get_path_in_folder(fldr_path, f_name)
      while path_exists(file_path):
        sfx = self.chron.get_suffix(sfx)
        f_name = "Suggestion - " + sfx + ".md"
        fldr_path = self.mdio.cfg.mdio_inbox_folder()
        file_path = get_path_in_folder(fldr_path, f_name)
      lines = []
      sug_line = "- " + sug
      lines.append(sug_line)
      write_lines(file_path, lines, True)
      print(f"saved to: {file_path}")
    else:
      print("abandoning empty suggestion")
