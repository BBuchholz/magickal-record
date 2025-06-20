class CardRowList:
  def __init__(self):
    self.cards = []

  def __len__(self):
    return len(self.cards)
  
  def append(self, card):
    self.cards.append(card)

  def contains_exactly(self, card: dict):
    seeking_card_code = card['Card Id']
    if seeking_card_code is None:
      seeking_card_code = ""
    if len(seeking_card_code) > 0:
      print(f"seeking card code: {seeking_card_code}")
      print("CardRowList.contains_exactly(card) not implemented")
      return True # gets scheduled for insert, until implemented assume already found
    else:
      print(f"card has no card code set, potentially acceptable remix, allowing duplicate")
      return False

  def contains_outdated(self, card:dict):
    print("CardRowList.contains_outdated(card) not implemented")
    return False # gets scheduled for update, until implemented assume no update necessary