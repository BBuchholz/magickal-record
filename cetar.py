import os

class CetAR:
  """
  Represents a Cet Audit Report
  """
  def __init__(self, short_name, rel_address):
    self.missing_elements = []
    self.full_path = os.path.expanduser(rel_address)