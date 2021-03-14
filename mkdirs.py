import os
from icecream import ic

new_dir_path = input("In what directory do you wish to store all your new dir? ")
#this function gets a number with the remaining digits replaced with zeros
#for example, 27 becomes 0027
def get_zero_num(int_num):
    str_num = str(int_num)
    length = len(str_num)
    switcher = {1: '000', 2: '00', 3: '0', 4: ''}
    return switcher.get(length) + str_num
    
#testing of the above function
ic(get_zero_num(9))
ic(get_zero_num(27))
ic(get_zero_num(987))
ic(get_zero_num(3080))

#num is the number of new directories to be made
#dir_type is the type of directory, which can be book, chapter,
#or chapter section
#new_dir_path is the file path to the directory where these new subdirectories
#are to be made
desc = 'description.txt'
def create_dirs(num, dir_type, new_dir_path, i):
    #creates the description.txt file if required
    #The below if statement checks that you are adding the right type of directory
    #for example, if a directory contains a group of books, it would be illogical
    #to add a chapter section. If you try to do this, the program will exit
    if desc in os.listdir():
        with open(desc) as d:
            #checks if the new type matches the one in description.txt
            accepted_type = d.readlines()[1]
            #the accepted directory type is found on the second line of description.txt
            if accepted_type.rstrip(accepted_type[-1]) != dir_type:
                print("Error: incorrect type of directory")
                return
    else:
        os.system('echo Directory type: >> ' + desc)
        os.system('echo ' + dir_type + ' >> ' + desc)
    
    #9999 is the maxium supported chapter amount because 4 digits are used 
    if num == 0:
        #nothing needs to be done
        return
    if num > 9999:
        print ("Error: Exceeds number of accepted directories. ")
        #createChapters(input("Please enter a valid number between 1 and 9999 inclusive."), 
        # dir_type)
        return
    #if an acceptable chapter or chapter section amount has been entered
    num_to_make = num + i
    while i < num_to_make:
        dirName = dir_type + '_' + get_zero_num(i) + "_"
        dirDescription =  input("What is the description of " + 
        '_' + dir_type + '_' + str(i) + "? ")
        #deals with problems with escape characters
        dirDescription = dirDescription.replace(' ', '_')
        dirName = dirName + dirDescription
        #TODO implement some form of input handling
        os.system("mkdir " + new_dir_path + '/' + dirName)
        i += 1
    #stores the number of new directories made in desc
    os.system("echo 'number of dirs' >> " + desc)
    os.system("echo " + str(i - 1) + ' >> ' + desc)
#TODO test method below
def add_section(dir_type, section_description):
    if desc not in os.listdir():
        os.system('echo Directory type: >> ' + desc)
        os.system('echo ' + dir_type + ' >> ' + desc)
        os.system("echo 'number of dirs' >> " + desc)
        os.system("echo 1 >> " + desc)
        os.system("mkdir " + dir_type + "_0001_" + section_description)
    else:
        with open(desc) as d:
            #checks if the new type matches the one in description.txt
            lines = d.readlines()
            accepted_type = lines[1].rstrip(accepted_type[-1])
            if (dir_type != accepted_type):
                print("Error: Incorrec directory type")
                return
            zero_num = get_zero_num(int(lines[3]))
            os.system("mkdir " + dir_type + '_' + zero_num + '_' + section_description)
#dir_type is 'chapter' or 'chapter_section' depending on the directory type needed
dir_type = ""
while dir_type != 'chapter' and dir_type != 'chapter_section':
    print("Do you want to make a chapter or chapter section? ")
    dir_type = input("Enter 'chapter' or 'chapter_section' ")

#i is the starting number for the chapter. If you 
i = int(input("What is the starting number for the chapter or chapter section? "))
create_dirs(int(input("How many directories do you want to make? ")), dir_type, new_dir_path, i)
