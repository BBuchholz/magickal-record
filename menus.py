from abc import ABC, abstractmethod

class LineOption(ABC):
  @abstractmethod
  def key(self):
    pass

  @abstractmethod
  def desc(self):
    pass

  @abstractmethod
  def run(self):
    pass

class Menu(ABC):
  @abstractmethod
  def get_ops(self):
    pass

  def print_options(self):
    for op in self.get_ops():
      print(f"{op.key()} : {op.desc()}")

  def show_menu(self):
    while True:
      self.print_options()
      user_input = input("Enter option (type 'exit' to quit): ")
      if user_input.lower() == 'exit':
          break  # Exit the loop if the user types 'exit'
      else:
          # Process the user input
          op_found = None
          for op in self.get_ops():
            if user_input.lower() == op.key():
              op_found = op
          if op_found is not None:
            op_found.run()
          else:
            print(f"unrecognized input: {user_input}")

class SubMenu(LineOption, Menu):
  def run(self):
    self.show_menu()