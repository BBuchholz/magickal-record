class CardRowList:
  def __init__(self):
    self.cards = []
    self.load_sheet_orm()

  def __len__(self):
    return len(self.cards)
  
  def append(self, card: dict):
    self.cards.append(card)

  def load_sheet_orm(self):
    self.sheet_orm = {}
    # TODO: change these to the correct values for the column names
    # db fields are correct, replact Card Id for each
    self.sheet_orm['cardCode'] = 'Card Id'
    self.sheet_orm['cardId'] = 'Card Id'
    self.sheet_orm['myrkiValue'] = 'Card Id'
    self.sheet_orm['cardText'] = 'Card Id'
    self.sheet_orm['cetCode'] = 'Card Id'
    self.sheet_orm['imageFile'] = 'Card Id'
    self.sheet_orm['canvaLinkHref'] = 'Card Id'
    self.sheet_orm['camyrkiCreditCollabIdrdCode'] = 'Card Id'
    self.sheet_orm['textCreditCollabId'] = 'Card Id'
    self.sheet_orm['imageCreditCollabId'] = 'Card Id'

  def get_orm_value_for_db_field(self, card, field):
    return card[self.sheet_orm[field]]

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
        orm_mapped_value = self.get_orm_value_for_db_field(card, "cardCode") 
        row_value = card_row["cardCode"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field cardId
        orm_mapped_value = self.get_orm_value_for_db_field(card, "cardId") 
        row_value = card_row["cardId"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field myrkiValue
        orm_mapped_value = self.get_orm_value_for_db_field(card, "myrkiValue") 
        row_value = card_row["myrkiValue"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field cardText
        orm_mapped_value = self.get_orm_value_for_db_field(card, "cardText") 
        row_value = card_row["cardText"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field cetCode
        orm_mapped_value = self.get_orm_value_for_db_field(card, "cetCode") 
        row_value = card_row["cetCode"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field imageFile
        orm_mapped_value = self.get_orm_value_for_db_field(card, "imageFile") 
        row_value = card_row["imageFile"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field canvaLinkHref
        orm_mapped_value = self.get_orm_value_for_db_field(card, "canvaLinkHref") 
        row_value = card_row["canvaLinkHref"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field myrkiCreditCollabId
        orm_mapped_value = self.get_orm_value_for_db_field(card, "myrkiCreditCollabId") 
        row_value = card_row["myrkiCreditCollabId"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field textCreditCollabId
        orm_mapped_value = self.get_orm_value_for_db_field(card, "textCreditCollabId") 
        row_value = card_row["textCreditCollabId"]
        if not orm_mapped_value == row_value:
          return False
        
        # check field imageCreditCollabId 
        orm_mapped_value = self.get_orm_value_for_db_field(card, "imageCreditCollabId") 
        row_value = card_row["imageCreditCollabId"]
        if not orm_mapped_value == row_value:
          return False
      
      # if found and no fields triggered a false return, at this point all fields match
      return found_card_code 
    else:
      print(f"card has no card code set, potentially acceptable remix, allowing duplicate")
      return False

  def contains_outdated(self, card:dict):
    print("CardRowList.contains_outdated(card) not implemented")
    return False # gets scheduled for update, until implemented assume no update necessary