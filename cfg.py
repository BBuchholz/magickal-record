import os

class Config():
  def __init__(self):
    self.nwd_folder = os.path.expanduser("~/nwd")

class TestConfig(Config):
  def __init__(self):
    self.nwd_folder = os.path.expanduser("~/nwd/test")