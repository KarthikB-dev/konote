#!/usr/bin/env python3
from pathlib import Path
import argparse

# import yaml

# from icecream import ic

# import ujson
notes = {}

parser = argparse.ArgumentParser()
parser.add_argument(
    "note_type", help="qt for quick todo, p for project, ltg for long term goal"
)
parser.add_argument("note_contents", help="What your note is about, in quotes")
args = parser.parse_args()

notes[args.note_type] = {args.note_contents}
# ic(notes)
# = Path.home() / "Documents" / "konote_notes" / "notes.txt"


#
# with open("notes.json", "w+") as fout:
#     ujson.dump(notes, fout)
