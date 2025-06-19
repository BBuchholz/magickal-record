class CardRowList:
  def __init__(self):
    self.cards = []

  def __len__(self):
    return len(self.cards)
  
  def append(self, card):
    self.cards.append(card)

  def contains_exactly(self, card: dict):
    print("CardRowList.contains_exactly(card) not implemented")
    return True # gets scheduled for insert, until implemented assume already found

  def contains_outdated(self, card:dict):
    print("CardRowList.contains_outdated(card) not implemented")
    return False # gets scheduled for update, until implemented assume no update necessary