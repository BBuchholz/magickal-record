# Myriad Files are more than "mere files" :)
# the class name is a play on words
# much like MyrKis are more than "mere keys"
class MyrFile:
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

  def get_lines(self):
    return self.lines

  def load_from_lines_arr(self, lines):
    self.lines = [] # clear existing lines
    for line in lines:
      self.lines.append(line)

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

  def get_image_lines(self):
    image_lines = []
    for line in self.lines:
      if line.startswith("!["):
        image_lines.append(line)
    return image_lines