import os

class CetER:
  def __init__(self):
    self._expected_cets = []
    self.load_expected_cets()

  def load_expected_cets(self):
    # hard coded for now
    # eventually should load from ChronIO
    self._expected_cets.append('LMS24')
    self._expected_cets.append('MBN24')
    # TODO: add the rest
  
  def get_expected_cets_list(self):
    return self._expected_cets

  def audit_repo(self, repo: dict):
    short_name = repo['short_name']
    rel_address = repo['rel_address']
    print(f"auditing repo with short name: {short_name}")
    print(f"verifying repo exists:")
    
    print("")
    print(f"CetER.audit_repo(repo) IMPLEMENTATION IN PROGRESS")
        
    