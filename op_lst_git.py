from menus import LineOption
from gitio import GitIO

class ListGitIOFoldersOp(LineOption):
  def __init__(self, git: GitIO):
    self.git = git

  def key(self):
    return "lst"
  
  def desc(self):
    return "List GitIO Folders"
  
  def run(self):
    repos = self.git.list_repos()
    repo_count = len(repos)
    if repo_count < 1:
      print("no repos found")
    else:
      print(f"found {repo_count} repos:")
      for repo in repos:
        print(repo)