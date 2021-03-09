import os

def createChapters(numChapters):
    if numChapters == 0:
        #nothing needs to be done
        return
    if numChapters > 17576:
        print ("Error: Exceeds number of accepted chapters. ")
        createChapters(input("Please enter a valid number between 1 and 17576 inclusive."))
    #if an acceptable chapter amount has been entered
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #generate the appropriate set of chapters
    i = 1
    chapterName = ""
    #l1 is for the first letter, l2 for the second, l3 for the third
    #example chapter name: ADC_Chapter_17_Networks  
    for l1 in letters:
        for l2 in letters:
            for l3 in letters:
                chapterName = l1 + l2 + l3 + "_Chapter_" + str(i) + "_"
                chapterDescription =  input("What is the description of chapter " + str(i) + "? ")
                #replaces all spaces with underscores to avoid problems with escape characters
                chapterDescription = chapterDescription.replace(' ', '_')
                chapterName = chapterName + chapterDescription
                #TODO implement some form of input handling
                os.system("mkdir " + chapterName)
                i += 1
                #If you've alreayd made enough chapters
                if i > numChapters:
                   return

createChapters(int(input("How many chapters do you want to make? ")))
#TODO add funtionality for creating chapter sections 
