from obsidio import ObsidIO
from menus import LineOption
from files import write_lines

class StoreLastLoadedVaultAsDefault(LineOption):
  def __init__(self, obio: ObsidIO):
    self.obio = obio

  def key(self):
    return "store"

  def desc(self):
    msg = "store last loaded vault folder as "
    msg += "verified default obsidian vault  "
    msg += "for autoloading in future sessions"
    return msg

  def run(self):
    print("")
    if self.obio.last_loaded_vault is None:
      print("no vault folder loaded ")
      print("please load a vault using the ")
      print("ldv option in the obo menu")
      print("")
    else:
      lines = [
        f"vault_folder: {self.obio.last_loaded_vault}"
      ]
      file_path = self.obio._cfg.verified_vault_file()
      print(f"storing file as {file_path}")
      write_lines(file_path, lines, True)
      print(f"{len(lines)} line(s) written")