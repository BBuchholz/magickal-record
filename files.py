##### moving constants to cfg
# from constants import OBSIDIAN_TEST_FOLDER
from cfg import NwdTestConfig
import os

def folder_exists(folder_path):
  dir_path = os.path.expanduser(folder_path)
  return os.path.exists(dir_path)

def path_exists(file_or_folder_path):
  full_path = os.path.expanduser(file_or_folder_path)
  return os.path.exists(full_path)

def get_md_files(folder_path, prefix):
  return get_files_by_ext(folder_path, ".md", prefix)

def get_xslx_files(folder_path):
  return get_files_by_ext(folder_path, ".xlsx")

def get_files_by_ext(folder_path, extension, prefix=""):
  # expand user if needed
  folder_path = os.path.expanduser(folder_path)
  file_list = []
  if not folder_exists(folder_path):
    print(f"folder path not found: {folder_path}")
    return file_list
  
  for file_name in os.listdir(folder_path):
    if file_name.endswith(extension):
      if file_name.startswith(prefix):
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
  dir_path = os.path.expanduser(tcfg.obsidian_test_folder)
  return os.path.join(dir_path, file_name)

def get_path_in_folder(folder_path, file_name):
  dir_path = os.path.expanduser(folder_path)
  return os.path.join(dir_path, file_name)
  
# TODO: make this account for a missing .md suffix
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