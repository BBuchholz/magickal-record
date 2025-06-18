class MyrkiRowList:
  def __init__(self):
    self.myrkis = []

  def __len__(self):
    return len(self.myrkis)

  def append(self, myrki):
    self.myrkis.append(myrki)

  def contains(self, myrki):
    # a case insensitive duplicate of the "in" operate
    # cowboy coded, replace this later if there is a cleaner way to do this
    found = False
    for any_myrki in self.myrkis:
      if any_myrki.lower() == myrki.lower():
        found = True
    return found