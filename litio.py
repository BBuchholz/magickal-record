from myr_file import MyrFile

class LitIO:
  def __init__(self):
    self.myr_files = []

  def get_source_values(self):
    source_values = []
    for myr_file in self.myr_files:
      for line in myr_file.get_lines():
        if line.lower().startswith("source: "):
          source_value = line[8:]
          source_values.append(source_value)
    return source_values
  
  def add_myr_file(self, myr_file):
    self.myr_files.append(myr_file)