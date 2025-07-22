from menus import LineOption
from gitio import GitIO
from ceter import CetER
from cfg import NwdTestConfig

class AuditGitIOFoldersOpRefactor(LineOption):
  def __init__(self, git: GitIO):
    self.git = git
    self.ceter = CetER(self.git)

  def key(self):
    return "ref"
  
  def desc(self):
    return "Audit GitIO Folders Refactored"
  
  def run(self):
    print("this is the refactor of the Audit GitIO Folders Operation")
    print("it is being refactored separately to leave existing, working code alone, as is")
    print("it will be used to add in assessment criteria for the deciding of if autogeneration of CRSL files is appropriate")
    print("this is so we can feed it existing cets and have entire sites generated automagically (currently we are hand crafting the sites and it is repetively time consuming, a perfect candidate for refactoring)")
    print(f"checking cet folder for existing cets")
    #TODO: FIRST CHANGE, each audit funcion 
    # should take an optional VERBOSE parameter 
    # that defaults to TRUE (so existing version 
    # still prints everything) where FALSE only 
    # prints cets to be audited and missing elements at the end
    cet_folder = self.git.cfg.cets_folder(False)
    print(f"checking cet folder: {cet_folder}")
    repos = self.git.list_repos()
    repo_count = len(repos)
    if repo_count < 1:
      print("no repos found")
    else:
      print(f"found {repo_count} repos:")
      self.ceter.compare_repos_to_expected(repos)
      for repo in repos:
        cetar = self.ceter.audit_repo(repo, False)


if __name__ == "__main__":
  tcfg = NwdTestConfig()
  git = GitIO(tcfg)
  main = AuditGitIOFoldersOpRefactor(git)
  main.run()