# This option creates an audit report which we 
# can grow over time and 
# TODO: should be its own submenu with 
# the ability to display different parts of 
# the report after it has been generated

from cartographer import Cartographer
from menus import SubMenu

from op_gen_aud_rep import GenerateAuditReportOp
from op_disp_aud_sum import DisplayAuditSummaryOp

class AudRepMenu(SubMenu):
  def __init__(self):
    super().__init__()
  
  def key(self):
    return "rep"
  
  def desc(self):
    return "Audit Report menu"
  
  def get_ops(self):
    ops = []
    ops.append(GenerateAuditReportOp(self.cart))
    ops.append(DisplayAuditSummaryOp(self.cart))
    return ops