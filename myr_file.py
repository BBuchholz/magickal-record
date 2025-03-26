class MyrFile:
  def __init__(self):
    self.lines = []

  def get_lines(self):
    return self.lines

  def load_from_lines_arr(self, lines):
    self.lines = [] # clear existing lines
    for line in lines:
      self.lines.append(line)