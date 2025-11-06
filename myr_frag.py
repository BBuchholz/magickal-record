# Myriad Fragments are more than "Mere Frags"
# the class name is a play on words much like
# MyrFiles and MyrKis
class MyrFrag():
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

  def get_comment_lines(self):
    comment_lines = []
    for line in self.lines:
      if line.startswith("- "):
        comment_lines.append(line)
    return comment_lines