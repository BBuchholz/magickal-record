import re
from wxrd_type import WxrdType
# from wxrd import Wxrd

class WxrdTypeMyrFile(WxrdType):
  def __init__(self):
    super().__init__()
    self.wxrd_type_name = "MyrFile"

# Myriad Files are more than "mere files" :)
# the class name is a play on words
# much like MyrKis are more than "mere keys"
class MyrFile():
  def __init__(self):
    self.lines = []

  def __eq__(self, value):
    my_lines = self.get_lines()
    those_lines = value.get_lines()
    if len(my_lines) != len(those_lines):
      return False
    for i in range(len(my_lines)):
      if my_lines[i] != those_lines[i]:
        return False
    return True

  def get_wxrd_type(self) -> WxrdType:
    wtmf = WxrdTypeMyrFile()
    return wtmf

  def get_lines(self):
    return self.lines

  def load_from_lines_arr(self, lines):
    self.lines = [] # clear existing lines
    for line in lines:
      self.lines.append(line)

  def load_from_string_path(self, str_path):
    pass

  def get_main_text_lines(self):
    # NB: main text can be multiple lines, 
    # should be the first text, so starts 
    # with the first line, but can be broken 
    # up with commentary, which will start 
    # with a hyphen, thus it should be all 
    # lines, in order, that do not have a 
    # hyphen (comments) or an exclamation 
    # point (embedded images/sub files) at 
    # the beginning
    main_text_lines = []
    for line in self.lines:
      if not line.startswith("- "):
        if not line.startswith("!["):
          if not len(line.strip()) == 0:
            main_text_lines.append(line)
    return main_text_lines
  
  def get_comment_lines(self):
    comment_lines = []
    for line in self.lines:
      if line.startswith("- "):
        comment_lines.append(line)
    return comment_lines
  
  def get_wikilink_matches(self, wikitext):
    
    # Regex to find wikilinks. It captures the entire link within the double brackets.
    # It handles cases with and without custom link text (e.g., [[Page|link text]] and [[Page]]).
    # Explanation:
    # \[\[          - Matches the opening double brackets
    # (             - Start capturing group for the link target and optional text
    #   [^\[\]\|]+  - Matches one or more characters that are not [ , ], or | (this is the page name)
    #   (?:\|([^\[\]]+))? - Optionally matches a pipe and then captures the link text
    # )             - End capturing group
    # \]\]          - Matches the closing double brackets
    pattern = r"\[\[([^\[\]\|]+)(?:\|([^\[\]]+))?\]\]" 

    # Use re.findall() to get all matches
    wikilinks = re.findall(pattern, wikitext)
    sorted_links = []
    # Print the extracted links
    for link in wikilinks:
        page_name = link[0]
        link_text = link[1] if link[1] else page_name # If no link text, use the page name

        # print(f"Page Name: {page_name}, Link Text: {link_text}") 
        sorted_links.append(page_name)
    return sorted_links


  def get_wikilinks(self):
    wikilinks = []
    #TODO: implement and test (IN PROGRESS)
    # this was copied from AI and is not working yet, test and modify, 
    # maybe wikilink_rx.sub above is not the right thing to use
    
    ##### TESTING ####
    # print(f"lines: {self.lines}")
    for line in self.lines:
      all_matches = self.get_wikilink_matches(line)
      for each_match in all_matches:
        # print(f"Match: {each_match}")
        wikilinks.append(each_match)
    return wikilinks

  def get_embedded_lines(self, strip_embedding=False):
    embedded_lines = []
    for line in self.lines:
      if line.startswith("!["):
        if strip_embedding:
          processed_line = line.strip("![]")
          embedded_lines.append(processed_line)
        else:
          embedded_lines.append(line)
    return embedded_lines