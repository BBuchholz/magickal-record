import os

class CetER:
  def __init__(self):
    self._expected_cets = []
    self.load_expected_cets()

  def compare_repos_to_expected(self, repos: list):
    expected_cets = self.get_expected_cets_list()
    expected_count = len(expected_cets)
    print(f"expected cets: {expected_count}")
    for expected_cet in expected_cets:
      print(f"expected cet: {expected_cet}")
    print("")
    print(f"comparing found cets to expected cets")
    found_expected_repos = []
    for repo in repos:
      short_name = repo['short_name']
      if short_name in expected_cets:
        print(f"expected repo found: {short_name}")
        found_expected_repos.append(short_name)
      else:
        print(f"unexpected repo found: {short_name}")
    for cet in expected_cets:
      if cet not in found_expected_repos:
        print(f"could not find cet: {cet}")
    print("")
    

  def load_expected_cets(self):
    # hard coded for now
    # eventually should load from ChronIO
    self._expected_cets.append('LMS24')
    self._expected_cets.append('MBN24')
    self._expected_cets.append('LMS25')
    # TODO: add the rest
  
  def get_expected_cets_list(self):
    return self._expected_cets
  
  def get_card_list_from(self, file_name):
    card_list = []
    # TODO: implement get card_list_from(file_name)
    card_list.append("TMPLT-LMS24")
    return card_list

  def audit_repo(self, repo: dict):
    short_name = repo['short_name']
    rel_address = repo['rel_address']
    print(f"auditing repo with short name: {short_name}")
    
    # existence
    print(f"verifying repo exists: {short_name}")
    full_path = os.path.expanduser(rel_address)
    if os.path.exists(full_path):
      print(f"path exists at: {full_path}")
      print("")
    else:
      print(f"no path exists at: {full_path}")
      print(f"skipping repo: {short_name}")
      print("")
      return # exit audit of this repo

    print(f"verifying repo {short_name} has git initialized:")
    print("git verification not yet implemented, skipping")
    print("")
    print(f"verifying repo {short_name} has a remote set:")
    print("git remote verification not yet implemented, skipping")
    print("")
    print(f"CetER.audit_repo(repo) IMPLEMENTATION IN PROGRESS")
    print("Cet should have a README")
    readme_fname = "README.md"
    print("Cet should have a cet list")
    cet_list_fname = short_name + ".md"
    print("checking for card carousel index")
    card_list = self.get_card_list_from(cet_list_fname)
    for card in card_list:
      print(f"checking card carousel components: {card}")
      print("checking for image")
      html_fname = card + ".html"
      print(f"checking for html file: {html_fname}")

        
    