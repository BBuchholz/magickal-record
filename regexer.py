import re

class Regexer:

  def match_uuid_suffix(self, suffix: str):
    pattern = r"^[a-zA-Z0-9]{4}$"
    return re.match(pattern, suffix)
  
  def match_sabbat_code(self, code: str):
    pattern = r"^[A-Z]{3}\d{2}$"
    return re.match(pattern, code)