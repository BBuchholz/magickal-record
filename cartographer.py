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

  def verify_folder(self):
    return path_exists(CARTOGRAPHER_FOLDER)

  def verify_cets_file(self):
    return path_exists(CETS_FILE)

  def get_cart_files(self):
    cart_files = get_xslx_files(CARTOGRAPHER_FOLDER)
    return cart_files

  def get_release_file_names(self):
    cets_file_lines = get_lines_from(CETS_FILE)
    print(f"cets file lines: {len(cets_file_lines)}")
    release_file_names = []
    releases_found = False
    index = 0
    while index < len(cets_file_lines):
      line = cets_file_lines[index]
      print(f"line is {line}")
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

  def get_myrkis(self):
    myrkis = []
    if self.selected_file is not None:
      file_path = get_path_in_folder(CARTOGRAPHER_FOLDER, self.selected_file)
      df = pd.read_excel(file_path, sheet_name='Cards')
      df_dict = df.to_dict()
      ### LEAVE THIS HERE FOR DEBUGGING
      # print(df_dict)
      # print(df_dict['MYRKI'].values())
      for myrki in df_dict['MYRKI'].values():
        myrki = myrki.strip()
        if myrki not in myrkis:
          myrkis.append(myrki)
    return myrkis


  def get_related_myrkis(self):
    myrkis = []
    if self.selected_file is not None:
      file_path = get_path_in_folder(CARTOGRAPHER_FOLDER, self.selected_file)
      df = pd.read_excel(file_path, sheet_name='Cards')
      df_dict = df.to_dict()
      ### LEAVE THIS HERE FOR DEBUGGING
      # print(df_dict)
      # print(df_dict['Related MYRKIS'].values())
      for myrki_lst_str in df_dict['Related MYRKIS'].values():
        if str(myrki_lst_str) != 'nan':
          myrkis_split = myrki_lst_str.split(",")
          for myrki in myrkis_split:
            myrki = myrki.strip()
            if myrki not in myrkis:
              myrkis.append(myrki)
    return myrkis
  
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