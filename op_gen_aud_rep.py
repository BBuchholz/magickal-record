from menus import (
  LineOption,
)

class GenerateAuditReportOp(LineOption):
  def __init__(self, cart):
    self.cart = cart

  def key(self):
    return "gen"
  
  def desc(self):
    return "Generate Audit Report"
  
  def run(self):
    pass