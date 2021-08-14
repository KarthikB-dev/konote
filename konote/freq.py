from datetime import datetime, timedelta, date
from pathlib import Path
import ujson


def get_tmrw(today):
    return today + timedelta(days=1)


def get_days_from_now(today, days_from_today):
    new_date = today + timedelta(days=days_from_today)
    return new_date


def due_today(init_date, curr_date, freq):
    return (curr_date - init_date).days % freq == 0


def write_to_json(d):
    json_path = Path.home() / "konote_files" / "freq.json"
    with open(json_path, "w") as fout:
        ujson.dump(d, fout)


def read_json():
    json_path = Path.home() / "konote_files" / "freq.json"
    with open(json_path, "r") as fout:
        return ujson.load(fout)


def complete_task(task_dict, task_name):
    mod_dict = task_dict.copy()
    mod_dict[task_name] = "DONE"


def in_progress_task(task_dict, task_name):
    mod_dict = task_dict.copy()
    mod_dict[task_name] = "IN_PROGRESS"


def todo_task(task_dict, task_name):
    mod_dict = task_dict.copy()
    mod_dict[task_name] = "TODO"


def main():
    today = date.today()
    five_days = get_days_from_now(today, 5)
    write_to_json({"hi": "bye"})
    print(five_days)


if __name__ == "__main__":
    main()
