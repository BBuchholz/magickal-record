from menus import LineOption
from crsl_crtr import CarouselCreator

class ListMyrCarouselFilesOp(LineOption):
  def __init__(self, crtr: CarouselCreator):
    self.crtr = crtr

  def key(self):
    return "lst"
  
  def desc(self):
    return "List MyrCarousel Files"
  
  def run(self):
    files = self.crtr.get_input_files()
    file_count = len(files)
    if file_count < 1:
      print("no files found")
      print("files should begin with ")
      print("the 'CRSL - ' prefix and ")
      print("should consist of wikilink ")
      print("format lines with one myrki ")
      print("instance link per line, ")
      print("those links will become ")
      print("the anchors for the carousel")
    else:
      print(f"found {file_count} files:")
      for file in files:
        print(file)