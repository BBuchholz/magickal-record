from menus import LineOption
from mdio import MDIO
from chronio import ChronIO
from files import (
  get_path_in_folder,
  path_exists,
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
    print(f"Saving suggestion to file system: {sug}")
    sfx = self.chron.get_suffix()
    f_name = "Suggestion - " + sfx + ".md"
    fldr_path = self.mdio.cfg.mdio_input_folder()
    file_path = get_path_in_folder(fldr_path, f_name)
    while path_exists(file_path):
      sfx = self.chron.get_suffix(sfx)
      f_name = "Suggestion - " + sfx + ".md"
      fldr_path = self.mdio.cfg.mdio_input_folder()
      file_path = get_path_in_folder(fldr_path, f_name)
    print(f"saved to: {file_path}")
    print("TODO: finish implementing")
    #TODO: implement a suggestion option that 
    # logs user input to a timestamped md file 
    # in mdio_inbox_folder like a suggestion box, 
    # these can then be processed later, which is 
    # why they belong in the mdio_inbox_folder
