import os

def hide_dir(dir_name):
    hide_name = '.' + dir_name
    os.system('mv ' dir_name + hide_name)

