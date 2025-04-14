from sabbat import Sabbat

class Chronomancer:
  def __init__(self):
    pass

  def get_sabbat(self, letter_code):
    match letter_code:
      case "LTH25":
        aliases = [
          "Litha",
        ]
        sbt = Sabbat("LTH", aliases, 2025)
        return sbt
