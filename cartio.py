import pandas as pd

from constants import (
  CARTOGRAPHER_FOLDER,
  CETS_FILE,
)
from files import (
  path_exists,
  get_lines_from,
  get_xslx_files,
  get_path_in_folder,
)

class Cartographer:
  def __init__(self):
    self.selected_file = None
    self.cards = {}
    # self.myrkis = []
    # self.myrkis_loaded = False
    # self.related_myrkis = []
    # self.related_myrkis_loaded = False

  def verify_folder(self):
    return path_exists(CARTOGRAPHER_FOLDER)

  def verify_cets_file(self):
    return path_exists(CETS_FILE)

  def get_cart_files(self):
    cart_files = get_xslx_files(CARTOGRAPHER_FOLDER)
    return cart_files

  def get_release_file_names(self):
    cets_file_lines = get_lines_from(CETS_FILE)
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
    self.selected_file = file_name
    # self.load_myrkis()
    # self.load_related_myrkis()
    if self.selected_file is not None:
      file_path = get_path_in_folder(CARTOGRAPHER_FOLDER, self.selected_file)
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
      

  # def load_myrkis(self):
  #   if self.myrkis_loaded:
  #     return
  #   elif self.selected_file is not None:
  #     file_path = get_path_in_folder(CARTOGRAPHER_FOLDER, self.selected_file)
  #     df = pd.read_excel(file_path, sheet_name='Cards')
  #     df_dict = df.to_dict()
  #     ### LEAVE THIS HERE FOR DEBUGGING
  #     # print(df_dict)
  #     # print(df_dict['MYRKI'].values())
  #     for myrki in df_dict['MYRKI'].values():
  #       myrki = myrki.strip()
  #       if myrki not in self.myrkis:
  #         self.myrkis.append(myrki)
  #     self.myrkis_loaded = True

  # def load_related_myrkis(self):
  #   if self.related_myrkis_loaded:
  #     return
  #   if self.selected_file is not None:
  #     file_path = get_path_in_folder(CARTOGRAPHER_FOLDER, self.selected_file)
  #     df = pd.read_excel(file_path, sheet_name='Cards')
  #     df_dict = df.to_dict()
  #     ### LEAVE THIS HERE FOR DEBUGGING
  #     # print(df_dict)
  #     # print(df_dict['Related MYRKIS'].values())
  #     for myrki_lst_str in df_dict['Related MYRKIS'].values():
  #       if str(myrki_lst_str) != 'nan':
  #         myrkis_split = myrki_lst_str.split(",")
  #         for myrki in myrkis_split:
  #           myrki = myrki.strip()
  #           if myrki not in self.related_myrkis:
  #             self.related_myrkis.append(myrki)
  #     self.related_myrkis_loaded = True

  def get_myrkis(self):
    # self.load_myrkis() # idempotent
    myrkis = []
    for card in self.cards.values():
      myrki = card["MYRKI"]
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