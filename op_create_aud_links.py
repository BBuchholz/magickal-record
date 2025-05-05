from menus import (
  LineOption,
)
from obsidio import ObsidIO
from files import (
  write_lines,
  get_lines_from,
)

class CreateAuditLinkagesFile(LineOption):
  def __init__(self, obio: ObsidIO):
    self.obio = obio

  def key(self):
    return "gen"
  
  def desc(self):
    return "Generate Audit Linkages File"
  
  def run(self):
    as_file_path = self.obio._cfg.audit_summary_file()
    myrkis = get_lines_from(as_file_path)
    print("found myrkis in audit summary file: ")
    print(myrkis)
    fnames = self.obio.get_src_md_fnames_containing(myrkis)
    print("found fnames: ")
    print(fnames)
    linkages = self.obio.fnames_to_wikilinks(fnames)
    print("created linkages: ")
    print(linkages)
    al_file_path = self.obio.cfg.audit_linkages_file()
    write_lines(al_file_path, linkages, True)
    print(f"{len(myrkis)} lines written to: {al_file_path}")