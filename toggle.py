import os

def hide_dir(dir_name):
    hide_name = '.' + dir_name
    os.system('mv ' + dir_name + hide_name)
def reveal_hidden():
    os.system('ls - a ')
def display_current_dir():
    os.system('tree $(pwd)')

#testing of the program
hide_dir(input("What is the name of the directory you want to hide? "))
display_current_dir()