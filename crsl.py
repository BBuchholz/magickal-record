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
    lst_length = len(self.lst)
    last_index = lst_length - 1
    for i in range(lst_length):
      if current_item == self.lst[last_index]:
        return self.lst[0]
      if current_item == self.lst[i]:
        return self.lst[i+1]
    return None
  
  def get_previous(self, current_item=None):
    if len(self.lst) < 1:
      return None
    lst_length = len(self.lst)
    last_index = lst_length - 1
    if current_item is None:
      return self.lst[last_index]
    for i in range(lst_length):
      if current_item == self.lst[0]:
        return self.lst[last_index]
      if current_item == self.lst[i]:
        return self.lst[i-1]
    return None