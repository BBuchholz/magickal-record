import os
from constants import READ_FROM_FOLDER

msg = "flippable feature audit"
print(msg)
path = os.path.expanduser(READ_FROM_FOLDER)
msg = "checking " + path + " for feature list"
print(msg)