from menus import LineOption
from gardiner import GarDinEr
from files import write_lines

class GenerateGarDinErReport(LineOption):
  def __init__(self, gar: GarDinEr):
    self.gar = gar

  def key(self):
    return "rep"
  
  def desc(self):
    return "Generate GarDinEr Report"
  
  def run(self):
    gr_file_path = self.gar.cfg.gardiner_report_file()
    report_lines = self.gar.report()
    if(len(report_lines) > 0):
      write_lines(gr_file_path, report_lines, True)
      print(f"{len(report_lines)} lines written to {gr_file_path}")
    else:
      print("nothing to write, aborting...")