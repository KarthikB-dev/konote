from pathlib import Path
import ujson

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
notes = dict()

def get_num_tabs(line):
    num_tabs = 0
    for char in line:
        if char == '\t':
            num_tabs += 1
        else:
            break
    return num_tabs

#checks that indentation is done correctly in the notes
def proper_format(lines):
    prev_num = get_num_tabs(lines[0])
    line_num = 0
    for line in lines:
        if get_num_tabs(line) > prev_num + 1:
            return "Incorrect formatting on line " + line_num
        prev_num = get_num_tabs(line)
        line_num += 1

notes_path = Path.home() / "Documents" / "konote_notes" / "notes.txt"
with open(notes_path, 'r') as fin:
    lines = fin.readlines()
    print(lines)
    for line in lines:


with open("notes.json", "w+") as fout:
    ujson.dump(notes, fout)
