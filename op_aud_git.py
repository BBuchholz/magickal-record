from menus import LineOption
from gitio import GitIO

class AuditGitIOFoldersOp(LineOption):
  def __init__(self, git: GitIO):
    self.git = git

  def key(self):
    return "aud"
  
  def desc(self):
    return "Audit GitIO Folders"
  
  def run(self):
    repos = self.git.list_repos()
    repo_count = len(repos)
    if repo_count < 1:
      print("no repos found")
    else:
      print(f"found {repo_count} repos:")
      for repo in repos:
        print(f"CetER audit goes here for repo: {repo}")