from constants import OBSIDIAN_TEST_FOLDER
import os

def folder_exists(folder_path):
  dir_path = os.path.expanduser(folder_path)
  return os.path.exists(dir_path)

def get_path(file_name):
  """
  gets the path for given file_name from the
  folder specified in constants file as
  OBSIDIAN_TEST_FOLDER
  """
  dir_path = os.path.expanduser(OBSIDIAN_TEST_FOLDER)
  return os.path.join(dir_path, file_name)
  
# TODO: make this account for a missing .md suffix
def get_lines_array(file_name):
  """
  gets the arrary of lines from the specified 
  file_name in the folder specified in the
  constants file as READ_FROM_FOLDER

  does not currently check for the .md suffix
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

def print_lines_array(file_name, lines):
  """
  prints the lines in the supplied lines array 
  prefaces the printing with file_name and line count
  """
  print(f"File Name: {file_name} has {len(lines)} lines: ")
  for index, line in enumerate(lines):
    print(f"Line {index}: {line}")