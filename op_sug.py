from menus import LineOption
from mdio import MDIO

class SuggestionOp(LineOption):
  def __init__(self, mdio: MDIO):
    super().__init__()
    self.mdio = mdio

  #TODO: implement a suggestion option that 
  # logs user input to a timestamped md file 
  # in mdio inbox folder like a suggestion box, 
  # these can then be processed later, which is 
  # why they belong in the inbox folder