from Pathlib import Path
import ujson

#returns the number of tabs found at the beginning of each line
def input_num_tabs(file_name):
    with open(file_name, 'r') as fin:
        lines = fin.read()
        print(lines)
        #TODO change this!
num_tabs = input_num_tabs(input.txt)
'''TODO complete input file processing
The desired functionality is to add one level of nesting
for every indent
for example, if we had the following:
Programming notes
    Algorithms
        Binary Search
        Sequential Search
    Data structures
        Collections
            Set
            ArrayList
            LinkedList
            Queue
        Maps
            HashMap
            TreeMap
We would have
"Programming notes": {
    "Algorithms": {
       "Binary Search",
       "Sequential Search"
    },
    "Data Structures": {
        "Collections":{
           "Set",
           "ArrayList",
           "LinkedList",
           "Queue"
        },
        "Maps"
        {
           "HashMap",
           TreeMap"
        }
    }
}

to be stored in a JSON.
'''
#TODO make notes have the desired dictionary structure
notes = {}
with open("notes.json", "w+") as fout:
    ujson.dump(notes, fout)
