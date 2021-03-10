import os

def create_dirs(num, dir_type):
    if num == 0:
        #nothing needs to be done
        return
    if num > 17576:
        print ("Error: Exceeds number of accepted directories. ")
        #createChapters(input("Please enter a valid number between 1 and 17576 inclusive."), dir_type)
        return
    #if an acceptable chapter amount has been entered
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #generate the appropriate set of chapters
    i = 1
    #l1 is for the first letter, l2 for the second, l3 for the third
    #example chapter name: ADC_Chapter_17_Cell_Biology
    for l1 in letters:
        for l2 in letters:
            for l3 in letters:
                dirName = l1 + l2 + l3 + '_'  + str(i) + "_"
                dirDescription =  input("What is the description of " + '_' + dir_type + '_' + str(i) + "? ")
                #replaces all spaces with underscores to avoid problems with escape characters
                dirDescription = dirDescription.replace(' ', '_')
                dirName = dirName + dirDescription
                #TODO implement some form of input handling
                os.system("mkdir " + dirName)
                i += 1
                #If you've already made enough chapters or chapter sections
                if i > num:
                   return

#dir_type is 'chapter' or 'chapter_section' depending on the directory type needed
dir_type = ""
while dir_type != 'chapter' and dir_type != 'chapter_section':
    print("Do you want to make a chapter or chapter section? ")
    dir_type = input("Enter 'chapter' or 'chapter_section' ")

create_dirs(int(input("How many chapters do you want to make? ")), dir_type)
