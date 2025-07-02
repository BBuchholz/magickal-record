from sqlio import SqlIO
from menus import LineOption
from cfg import NwdTestConfig
from cartio import CartIO
from myrreg import MyrkiRegistry


class InsertSelectedCartFileIntoCurrentDb(LineOption):
  def __init__(self, sql: SqlIO, cart: CartIO, reg: MyrkiRegistry):
    self.sql = sql
    self.cart = cart
    self.reg = reg

  def desc(self):
    return "Insert Cart File Into Db"
  
  def key(self):
    return "ins"
  
  def run(self):
    cards = []
    cards_to_insert = []
    myrkis = []
    use_cart = False
    use_reg = False
    if len(self.cart.selected_files) < 1:
      print("no cartographer file selected")
      msg = "would you like to use the "
      msg += "MyrkiRegistry instead? "
      msg += "(enter y for yes, anything "
      msg += "else for no): "
      response = input(msg)
      if response == 'y':
        use_reg = True
        print("loading MyrkiRegistry")
        self.reg.load()
        cards_to_insert = self.reg.cartrg.carts
      else:
        print("please select a file using")
        print("the select option in the cartographer menu")
        print("")
    else:
      use_cart = True
      cards_to_insert = self.cart.cards
    if self.sql.selected_db is None:
      print("no db file selected")
      default_db = "default.sqlite3"
      msg = "would you like to use the "
      msg += "default db file instead? "
      msg += f"[{default_db}]"
      msg += "(enter y for yes, anything "
      msg += "else for no): "
      response = input(msg)
      if response == 'y':
        self.sql.select_file(default_db)
    if self.sql.selected_db is None:
      print("please select a file using")
      print("the select option in the sql menu")
      print("")
    else:
      card_count = len(cards_to_insert)
      print(f"cards to insert: {len(cards_to_insert)}")
      if card_count < 1:
        print("no cards to insert")
      else:
        # TODO: MODIFY THIS 
        # insert myrkis from selected file
        # insert myrki instances (cards) from selected file
        # TODO: should prompt with a list of what is 
        # about to be inserted and then require 
        # a confirmation 
        # (eg. "enter y to continue, any other 
        # key to abort")
        print(f"found {card_count} cards to insert")
        print(f"checking to see if they are already in the database first")
        existing_myrkis = self.sql.select_myrkis()
        queued_myrkis = []
        queued_card_insertions = []
        queued_card_updates = []
        print(f"existing myrkis found: {len(existing_myrkis)}")
        # TODO: after myrkis are working, make this work, 
        # already started just uncomment and run to see where its at
        existing_cards = self.sql.select_cards()
        print(f"existing cards found: {len(existing_cards)}")
        for card in cards_to_insert:
          myrki = card['MYRKI']
          card_id = card['Card Id']
          card_id = card_id if card_id.strip() != "" else "NO CARD ID"
          print(f"checking for myrki: {myrki} (card: {card_id})")
          if existing_myrkis.contains(myrki):
            print(f"found myrki '{myrki}' in existing myrkis")
            print(f"ignoring myrki insertion")
            if existing_cards.contains_exactly(card):
              print(f"card already exists in database with no changes: {myrki} -> {card_id}")
              print(f"ignoring card: {myrki} -> {card_id}")
              print("")
            elif existing_cards.contains_outdated(card):
              print(f"previous version found of card: {myrki} -> {card_id}")
              print(f"updating from previous verison: {myrki} -> {card_id}")
              print(f"queueing new version for update: {myrki} -> {card_id}")
              print(f"queueing card: {card}")
              queued_card_updates.append(card)
              print("")
            else:
              print(f"new card found: {myrki} -> {card_id}")
              print(f"queuing new card for insertion: {myrki} -> {card_id}")
              print(f"queueing card: {card}")
              queued_card_insertions.append(card)
              print("")
          else:
            print(f"did not find myrki '{myrki}' in existing myrkis")
            print(f"queueing myrki for insertion")
            queued_myrkis.append(myrki)
            print(f"myrki queued for insertion: {myrki}")
            print(f"myrkis queued for insertion: {len(queued_myrkis)}")
        print(f"total myrkis queued for insertion: {len(queued_myrkis)}")
        if len(queued_myrkis) > 0:
          print(f"inserting myrkis: {queued_myrkis}")
          self.sql.batch_insert_myrkis(queued_myrkis)
          print(f"inserted myrkis")
        else:
          print("no myrkis to insert, skipping")
        qci_total = len(queued_card_insertions)
        print(f"total cards queued for insertion: {qci_total}")
        if qci_total > 0:
          print(f"inserting cards:")
          qci_count = 0
          for queued_card in queued_card_insertions:
            qci_count += 1
            print(f"queued for insertion, card {qci_count} of {qci_total}:")
            print(queued_card)
          self.sql.batch_insert_cards(queued_card_insertions)
          print("inserted cards")
        else:
          print("no cards to insert, skipping")
        print(f"total cards queued for update: {len(queued_card_updates)}")
        if len(queued_card_updates) > 0:
          print(f"updating cards: {queued_card_updates}")
          self.sql.batch_update_cards(queued_card_updates)
          print("updated cards")
        else:
          print("no cards to update, skipping")
          

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  sql = SqlIO(tcfg)
  cart = CartIO(tcfg)
  reg = MyrkiRegistry(tcfg)
  main = InsertSelectedCartFileIntoCurrentDb(sql, cart, reg)
  main.run()