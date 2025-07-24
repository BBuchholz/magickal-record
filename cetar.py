import os

class CetAR:
  """
  Represents a Cet Audit Report
  """
  def __init__(self, short_name, rel_address):
    self.missing_elements = []
    self.short_name = short_name
    self.full_path = os.path.expanduser(rel_address)

  def print_missing_elements(self, verbose=False):
    count = len(self.missing_elements)
    print(f"{count} missing elements for repo: {self.short_name}")
    if verbose: 
      if count > 0:
        for missing_element in self.missing_elements:
          print(missing_element)
      else:
        print(f"no missing elements found for repo: {self.short_name}")
    print("")