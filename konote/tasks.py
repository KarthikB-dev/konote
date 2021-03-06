#!/usr/bin/env python3
# from pathlib import Path
import argparse
try:
    import ujson as json
except ImportError:
    import json

# from icecream import ic
import copy
import pathlib
from pathlib import Path
from typing import Iterable

# reads tasks from the yaml file
def read_tasks(task_path):
    tasks = None
    try:
        with open(task_path, "r") as fin:
            tasks = json.load(fin)
    except:
        pass
    # if the program has been run for the first time
    if tasks == None:
        tasks = {"qt": {}, "pr": {}, "ltg": {}}
    return tasks


# displays all tasks
def display_tasks(tasks, header_len):
    for category in tasks:
        print()
        print(category)
        print(header_len * "*")
        if isinstance(tasks[category], Iterable):
            for task in tasks[category]:
                print(task)
        else:
            print(tasks[category])


# takes new task input from console


def task_input():
    # TODO add support for 'nested' tasks
    # add an optional argument that shows what task it must be added to
    # for example, you might have a task that says 'learn calculus',
    # which would have a subtask of learn integral calculus, which in turn
    # would have a subtask of learn to deal with exponents
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_type",
        help="qt for quick todo, pr for project, ltg for long term goal, st for nested tasks",
    )
    parser.add_argument("task_contents", help="What your task is about, in quotes")
    args = parser.parse_args()
    return args


# checks if the task contents are reserved
def is_reserved_word(task):
    return task in ["__TODO", "__ANSWER"]


# writes the tasks to the yaml file
def write_tasks(args, tasks, kfiles_path):
    valid_task_types = ["qt", "pr", "ltg"]
    if args.task_type in valid_task_types:
        new_tasks = copy.deepcopy(tasks)
        if is_reserved_word(args.task_contents):
            print("Error: Invalid task name")
        else:
            new_tasks[args.task_type][args.task_contents] = None
            with open(kfiles_path, "w") as fout:
                json.dump(new_tasks, fout)
    else:
        # TODO add support for 'st' or subtask
        if args.task_type == "st":
            # The task needs to be add
            # as part of another task
            # what must be done is that
            # user input about which task they want
            # to change must be taken
            # display every existing task
            # TODO change this so that tasks are displayed, user input as to what task this one should be added to is taken
            display_tasks(tasks, 10)
            # TODO add support for 'st' or subtask

        else:
            print("error: invalid task type")


# creates the folder to store tasks, if it does not exist
def make_json_path():
    kfiles_path = Path.home() / "konote_files"
    json_path = kfiles_path / "Tasks.json"
    already_made_dir = kfiles_path.exists()
    pathlib.Path(kfiles_path).mkdir(exist_ok=True)
    json_path.touch()
    return json_path


def main():
    json_path = make_json_path()
    tasks = read_tasks(json_path)
    args = task_input()
    write_tasks(args, tasks, json_path)


if __name__ == "__main__":
    main()
