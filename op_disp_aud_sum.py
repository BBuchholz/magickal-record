from menus import (
  LineOption,
)

class DisplayAuditSummaryOp(LineOption):
  def __init__(self, cart):
    self.cart = cart

  def key(self):
    return "sum"
  
  def desc(self):
    return "Display Audit Summary"
  
  def run(self):
    pass
    