from menus import LineOption
from obsidio import ObsidIO
from cfg import NwdTestConfig
from files import get_lc_basename_from_path

class IsolateObsidIOFileOp(LineOption):
  def __init__(self, obsid: ObsidIO):
    self.obsid = obsid

  def key(self):
    return "iso"
  
  def desc(self):
    return "Isolate ObsidIO File"
  
  def run(self):
    file_name = input("Enter markdown file name (md suffix optional) that you want to isolate: ")
    lc_fname = file_name.lower()
    if not lc_fname.endswith(".md"):
      lc_fname = lc_fname + ".md"
    print(f"FileName normalized to: {lc_fname}")
    
    print("checking if file exists...")
    found_path = ""

    for file in self.obsid.list_obsidio_files():
      print(f"checking {file}")
      lc_to_check = get_lc_basename_from_path(file)
      if lc_to_check == lc_fname:
        print(f"Found: {lc_fname}")
        found_path = file

    if found_path != "":
      print("not fully implemented")
      print(f"Found path to isolate: {found_path}")
    else:
      print(f"Could not find file name: {lc_fname}")
    
    
    

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  obio = ObsidIO(tcfg)
  main = IsolateObsidIOFileOp(obio)
  main.run()