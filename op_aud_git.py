from menus import LineOption
from gitio import GitIO
from ceter import CetER
from cfg import NwdTestConfig

class AuditGitIOFoldersOp(LineOption):
  def __init__(self, git: GitIO):
    self.git = git
    self.ceter = CetER()

  def key(self):
    return "aud"
  
  def desc(self):
    return "Audit GitIO Folders"
  
  def run(self):
    expected_cets = self.ceter.get_expected_cets_list()
    expected_count = len(expected_cets)
    print(f"expected cets: {expected_count}")
    for expected_cet in expected_cets:
      print(f"expected cet: {expected_cet}")
    print("")
    print(f"checking cet folder for existing cets")
    cet_folder = self.git.cfg.cets_folder(False)
    print(f"checking cet folder: {cet_folder}")
    repos = self.git.list_repos()
    repo_count = len(repos)
    if repo_count < 1:
      print("no repos found")
    else:
      print(f"found {repo_count} repos:")
      for repo in repos:
        self.ceter.audit_repo(repo)


if __name__ == "__main__":
  tcfg = NwdTestConfig()
  git = GitIO(tcfg)
  main = AuditGitIOFoldersOp(git)
  main.run()