class Sabbat():
  def __init__(self, prefix, aliases, date_stamp: str):
    self.prefix = prefix
    self.aliases = aliases
    self.year = date_stamp[:2]
    self.month = date_stamp[2:4]
    self.day = date_stamp[4:6]

  def __str__(self):
    return f"{self.aliases[0]} 20{str(self.year)}"
  
  def as_date_stamp(self):
    return f"{self.year}{self.month}{self.day}"
  
  def as_string_code(self):
    return f"{self.prefix}{self.year}"