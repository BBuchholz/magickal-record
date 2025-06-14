from sqlio import SqlIO
from menus import LineOption
from cfg import NwdTestConfig
from cartio import CartIO

class InsertSelectedCartFileIntoCurrentDb(LineOption):
  def __init__(self, sql: SqlIO, cart: CartIO):
    self.sql = sql
    self.cart = cart

  def desc(self):
    return "Insert Cart File Into Db"
  
  def key(self):
    return "ins"
  
  def run(self):
    if len(self.cart.selected_files) < 1:
      print("no cartographer file selected")
      print("please select a file using")
      print("the select option in the cartographer menu")
      print("")
    elif self.sql.selected_db is None:
      print("no db file selected")
      print("please select a file using")
      print("the select option")
      print("")
    else:
      card_count = len(self.cart.cards)
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
        myrkis = self.sql.select_myrkis()
        print(f"existing myrkis found: {myrkis}")
        cards = self.sql.select_cards()
        print(f"existing cards found: {cards}")
        for card in self.cart.cards:
          print(f"checking for card: {card}")
          print("TODO: check here")



if __name__ == "__main__":
  tcfg = NwdTestConfig()
  sql = SqlIO(tcfg)
  cart = CartIO(tcfg)
  main = InsertSelectedCartFileIntoCurrentDb(sql, cart)
  main.run()