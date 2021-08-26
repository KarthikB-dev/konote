from datetime import datetime, timedelta, date
from pathlib import Path
import ujson
import argparse

# comment this out before commit
# from icecream import ic


def init_freq_dict():
    # initializes freq json
    json_path = Path.home() / "konote_files" / "freq.json"
    if not json_path.is_file():
        # NO_TASKS means that no tasks are due that day
        # NO_STATUS means that beacause there is no real task, it does not have a status
        init_dict = {"freq_log": {get_today(): {"NO_TASKS": "NO_STATUS"}}}
        # the freq log:
        # Key: isoformat date
        # Value: another dictionary
        #           ⮩ Key: task due on that day
        #           ⮩ Value: whether the task is IN_PROGRESS, DONE, or TODO
        # A frequency of -1 and NO_DATE are to show that these are not real tasks
        init_dict["todos"] = {"NO_TASKS": {"frequency": -1, "init_date": "NO_DATE"}}
        # todos:
        # Key: task_name (string)
        # Value: another dictionary
        #           ⮩ Key: 'frequency', Value: <integer giving frequency>
        #           ⮩ Key: 'init_date', Value: <isoformat date of when the todo was added>
        with open(json_path, "w") as fout:
            ujson.dump(init_dict, fout)


# make it look at the initial date, then fill in all the following ones
# It looks at all the init dates for the todos
# Out of these dates, it takes the earliest one, and stores it in early_date
# If dates have already been filled in, it sets the earliest date to
# The last date that was added
# It gets today's date
# It makes a list of all the dates between the earliest date and todays' date
def add_all_dates():
    freq_json = read_json()
    assert "ERROR" not in freq_json
    dates = freq_json["freq_log"].keys()
    # Handling potential errors
    error_msg = "ERROR: COULD NOT FIND FREQ JSON FILE"
    if dates == error_msg:
        return error_msg
    # if today's date is included, nothing needs to be done
    today = get_today()
    if dates is None:
        return "ERROR: DATES IS NONE"
    latest_date = max(dates)
    # If today has already been filled in, nothing needs to be done
    if today != latest_date:
        today_date_obj = date.fromisoformat(today)
        latest_date_obj = date.fromisoformat(latest_date)
        days_to_add = (today_date_obj - latest_date_obj).days
        if days_to_add < 0:
            return "ERROR: FUTURE DATES ADDED"
        for int_delta in range(1, days_to_add + 1):
            add_date = latest_date_obj + timedelta(days=int_delta)
            freq_json["freq_log"][add_date.isoformat()] = {"NO_TASKS": "NO_STATUS"}
    freq_json["freq_log"] = fill_in_todos(freq_json)
    write_to_json(freq_json)
    return "SUCCESSFUL_RUN"


def fill_in_todos(freq_dict):
    # iterate through the list of todos
    # for each todo, iterate through its due dates
    # the due dates are extracted are calculated using a function get_due_dates
    # if the todo has already been filled in for one of the dates, do not change that date
    # if the todo is absent, add it to that date's list of todos with its status set to TODO
    # TODO add support for days of the week
    mod_freq_log = freq_dict["freq_log"].copy()
    todo_dict = freq_dict["todos"]
    for curr_todo in todo_dict:
        due_dates = get_due_dates(todo_dict[curr_todo])
        if due_dates == "NO_DATES":
            return mod_freq_log
        for curr_date in due_dates:
            if not curr_todo in mod_freq_log[curr_date]:
                mod_freq_log[curr_todo] = "TODO"
    return mod_freq_log


# For a given task, get all the dates for which it must be completed (from init date to today)
def get_due_dates(task_dict):
    if task_dict["frequency"] == -1 or task_dict["init_date"] == "NO_DATE":
        return "NO_DATES"
    init_date_obj = date.fromisoformat(task_dict["init_date"])
    days_since_init = (date.today() - init_date_obj).days
    out_list = []
    for int_delta in range(0, days_since_init + 1, task_dict["frequency"]):
        out_list = out_list + [
            date.isoformat(init_date_obj + timedelta(days=int_delta))
        ]
    return out_list


def get_today():
    return date.isoformat(date.today())


def add_task(freq_dict, task_name, freq):
    mod_dict = freq_dict.copy()
    if "NO_TASKS" in mod_dict["todos"]:
        del mod_dict["todos"]["NO_TASKS"]
    mod_dict["todos"] = {task_name: {"frequency": freq, "init_date": get_today()}}
    return mod_dict


def task_input():
    # TODO: test this!
    parser = argparse.ArgumentParser()
    parser.add_argument("task_name", help="the name of the task you want to add")
    parser.add_argument(
        "frequency",
        help="How often you want to do the task. Supports entry for a day of the week",
    )
    return parser.parse_args()


def task_output():
    # TODO: test this!
    assert "ERROR" not in add_all_dates()
    args = task_input()
    freq_json = read_json()
    assert "ERROR" not in freq_json
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    freq = args.frequency
    if args.frequency not in days and args.frequency not in months:
        # If the frequency is not a day or month, it should be an int
        freq = int(freq)
    write_to_json(add_task(freq_json, args.task_name, freq))


def get_tmrw(today):
    return today + timedelta(days=1)


def get_days_from_now(today, days_from_today):
    return today + timedelta(days=days_from_today)


def due_today(init_date, freq):
    if type(freq) is str:
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        if freq in days:
            todays_day_of_week = get_day_of_week(date.today())
            return todays_day_of_week == freq
        elif freq in months:
            return due_this_month(freq)
    return (date.today() - init_date).days % freq == 0


def write_to_json(d):
    json_path = Path.home() / "konote_files" / "freq.json"
    try:
        with open(json_path, "w") as fout:
            ujson.dump(d, fout)
    except:
        return "ERROR: COULD NOT FIND FREQ JSON FILE"


def read_json():
    json_path = Path.home() / "konote_files" / "freq.json"
    try:
        with open(json_path, "r") as fout:
            return ujson.load(fout)
    except:
        return "ERROR: COULD NOT FIND FREQ JSON FILE"


def complete_task(task_dict, task_name):
    mod_dict = task_dict.copy()
    return {**mod_dict, task_name: "DONE"}


def in_progress_task(task_dict, task_name):
    mod_dict = task_dict.copy()
    return {**mod_dict, task_name: "IN_PROGRESS"}


def todo_task(task_dict, task_name):
    mod_dict = task_dict.copy()
    return {**mod_dict, task_name: "TODO"}


def get_day_of_week(date_obj):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    return days[date_obj.isoweekday() - 1]


def due_this_month(month):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    index = date.today().month - 1
    return month == months[index]


# prints out today's tasks
def todays_tasks():
    add_all_dates()
    json = read_json()
    assert "ERROR" not in json
    todays_tasks = json["freq_log"][get_today()]
    if "NO_TASKS" not in todays_tasks:
        for task in todays_tasks:
            status = todays_tasks[task]
            print(task + ": " + status)
    return todays_tasks
