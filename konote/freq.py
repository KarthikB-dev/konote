from datetime import datetime, timedelta, date
from pathlib import Path
import ujson


def get_tmrw(today):
    return today + timedelta(days=1)


def get_days_from_now(today, days_from_today):
    new_date = today + timedelta(days=days_from_today)
    return new_date


def days_between_dates(d1, d2):
    return (d2 - d1).days


def due_today(init_date, curr_date, freq):
    return days_between_dates(init_date, curr_date) % freq == 0


def write_to_json(d):
    json_path = Path.home() / "konote_files" / "freq.json"
    with open(json_path, "w") as fout:
        ujson.dump(d, fout)


def read_json():
    json_path = Path.home() / "konote_files" / "freq.json"
    with open(json_path, "r") as fout:
        return ujson.load(fout)


def main():
    today = date.today()
    five_days = get_days_from_now(today, 5)
    write_to_json({"hi": "bye"})
    print(five_days)


if __name__ == "__main__":
    main()
