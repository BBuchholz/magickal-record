##### moving constants to cfg
# from constants import OBSIDIAN_TEST_FOLDER
from cfg import NwdTestConfig
import os

def folder_exists(folder_path):
  dir_path = os.path.expanduser(folder_path)
  return os.path.exists(dir_path)

def ensure_folder(folder_path):
  if not os.path.exists(folder_path):
      os.makedirs(folder_path)
      print(f"Folder '{folder_path}' created.")
  else:
      print(f"Folder '{folder_path}' already exists.")

def path_exists(file_or_folder_path):
  full_path = os.path.expanduser(file_or_folder_path)
  return os.path.exists(full_path)

def get_filtered_md_files(folder_path, filter):
  return get_files_by_ext(folder_path, ".md", "", filter)

def get_multi_filter_md_files(folder_path, filters):
  unfiltered = get_files_by_ext(folder_path, ".md", "", "")
  filtered = []
  for file_path in unfiltered:
    for filter in filters:
      if filter.lower() in os.path.basename(file_path).lower():
        filtered.append(file_path)
  return filtered

def get_prefixed_md_files(folder, prefixes, include_dash=False):
  unfiltered = get_files_by_ext(folder, ".md", "", "")
  filtered = []
  for file_path in unfiltered:
    for prefix in prefixes:
      if include_dash:
        prefix = prefix + "-"
      if os.path.basename(file_path).lower().startswith(prefix.lower()):
        filtered.append(file_path)
  return filtered

def get_md_files(folder_path, prefix):
  return get_files_by_ext(folder_path, ".md", prefix)

def get_xslx_files(folder_path):
  return get_files_by_ext(folder_path, ".xlsx")

def get_sqlite3_files(folder_path):
  return get_files_by_ext(folder_path, ".sqlite3")

def get_files_by_ext(folder_path, extension, prefix="", filter=""):
  # expand user if needed
  folder_path = os.path.expanduser(folder_path)
  file_list = []
  if not folder_exists(folder_path):
    print(f"folder path not found: {folder_path}")
    return file_list
  
  for file_name in os.listdir(folder_path):
    if file_name.endswith(extension):
      if file_name.startswith(prefix):
        if filter in file_name:
          file_list.append(file_name)
  
  return file_list



def get_path(file_name):
  """
  gets the path for given file_name from the
  folder specified in TestingConfig
  """
  tcfg = NwdTestConfig()
  ##### moving constants to cfg
  # dir_path = os.path.expanduser(OBSIDIAN_TEST_FOLDER)
  dir_path = os.path.expanduser(tcfg.obsidian_test_folder())
  return os.path.join(dir_path, file_name)

def get_path_in_folder(folder_path, file_name):
  dir_path = os.path.expanduser(folder_path)
  return os.path.join(dir_path, file_name)
  
def get_lines_array(file_name):
  """
  gets the arrary of lines from the specified 
  file_name in the folder specified in the
  constants file as READ_FROM_FOLDER

  does not check for the .md suffix
  """
  lines = []
  file_path = get_path(file_name)
  if os.path.exists(file_path):
    with open(file_path, 'r') as file:
      line = file.readline()
      while line:
        lines.append(line.strip())
        line = file.readline()
  else:
    print(f"File '{file_path}' does not exists")
  return lines

def write_lines(file_path, lines, add_newlines):
  if add_newlines:
    new_lines = []
    for line in lines:
      new_lines.append(line + "\n")
    lines = new_lines
  file_path = os.path.expanduser(file_path)
  f = open(file_path, "w")
  f.writelines(lines)
  f.close()

def get_lines_from(file_path):
  """
  gets the arrary of lines from the specified 
  file_path

  does not check for the .md suffix
  """
  lines = []
  file_path = os.path.expanduser(file_path)
  if os.path.exists(file_path):
    with open(file_path, 'r') as file:
      line = file.readline()
      while line:
        lines.append(line.strip())
        line = file.readline()
  else:
    print(f"File '{file_path}' does not exists")
  return lines

def print_lines_array(file_name, lines):
  """
  prints the lines in the supplied lines array 
  prefaces the printing with file_name and line count
  """
  print(f"File Name: {file_name} has {len(lines)} lines: ")
  for index, line in enumerate(lines):
    print(f"Line {index}: {line}")