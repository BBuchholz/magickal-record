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
            print(f"ignoring")
          else:
            print(f"did not find myrki '{myrki}' in existing myrkis")
            print(f"queueing myrki for insertion")
            queued_myrkis.append(myrki)
            print(f"myrki queued for insertion: {myrki}")
            print(f"myrkis queued for insertion: {len(queued_myrkis)}")
        print(f"total myrkis queued for insertion: {len(queued_myrkis)}")
        print(f"inserting myrkis: {queued_myrkis}")
        self.sql.batch_insert_myrkis(queued_myrkis)
        print(f"inserted myrkis")
          
          



if __name__ == "__main__":
  tcfg = NwdTestConfig()
  sql = SqlIO(tcfg)
  cart = CartIO(tcfg)
  reg = MyrkiRegistry(tcfg)
  main = InsertSelectedCartFileIntoCurrentDb(sql, cart, reg)
  main.run()