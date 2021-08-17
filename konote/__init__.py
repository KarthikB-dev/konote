import argparse
import sys
from pathlib import Path
from konote.tasks import *
from datetime import datetime, timedelta, date
import ujson


# thank you to r2dev2 for this program
def main():
    print("Welcome to konote *hacker noises*")
    # initializes freq json
    json_path = Path.home() / "konote_files" / "freq.json"
    if not json_path.is_file():
        init_dict = {"init_date": date.isoformat(date.today())}
        init_dict["todos"] = None
        with open(json_path, "w") as fout:
            ujson.dump(init_dict, fout)
