from Pathlib import Path

num_tabs = input_num_tabs(input.txt)
    #TODO complete input file processing
    notes = {}
    with open("notes.json", "w+") as fout:
        ujson.dump(note_json, fout)
