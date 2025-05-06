from cartio import CartIO
from menus import SubMenu

from op_gen_aud_rep import GenerateAuditReportOp
from op_disp_aud_sum import DisplayAuditSummaryOp

class AudRepMenu(SubMenu):
  def __init__(self, cart):
    self.cart = cart
  
  def key(self):
    return "rep"
  
  def desc(self):
    return "Audit Report menu"
  
  def get_ops(self):
    ops = []
    ops.append(GenerateAuditReportOp(self.cart))
    ops.append(DisplayAuditSummaryOp(self.cart))
    return ops