from gitio import GitIO
from menus import SubMenu
from cfg import Config, NwdTestConfig
from op_lst_git import ListGitIOFoldersOp
from op_aud_git import AuditGitIOFoldersOp

class GitIOMenu(SubMenu):
  def __init__(self, cfg: Config):
    print(f"loading GitIO configuration: {cfg.status()}")
    self.cfg = cfg
    self.git = GitIO(cfg)

  def key(self):
    return "git"
  
  def desc(self):
    return "GitIO Menu"
  
  def get_ops(self):
    ops = []
    ops.append(ListGitIOFoldersOp(self.git))
    ops.append(AuditGitIOFoldersOp(self.git))
    return ops
  
if __name__ == "__main__":
  tcfg = NwdTestConfig()
  main = GitIOMenu(tcfg)
  main.show_menu()