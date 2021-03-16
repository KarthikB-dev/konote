import os
from pathlib import path
def hide_dir(dir_name):
    hide_name = '.' + dir_name
    os.system('mv ' + dir_name + hide_name)
def reveal_dir(dir_name):
    if dir_name[0] != '.':
        print("Dir not hidden")
        return
    reveal_dir_name = dir_name[1:]
    os.system('mv ' + dir_name + ' ' + reveal_dir_name)
def reveal_hidden():
    os.system('tree -a ')
def display_current_dir():
    os.system('tree $(pwd)')
#get_display_name removes the directory header
def get_display_name(name: str) -> str:
    if (name == 'description.txt'):
        return None
    return name[name.find('_') + 1:]
#testing get_display_name
print(get_display_name("cs0002_The_main_types_of_malware"))
print(get_display_name("description.txt"))

#testing of the program
#hide_dir(input("What is the name of the directory you want to hide? "))
#display_current_dir()
