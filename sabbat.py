class Sabbat():
  def __init__(self, prefix, aliases, year):
    self.prefix = prefix
    self.aliases = aliases
    self.year = year

  def __str__(self):
    return f"{self.aliases[0]} {str(self.year)}"