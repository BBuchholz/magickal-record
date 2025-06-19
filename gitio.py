from cfg import Config
import os

class GitIO:
  def __init__(self, cfg: Config):
    self.repo_list = []
    self.cfg = cfg
    # self.add_repo("mdio/inbox", self.cfg.mdio_inbox_folder(False))
    self.load_cets_folder()

  def list_repos(self):
    return self.repo_list
  
  def load_cets_folder(self):
    c_fldr = self.cfg.cets_folder(False)
    full_c_path = os.path.expanduser(c_fldr)
    for entry in os.listdir(full_c_path):
      rel_path = os.path.join(c_fldr, entry)
      full_path = os.path.expanduser(rel_path)
      if os.path.isdir(full_path):
        self.add_repo(entry, rel_path)
  
  def add_repo(self, short_name, rel_address):
    if not rel_address.startswith("~/"):
      raise ValueError("repo addresses must be relative, ie. beginning with '~/someFolder'")
    repo = {
      "short_name": short_name,
      "rel_address": rel_address
    }
    if repo not in self.repo_list:
      self.repo_list.append(repo)