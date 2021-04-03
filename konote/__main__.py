import os
import ujson

def input_num_tabs(file_name):
    with open file_name as f:
        lines = f.readlines()
if __name__ == "__main__":
    num_tabs = input_num_tabs(input.txt)
    #TODO complete input file processing
    notes = {}
    with open("notes.json", "w+") as fout:
        ujson.dump(note_json, fout)
