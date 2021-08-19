from datetime import datetime, timedelta, date
from pathlib import Path
import ujson


def init_freq_dict():
    # initializes freq json
    json_path = Path.home() / "konote_files" / "freq.json"
    if not json_path.is_file():
        # NO_TASKS means that no tasks are due that day
        # NO_STATUS means that beacause there is no real task, it does not have a status
        init_dict = {
            "freq_log": {date.isoformat(date.today()): {"NO_TASKS": "NO_STATUS"}}
        }
        # the freq log:
        # Key: isoformat date
        # Value: another dictionary
        #           ⮩ Key: task due on that day
        #           ⮩ Value: whether the task is IN_PROGRESS, DONE, or TODO
        init_dict["todos"] = {}
        # todos:
        # Key: task_name (string)
        # Value: another dictionary
        #           ⮩ Key: 'frequency', Value: <integer giving frequency>
        #           ⮩ Key: 'init_date', Value: <isoformat date of when the todo was added>
        with open(json_path, "w") as fout:
            ujson.dump(init_dict, fout)


# TODO write function to add all dates up to this one
# make it look at the initial date, then fill in all the following ones


def add_task(freq_dict, task_name, freq, init_date):
    # TODO test this
    mod_dict = freq_dict.copy()
    if "NO_TASKS" in mod_dict:
        del freq_dict["NO_TASKS"]
    return {**freq_dict, task_name: {freq, init_date}}


def get_tmrw(today):
    return today + timedelta(days=1)


def get_days_from_now(today, days_from_today):
    return today + timedelta(days=days_from_today)


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
    return {**mod_dict, task_name: "DONE"}


def in_progress_task(task_dict, task_name):
    mod_dict = task_dict.copy()
    return {**mod_dict, task_name: "IN_PROGRESS"}


def todo_task(task_dict, task_name):
    mod_dict = task_dict.copy()
    return {**mod_dict, task_name: "TODO"}
