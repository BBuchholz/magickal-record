from cfg import Config

class GitIO:
  def __init__(self, cfg: Config):
    self.repo_list = []
    self.cfg = cfg
    self.add_repo("mdio/inbox", self.cfg.mdio_inbox_folder(False))

  def list_repos(self):
    return self.repo_list
  
  def add_repo(self, short_name, rel_address):
    if not rel_address.startswith("~/"):
      raise ValueError("repo addresses must be relative, ie. beginning with '~/someFolder'")
    repo = {
      "short_name": short_name,
      "rel_address": rel_address
    }
    if repo not in self.repo_list:
      self.repo_list.append(repo)