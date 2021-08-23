from datetime import datetime, timedelta, date
from pathlib import Path
import ujson

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
    if today == latest_date:
        return "SUCCESS: ALL_DATES_ALREADY_PRESENT"
    today_date_obj = date.fromisoformat(today)
    latest_date_obj = date.fromisoformat(latest_date)
    days_to_add = (today_date_obj - latest_date_obj).days
    if days_to_add < 0:
        return "ERROR: FUTURE DATES ADDED"
    for int_delta in range(1, days_to_add + 1):
        add_date = latest_date_obj + timedelta(days=int_delta)
        freq_json["freq_log"][add_date.isoformat()] = {"NO_TASKS": "NO_STATUS"}
    freq_json["freq_log"] = fill_in_todos(freq_json["freq_log"])
    write_to_json(freq_json)
    return "SUCCESSFUL_RUN"


def fill_in_todos(freq_dict):
    # TODO: test this!
    # iterate through the list of todos
    # for each todo, iterate through its due dates
    # the due dates are extracted are calculated using a function get_due_dates
    # if the todo has already been filled in for one of the dates, do not change that date
    # if the todo is absent, add it to that date's list of todos with its status set to TODO
    mod_freq_log = freq_dict["freq_log"].copy()
    todo_dict = freq_dict["todos"]
    for curr_todo in todo_dict:
        due_dates = get_due_dates(todo_dict[curr_todo])
        for curr_date in due_dates:
            if not curr_todo in mod_freq_log[curr_date]:
                mod_freq_log[curr_todo] = "TODO"
    return mod_freq_log


# For a given task, get all the dates for which it must be completed (from init date to today)
def get_due_dates(task_dict):
    if task_dict["freq"] == -1 or task_dict["init_date"] == "NO_DATE":
        return "NO_DATES"
    init_date_obj = date.fromisoformat(task_dict["init_date"])
    days_since_init = (date.today() - init_date_obj).days
    out_list = []
    for int_delta in range(0, days_since_init + 1, task_dict["freq"]):
        out_list = out_list + [
            date.isoformat(init_date_obj + timedelta(days=int_delta))
        ]
    return out_list


def get_today():
    return date.isoformat(date.today())


def add_task(freq_dict, task_name, freq, init_date):
    mod_dict = freq_dict.copy()
    if "NO_TASKS" in mod_dict["todos"]:
        del mod_dict["todos"]["NO_TASKS"]
    mod_dict["todos"] = {task_name: {"frequency": freq, "init_date": init_date}}
    return mod_dict


def get_tmrw(today):
    return today + timedelta(days=1)


def get_days_from_now(today, days_from_today):
    return today + timedelta(days=days_from_today)


def due_today(init_date, curr_date, freq):
    # TODO: test this!
    if type(freq) is str:
        todays_day_of_week = get_day_of_week(date.today())
        return todays_day_of_week == freq
    return (curr_date - init_date).days % freq == 0


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
