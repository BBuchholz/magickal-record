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
    # only these values will map to the sheet values
    # everything else are db reference columns
    # that will require special handling elsewhere
    self.sheet_orm['cardCode'] = 'Card Id'
    self.sheet_orm['myrkiValue'] = 'MYRKI'
    self.sheet_orm['cardText'] = 'Card Text'
    self.sheet_orm['cetCode'] = 'Cet'
    self.sheet_orm['canvaLinkHref'] = 'Canva Link'

  def get_orm_value_for_db_field(self, card, field):
    return card[self.sheet_orm[field]]

  def contains_exactly(self, card: dict):
    seeking_card_code = card['Card Id']
    if seeking_card_code is None:
      seeking_card_code = ""
    if len(seeking_card_code) > 0:
      print(f"seeking card code: {seeking_card_code}")
      for card_row in self.cards:
        # check each field, if even a single one is different, return false
        # start with cardCode, if that differs can return False immediately
        
        # check field cardCode
        # object relational map, field names and sheet names differ so need a reference
        orm_mapped_value = self.get_orm_value_for_db_field(card, "cardCode") 
        row_value = card_row["cardCode"]
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
        
        # check field canvaLinkHref
        orm_mapped_value = self.get_orm_value_for_db_field(card, "canvaLinkHref") 
        row_value = card_row["canvaLinkHref"]
        if not orm_mapped_value == row_value:
          return False
      
      # if found and no fields triggered a false return, at this point all fields match
      return True 
    else:
      print(f"card has no card code set, potentially acceptable remix, allowing duplicate")
      return False

  def contains_outdated(self, card:dict):
    # TODO: VERIFY AND MODIFY, COPIED VERBATIM FROM contains_exactly
    seeking_card_code = card['Card Id']
    if seeking_card_code is None:
      seeking_card_code = ""
    # anything without a card code is a potential remix and should be to NOT BE OUTDATED (no update needed)
    # it MAY NEED INSERTION if there isn't a row that has all the other values EXACTLY the same, so check for that
    if len(seeking_card_code.strip()) == 0:
      print(f"empty card code, checking each existing card for full duplication of all values: {seeking_card_code}")
      found_no_identicals_at_all = True
      for card_row in self.cards:
        # assume every value is identical, flip the boolean if we find anything different
        found_identical = True
        # check each field, if even a single one is different, return True
        # start with cardCode, if that differs can return False immediately
        
        # check field cardCode
        # object relational map, field names and sheet names differ so need a reference
        orm_mapped_value = self.get_orm_value_for_db_field(card, "cardCode") 
        row_value = card_row["cardCode"]
        if not orm_mapped_value == row_value:
          found_identical = False
        
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
        
        # check field canvaLinkHref
        orm_mapped_value = self.get_orm_value_for_db_field(card, "canvaLinkHref") 
        row_value = card_row["canvaLinkHref"]
        if not orm_mapped_value == row_value:
          return False
      
        # if still true at this point all fields match, found identical and needs no update
        if found_identical:
          print(f"found identical, no update needed, skipping")
          found_no_identicals_at_all = False
          return False
      if found_no_identicals_at_all:
        print("not yet implemented, need to check by card code for update, will only be one, card code is unique identifier")
        card_row_to_check_for_update = None
        for card_row in self.cards:
          # check field cardCode
          # object relational map, field names and sheet names differ so need a reference
          orm_mapped_value = self.get_orm_value_for_db_field(card, "cardCode") 
          row_value = card_row["cardCode"]
          if len(orm_mapped_value.strip()) > 0 and orm_mapped_value == row_value:
            card_row_to_check_for_update = card_row

        # assume no update needed
        update_needed = False
        if card_row_to_check_for_update is not None:
          # check each other value here

          # check field myrkiValue
          orm_mapped_value = self.get_orm_value_for_db_field(card, "myrkiValue") 
          row_value = card_row["myrkiValue"]
          if len(orm_mapped_value.strip()) > 0 and not orm_mapped_value == row_value:
            update_needed = True
          
          # check field cardText
          orm_mapped_value = self.get_orm_value_for_db_field(card, "cardText") 
          row_value = card_row["cardText"]
          if len(orm_mapped_value.strip()) > 0 and not orm_mapped_value == row_value:
            update_needed = True
          
          # check field cetCode
          orm_mapped_value = self.get_orm_value_for_db_field(card, "cetCode") 
          row_value = card_row["cetCode"]
          if len(orm_mapped_value.strip()) > 0 and not orm_mapped_value == row_value:
            update_needed = True
          
          # check field canvaLinkHref
          orm_mapped_value = self.get_orm_value_for_db_field(card, "canvaLinkHref") 
          row_value = card_row["canvaLinkHref"]
          if len(orm_mapped_value.strip()) > 0 and not orm_mapped_value == row_value:
            update_needed = True
        if update_needed:
          return True # if we reach here we found a matching card code that has different values
    else:
      print(f"card has no card code set, potentially acceptable remix, no update needed")
      return False