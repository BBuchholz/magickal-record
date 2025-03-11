from constants import READ_FROM_FOLDER
import os

def get_path(file_name):
  dir_path = os.path.expanduser(READ_FROM_FOLDER)
  return os.path.join(dir_path, file_name)
  

def get_lines_array(file_name):
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