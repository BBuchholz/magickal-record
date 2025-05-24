import pandas as pd

from cfg import Config

from files import (
  path_exists,
  get_lines_from,
  get_xslx_files,
  get_path_in_folder,
)

class CartIO:
  def __init__(self, cfg: Config):
    self.selected_files = []
    self.cards = {}
    self.cfg = cfg

  def verify_folder(self):
    return path_exists(self.cfg.cartio_folder())

  def verify_cets_file(self):
    return path_exists(self.cfg.cets_file())

  def get_cart_files(self):
    cart_files = get_xslx_files(self.cfg.cartio_folder())
    return cart_files
  
  def print_selected_files(self):
    print("currently selected files: ")
    for file_name in self.selected_files:
      print(file_name)
    print("end of currently selected files")

  def get_release_file_names(self):
    cets_file_lines = get_lines_from(self.cfg.cets_file())
    # print(f"cets file lines: {len(cets_file_lines)}")
    release_file_names = []
    releases_found = False
    index = 0
    while index < len(cets_file_lines):
      line = cets_file_lines[index]
      # print(f"line is {line}")
      if line.startswith("# Releases"):
        releases_found = True
      elif releases_found and line.startswith("# "):
        releases_found = False
      if releases_found and line.startswith("- "):
        name = self.get_release_file_name_from_line(line)
        release_file_names.append(name)
      index += 1
    return release_file_names

  def get_release_file_name_from_line(self, line):
    line = line.replace("- [ ] [[", "")
    line = line.replace("]]", "")
    return line

  def select_file(self, file_name):
    if file_name is not None:
      if file_name not in self.selected_files:
        self.selected_files.append(file_name)
      file_path = get_path_in_folder(self.cfg.cartio_folder(), file_name)
      df = pd.read_excel(file_path, sheet_name='Cards')
      df_dict = df.to_dict()
      # print(df_dict)
      temp_dict = {}
      for key, value in df_dict.items():
        # print(f"Key: {key}")
        for k, v in value.items():
          # print(f"K: {k} V: {v}")
          if k not in temp_dict:
            temp_dict[k] = {}
          if str(v) == "nan":
            temp_dict[k][key] = ''
          else:
            temp_dict[k][key] = v.strip()
      # print(temp_dict)
      for card in temp_dict.values():
        # print(card["MYRKI"])
        # print(card)
        self.cards[card["MYRKI"]] = card
    
  def get_myrkis(self):
    # self.load_myrkis() # idempotent
    myrkis = []
    for card in self.cards.values():
      myrki = card["MYRKI"]
      if myrki not in myrkis:
        myrkis.append(myrki)
    return myrkis
  
  def get_all_myrkis(self):
    myrkis = []
    for myrki in self.get_myrkis():
      if myrki not in myrkis:
        myrkis.append(myrki)
    for myrki in self.get_related_myrkis():
      if myrki not in myrkis:
        myrkis.append(myrki)
    return myrkis

  def get_related_myrkis(self):
    # self.load_related_myrkis() # idempotent
    related_myrkis = []
    for card in self.cards.values():
        myrki_lst_str = card["Related MYRKIS"]
        # print(myrki_lst_str)
        if myrki_lst_str.strip() != '':
          myrkis_split = myrki_lst_str.split(",")
          for myrki in myrkis_split:
            myrki = myrki.strip()
            if myrki not in related_myrkis:
              related_myrkis.append(myrki)
    return related_myrkis

  def get_unconnected_myrkis(self):
    missing_myrkis = []
    # shoud test both ways ie. every myrki 
    # in related column should also be in the 
    # myrki column and every myrki should be 
    # related to at least one other so should 
    # appear in the related column as well
    myrkis = self.get_myrkis()
    related = self.get_related_myrkis()
    for myrki in related:
      if myrki not in myrkis:
        if myrki not in missing_myrkis:
          missing_myrkis.append(myrki)
    for myrki in myrkis:
      if myrki not in related:
        if myrki not in missing_myrkis:
          missing_myrkis.append(myrki)
    return missing_myrkis
  
  def get_card(self, myrki):
    return self.cards[myrki]