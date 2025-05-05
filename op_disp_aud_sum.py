from menus import (
  LineOption,
)
from cartio import CartIO
from files import get_lines_from

class DisplayAuditSummaryOp(LineOption):
  def __init__(self, cart: CartIO):
    self.cart = cart

  def key(self):
    return "sum"
  
  def desc(self):
    return "Display Audit Summary"
  
  def run(self):
    file_path = self.cart.cfg.audit_summary_file()
    lines = get_lines_from(file_path)
    if len(lines) > 0:
      for line in lines:
        print(line)
    else:
      print("audit report either empty or not found")