from sabbat import Sabbat
from constants_sabbats import (
  LTH_ALIASES,
  BEL_ALIASES,
  LMS_ALIASES,
  MBN_ALIASES,
  SMH_ALIASES,
  YUL_ALIASES,
  IMB_ALIASES,
  OST_ALIASES,
)

class Chronomancer:
  def __init__(self):
    pass

  def get_sabbat(self, letter_code):
    match letter_code:
      case "BEL25":
        aliases = BEL_ALIASES
        sbt = Sabbat("BEL", aliases, 2025)
        return sbt
      case "LTH25":
        aliases = LTH_ALIASES
        sbt = Sabbat("LTH", aliases, 2025)
        return sbt
      case "LMS25":
        aliases = LMS_ALIASES
        sbt = Sabbat("LMS", aliases, 2025)
        return sbt
      case "MBN25":
        aliases = MBN_ALIASES
        sbt = Sabbat("MBN", aliases, 2025)
        return sbt
      case "SMH25":
        aliases = SMH_ALIASES
        sbt = Sabbat("SMH", aliases, 2025)
        return sbt
      case "YUL25":
        aliases = YUL_ALIASES
        sbt = Sabbat("YUL", aliases, 2025)
        return sbt
      case "IMB26":
        aliases = IMB_ALIASES
        sbt = Sabbat("IMB", aliases, 2026)
        return sbt
      case "OST26":
        aliases = OST_ALIASES
        sbt = Sabbat("OST", aliases, 2026)
        return sbt
      case "BEL26":
        aliases = BEL_ALIASES
        sbt = Sabbat("BEL", aliases, 2026)
        return sbt
      case "LTH26":
        aliases = LTH_ALIASES
        sbt = Sabbat("LTH", aliases, 2026)
        return sbt
      case "LMS26":
        aliases = LMS_ALIASES
        sbt = Sabbat("LMS", aliases, 2026)
        return sbt
      case "MBN26":
        aliases = MBN_ALIASES
        sbt = Sabbat("MBN", aliases, 2026)
        return sbt
      case "SMH26":
        aliases = SMH_ALIASES
        sbt = Sabbat("SMH", aliases, 2026)
        return sbt
      case "YUL26":
        aliases = YUL_ALIASES
        sbt = Sabbat("YUL", aliases, 2026)
        return sbt
      
