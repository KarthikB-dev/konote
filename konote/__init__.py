import argparse
import sys
from pathlib import Path
from konote.tasks import *
from konote.freq import *
from datetime import datetime, timedelta, date
import ujson


# thank you to r2dev2 for this program
def main():
    print("Welcome to konote *hacker noises*")
    init_freq_dict()
