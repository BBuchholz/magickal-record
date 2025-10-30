from cfg import NwdTestConfig

class ProfileExample:
  def __init__(self):
    self.cfg = NwdTestConfig()

  def example_file(self):
    return self.cfg.audit_summary_file()
  
  def example_folder(self):
    return self.cfg.mdio_inbox_folder()
  
  def example_md_file(self):
    return self.cfg.gardiner_report_file()
  
  def example_ufu_md_file(self):
    return self.cfg.eg_ufu_md_file()
  
  def example_git_folder(self):
    return self.cfg.folder_cets_lms24()
  
  def example_io_folder(self):
    return self.cfg.cartio_folder()
  
  def example_myrki_instance_file(self):
    return self.cfg.file_path_star_lth25_md()
  
