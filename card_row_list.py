class CardRowList:
  def __init__(self):
    self.cards = []
    self.load_sheet_orm()

  def __len__(self):
    return len(self.cards)
  
  def append(self, card):
    self.cards.append(card)

  def load_sheet_orm(self):
    self.sheet_orm = {}
    self.sheet_orm['cardCode'] = 'Card Id'
    # TODO: fill in for all sheet column names

  def get_orm_for_db_field(self, field):
    return self.sheet_orm(field)

  def contains_exactly(self, card: dict):
    seeking_card_code = card['Card Id']
    if seeking_card_code is None:
      seeking_card_code = ""
    if len(seeking_card_code) > 0:
      print(f"seeking card code: {seeking_card_code}")
      found_card_code = False
      for card_row in self.cards:
        # TODO: check each field, if even a single one is different, return false
        # start with cardCode, if that differs can return False immediately
        
        # check field cardCode
        # object relational map, field names and sheet names differ so need a reference
        orm_map = self.get_orm_for_db_field("cardCode") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field cardId
        orm_map = self.get_orm_for_db_field("cardId") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field myrkiValue
        orm_map = self.get_orm_for_db_field("myrkiValue") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field cardText
        orm_map = self.get_orm_for_db_field("cardText") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field cetCode
        orm_map = self.get_orm_for_db_field("cetCode") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field imageFile
        orm_map = self.get_orm_for_db_field("imageFile") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field canvaLinkHref
        orm_map = self.get_orm_for_db_field("canvaLinkHref") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field myrkiCreditCollabId
        orm_map = self.get_orm_for_db_field("myrkiCreditCollabId") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field textCreditCollabId
        orm_map = self.get_orm_for_db_field("textCreditCollabId") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
        
        # check field imageCreditCollabId 
        orm_map = self.get_orm_for_db_field("imageCreditCollabId") 
        if not self.fields_match_exactly(card, card_row, orm_map):
          return False
      
      # if found and no fields triggered a false return, at this point all fields match
      return found_card_code 
    else:
      print(f"card has no card code set, potentially acceptable remix, allowing duplicate")
      return False

  def contains_outdated(self, card:dict):
    print("CardRowList.contains_outdated(card) not implemented")
    return False # gets scheduled for update, until implemented assume no update necessary