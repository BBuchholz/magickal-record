class MyrCarousel:
  def __init__(self):
    self.lst = []

  def load_list(self, mi_name_list):
    for mi in mi_name_list:
      self.add_myrki_instance_name(mi)
  
  def add_myrki_instance_name(self, mi_name):
    if mi_name not in self.lst:
      self.lst.append(mi_name)

  def get_next(self, current_item=None):
    if len(self.lst) < 1:
      return None
    if current_item is None:
      return self.lst[0]
    return None