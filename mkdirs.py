import os
from icecream import ic

new_dir_path = input("In what directory do you wish to store all your new dir? ")

def get_zero_num(int_num):
    str_num = str(int_num)
    length = len(str_num)
    switcher = {1: '000', 2: '00', 3: '0', 4: ''}
    return switcher.get(length) + str_num
    
#testing of the above function
ic(get_zero_num(9))
ic(get_zero_num(27))
ic(get_zero_num(987))

def create_dirs(num, dir_type, new_dir_path):
    #TODO switch to a chapter/chapter_section followed by a number, with 0 placeholder
    #eg. instead of AAC_chapter3_cell_biology -> 003_chapter3_cell_biology
    #17576 is the maxium supported chapter amount because 3 letters are used 
    #for ordering the chapters
    if num == 0:
        #nothing needs to be done
        return
    if num > 17576:
        print ("Error: Exceeds number of accepted directories. ")
        #createChapters(input("Please enter a valid number between 1 and 17576 inclusive."), 
        # dir_type)
        return
    #if an acceptable chapter or chapter section amount has been entered
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    #generate the appropriate set of chapters
    i = 1
    #l1 is for the first letter, l2 for the second, l3 for the third
    #example chapter name: ADC_Chapter_17_Cell_Biology
    #the letters at the start keep all the chapters listed in the proper order
    for l1 in letters:
        for l2 in letters:
            for l3 in letters:
                dirName = l1 + l2 + l3 + '_' + dir_type + str(i) + "_"
                dirDescription =  input("What is the description of " + 
                '_' + dir_type + '_' + str(i) + "? ")
                #deals with problems with escape characters
                dirDescription = dirDescription.replace(' ', '_')
                dirName = dirName + dirDescription
                #TODO implement some form of input handling
                os.system("mkdir " + new_dir_path + '/' + dirName)
                i += 1
                #If you've already made enough chapters or chapter sections
                if i > num:
                   return

#dir_type is 'chapter' or 'chapter_section' depending on the directory type needed
dir_type = ""
while dir_type != 'chapter' and dir_type != 'chapter_section':
    print("Do you want to make a chapter or chapter section? ")
    dir_type = input("Enter 'chapter' or 'chapter_section' ")

create_dirs(int(input("How many directories do you want to make? ")), dir_type, new_dir_path)
