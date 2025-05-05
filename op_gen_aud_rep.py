from menus import (
  LineOption,
)
from cartio import CartIO
from files import write_lines

class GenerateAuditReportOp(LineOption):
  def __init__(self, cart: CartIO):
    self.cart = cart

  def key(self):
    return "gen"
  
  def desc(self):
    return "Generate Audit Report"
  
  def run(self):
    myrkis = self.cart.get_all_myrkis()
    file_path = self.cart.cfg.audit_summary_file()
    write_lines(file_path, myrkis, True)
    print(f"{len(myrkis)} lines written to: {file_path}")