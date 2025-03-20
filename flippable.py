import os
from constants import OBSIDIAN_TEST_FOLDER

msg = "flippable feature audit"
print(msg)
path = os.path.expanduser(OBSIDIAN_TEST_FOLDER)
msg = "checking " + path + " for feature list"
print(msg)