# TODO: create repo manager (GitIO) for 
# comparing md files between two or more repositories

class GitIO:
  def __init__(self):
    self.repo_list = []

  def list_repos(self):
    return self.repo_list
  
  def add_repo(self, short_name, rel_address):
    if not rel_address.startswith("~/"):
      raise ValueError("repo addresses must be relative, ie. beginning with '~/someFolder'")
    repo = {
      short_name: short_name,
      rel_address: rel_address
    }
    if repo not in self.repo_list:
      self.repo_list.append(repo)