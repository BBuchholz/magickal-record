from abc import ABC, abstractmethod

class FileManager(ABC):
  @abstractmethod
  def select_file(self, file_name):
    pass