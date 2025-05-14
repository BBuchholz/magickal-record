from obsidio import ObsidIO
from cfg import NwdTestConfig
from menus import LineOption

import shutil
from os import path

class CopyFilesOp(LineOption):
  def __init__(self, obio: ObsidIO, files):
    self.vault_location = obio.last_loaded_vault
    self.files = files
    self.obio = obio

  def key(self):
    return "cpy"
  
  def desc(self):
    return f"Copy {len(self.files)} files into ObsidIO"
  
  def run(self):
    print("copying files...")

    for file in self.files:
      print(f"processing file: {file}")
      src = path.join(self.vault_location, file)
      print(f"source: {src}")
      dest_fldr = self.obio.obsidio_folder()
      dest = path.join(dest_fldr, file)
      print(f"destination: {dest}")
      shutil.copy2(src, dest)


    print("done copying files.")

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  obio.load_vaults(tcfg.test_vault_config_file())
  files = tcfg.test_vault_files()
  main = CopyFilesOp(obio, files)
  main.run()