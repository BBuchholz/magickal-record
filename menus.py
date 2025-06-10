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

  def exit_after_selection(self):
    return False

  def print_options(self):
    print("")
    print("Current Options:")
    for op in self.get_ops():
      print(f"{op.key()} : {op.desc()}")

  def show_menu(self):
    self.op_found = None
    self.run_again = True
    while self.run_again:
      self.print_options()
      user_input = input("Enter option (type 'exit' to quit): ")
      if user_input.lower() == 'exit':
          self.run_again = False
          break  # Exit the loop if the user types 'exit'
      else:
          # Process the user input
          for op in self.get_ops():
            if str(user_input.lower()) == str(op.key()):
              self.op_found = op
          if self.op_found is not None:
            self.op_found.run()
            if self.exit_after_selection():
              self.run_again = False
          else:
            print(f"unrecognized input: {user_input}")

class SubMenu(LineOption, Menu):
  def run(self):
    self.show_menu()