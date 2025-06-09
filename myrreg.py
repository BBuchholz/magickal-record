from cfg import Config
from os import path
from obsidio import ObsidIO
from cartreg import CartRegistry
from files import (
  get_prefixed_md_files,
  get_lines_from,
)
from regexer import Regexer

class MyrkiRegistry:
  def __init__(self, cfg: Config):
    self.myrkis = []
    self.myrki_instances = []
    self.obio = ObsidIO(cfg)
    self.cartrg = CartRegistry(cfg)

  def contains_myrki(self, myrki_value):
    for myrki in self.myrkis:
      if myrki.lower() == myrki_value.lower():
        return True
    return False

  def validate_myrki_instance(self, candidate: str):
    # TODO: implement, see sheets for valid 
    # and invalid instances to test against 
    # (write unit test)
    # logic already filters candidates against
    # registered myrkis (ie. only files starting)
    # with a myrki and a dash are "candidates"
    # just need to filter everything that doesn't 
    # end with a 4 digit uuid suffix or a 5 digit Cet code
    res = candidate.rsplit('-', 1)
    regex = Regexer()
    if len(res) < 2:
      # didn't have a dash
      return False 
    else:
      suffix = res[1]
      if regex.match_uuid_suffix(suffix):
        return True
      else:
        if regex.match_sabbat_code(suffix):
          return True
        else:
          return False

  def load(self, verbose=True):
    self.cartrg.load()
    if len(self.cartrg.carts) < 0:
      print("no carts loaded for CartRegistry")
      print("no MyrKiS to search for, aborting...")
      return
    msg = "attempting to load MyrkiRegistry from "
    msg += "stored configuation"
    print(msg)
    # check if stored configuration exists
    verified_file = self.obio._cfg.verified_vault_file()
    if path.exists(verified_file):
      print("verified file found")
      # TODO: mirror CartRegistry.load()  
      vlt_fldr = self.load_vault_fldr_from(verified_file)
      # using cartreg myrki list, 
      myrkis = self.cartrg.get_myrkis(True)
      if verbose:
        print(f"cartreg myrkis are: {myrkis}")
      # check Obsidio verified vault for any file 
      if verbose:
        print(f"checking files in vault: {vlt_fldr}")
      # get everything that starts with a myrki
      all_files = get_prefixed_md_files(
        vlt_fldr, # search the whole vault
        myrkis, # any files starting with these
        False # ignore the dash at this point to get all
      )

      stripped_fnames = []
      # strip file paths
      for md_file in all_files:
        stripped = str(path.basename(md_file))
        stripped = stripped.removesuffix(".md")
        stripped_fnames.append(stripped)

      # then sort into two types:
      myrki_instance_candidates = []
      myrki_candidates = []
      for stripped in stripped_fnames:
        # if in MYRKI-SUFFIX format add to myrki instance candidates
        if "-" in stripped:
          myrki_instance_candidates.append(stripped)
          if verbose:
            print(f"added {stripped} to myrki instance candidates")
        else:
          # add to myrki candidates
          myrki_candidates.append(stripped)
          if verbose:
            print(f"added {stripped} to myrki candidates")

      # filter them against the original list
      if verbose:
        print("")
        print("filtering candidates")
        print("")
      for candidate in myrki_instance_candidates:
        first_half = str(candidate.split("-")[0])
        if first_half.lower() in myrkis:
          if self.validate_myrki_instance(candidate):
            self.myrki_instances.append(candidate)
            if verbose:
              print(f"added {candidate} to myrki instances")
      
      for candidate in myrki_candidates:
        lowered = str(candidate).lower()
        if lowered in myrkis:
          self.myrkis.append(candidate)
          if verbose:
            print(f"added {candidate} to myrkis")

    else:
      print("verified file not found")
      msg = "autoloading is disabled until a verified "
      msg += "vault file is stored using the store "
      msg += "option in the obsidio ops menu (obo)"
      print(msg)
      
  def load_vault_fldr_from(self, verified_file):
    print(f"loading verified file: {verified_file}")
    # load from that file
    lines = get_lines_from(verified_file)
    print("reading from verified file")
    print("if verified file has multiple lines")
    print("only last line will be used")
    print(f"found {len(lines)} line(s)")
    found = ""
    for line in lines:
      found = self.process_verified_file_line(line)
    return found
  
  def process_verified_file_line(self, line):
    found = ""
    if line.lower().startswith("vault_folder: "):
      found = line[14:]
      print(f"found vault_folder: {found}")
    return found