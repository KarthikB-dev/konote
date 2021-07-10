from pathlib import Path
import argparse
import yaml
# from icecream import ic

# import ujson

parser = argparse.ArgumentParser()
parser.add_argument(
    "note_type", type=int, help="1 for quick todo, 2 for project, 3 for long term goal"
)
parser.add_argument("note_contents", help="What your note is about")
args = parser.parse_args()
# ic(args)
# ic(args.note_type)
# = Path.home() / "Documents" / "konote_notes" / "notes.txt"


#
# with open("notes.json", "w+") as fout:
#     ujson.dump(notes, fout)
