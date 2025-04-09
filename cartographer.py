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
        myrkis.append(myrki.strip())
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
            myrkis.append(myrki.strip())
    return myrkis