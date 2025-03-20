from files import get_lines_array, print_lines_array
from constants import EXISTANT_FILE, NONEXISTANT_FILE

print("this is the sandbox")
print("you can test ideas here... :)")
print("happy hacking!")

print("building function get_lines_array(file_name)")
existant_lines = get_lines_array(EXISTANT_FILE)
nonexistant_lines = get_lines_array(NONEXISTANT_FILE)

print_lines_array(EXISTANT_FILE, existant_lines)
print_lines_array(NONEXISTANT_FILE, nonexistant_lines)