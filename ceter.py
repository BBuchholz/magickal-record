import os
from gitio import GitIO
from files import get_lines_from
from myr_file import MyrFile

def print_if_verbose(verbose, message):
  if verbose:
    print(message)

class CetER:
  def __init__(self, git: GitIO):
    self._expected_cets = []
    self.load_expected_cets()
    self.git = git

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
  
  def get_card_list_from(self, file_path, verbose):
    card_list = []
    lines_arr = get_lines_from(file_path)
    mf = MyrFile()
    mf.load_from_lines_arr(lines_arr)
    for embedded_value in mf.get_embedded_lines(True):
      print_if_verbose(verbose, f"found embedded value: {embedded_value}")
      card_list.append(embedded_value)
    return card_list

  def audit_repo(self, repo: dict, verbose=True):
    short_name = repo['short_name']
    rel_address = repo['rel_address']
    missing_elements = []
    print(f"auditing repo with short name: {short_name}")
    
    # existence
    print_if_verbose(verbose, f"verifying repo exists: {short_name}")
    full_path = os.path.expanduser(rel_address)
    if os.path.exists(full_path):
      print_if_verbose(verbose, f"path exists at: {full_path}")
      print_if_verbose(verbose, "")
    else:
      print_if_verbose(verbose, f"no path exists at: {full_path}")
      print_if_verbose(verbose, f"skipping repo: {short_name}")
      print_if_verbose(verbose, "")
      return # exit audit of this repo

    print_if_verbose(verbose, f"verifying repo {short_name} has git initialized:")
    if self.git.is_git_repo(full_path):
      print_if_verbose(verbose, f"found a .git subfolder in repo {short_name}, assuming git has been initialized")
    else:
      print_if_verbose(verbose, f"could not find a .git subfolder in repo {short_name}")
      missing_elements.append(f"double check that git has been initialized in directory: {full_path}")

    print_if_verbose(verbose, "")
    print_if_verbose(verbose, f"verifying repo {short_name} has a remote set:")
    if self.git.has_remote(full_path):
      print_if_verbose(verbose, f"found remote(s) for repo: {short_name}")
      for remote in self.git.get_remotes(full_path):
        print_if_verbose(verbose, f"remote: {remote}")
    else:
      missing_remote = f"no remotes found for repo: {short_name}"
      print_if_verbose(verbose, missing_remote)
      missing_elements.append(missing_remote)
    print_if_verbose(verbose, "")
    print_if_verbose(verbose, "Cet should have a README")
    readme_fname = "README.md"
    readme_fpath = os.path.join(full_path, readme_fname)
    if os.path.exists(readme_fpath):
      print_if_verbose(verbose, f"found README at: {readme_fpath}")
    else:
      missing_readme = f"expected README not found at: {readme_fpath}"
      print_if_verbose(verbose, missing_readme)
      missing_elements.append(missing_readme)
    print_if_verbose(verbose, "")
    print_if_verbose(verbose, "checking for card carousel index")
    index_fname = "index.html"
    index_fpath = os.path.join(full_path, index_fname)
    if os.path.exists(index_fpath):
      print_if_verbose(verbose, f"found index at: {index_fpath}")
    else:
      missing_index = f"expected index not found at: {index_fpath}"
      print_if_verbose(verbose, missing_index)
      missing_elements.append(missing_index)
    print_if_verbose(verbose, "")
    print_if_verbose(verbose, "Cet should have a cet list")
    cet_list_fname = short_name + ".md"
    cet_list_fpath = os.path.join(full_path, cet_list_fname)
    if os.path.exists(cet_list_fpath):
      print_if_verbose(verbose, f"found Cet List (CL) at: {cet_list_fpath}")
    else:
      missing_cl = f"expected Cet List (CL) not found at: {cet_list_fpath}"
      print_if_verbose(verbose, missing_cl)
      missing_elements.append(missing_cl)
    card_list = self.get_card_list_from(cet_list_fpath, verbose)
    for card in card_list:
      print_if_verbose(verbose, f"checking card carousel components: {card}")
      # image file
      image_fname = card + "_CARD.png"
      print_if_verbose(verbose, f"checking for image file: {image_fname}")
      image_fpath = os.path.join(full_path, image_fname)
      if os.path.exists(image_fpath):
        print_if_verbose(verbose, f"found Image Card File (ICF) at: {image_fpath}")
      else:
        missing_image = f"expected Image Card File (ICF) not found at: {image_fpath}"
        print_if_verbose(verbose, missing_image)
        missing_elements.append(missing_image)
      # html file
      html_fname = card + ".html"
      print_if_verbose(verbose, f"checking for html file: {html_fname}")
      html_fpath = os.path.join(full_path, html_fname)
      if os.path.exists(html_fpath):
        print_if_verbose(verbose, f"found html Card File (CF) at: {html_fpath}")
      else:
        missing_html = f"expected Card File (CF) not found at: {html_fpath}"
        print_if_verbose(verbose, missing_html)
        missing_elements.append(missing_html)
    print("")
    if len(missing_elements) > 0:
      print(f"Audit complete for repo {short_name}, missing elements: ")
      for missing_element in missing_elements:
        print(missing_element)
    else:
      print(f"Audit complete, no missing elements found for repo: {short_name}")

        
    