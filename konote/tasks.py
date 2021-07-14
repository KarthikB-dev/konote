#!/usr/bin/env python3
# from pathlib import Path
import argparse

import yaml

from icecream import ic
import copy
import pathlib
from pathlib import Path

# reads tasks from the yaml file
def read_tasks(tasks, task_path):
    with open(task_path, "r") as fin:
        tasks = yaml.safe_load(fin)
    # if the program has been run for the first time
    if tasks == None:
        tasks = {"qt": {}, "pr": {}, "ltg": {}}
    return tasks


# takes new task input from console
def task_input():
    # TODO add support for 'nested' tasks
    # add an optional argument that shows what task it must be added to
    # for example, you might have a task that says 'learn calculus',
    # which would have a subtask of learn integral calculus, which in turn
    # would have a subtask of learn to deal with exponents
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_type", help="qt for quick todo, pr for project, ltg for long term goal"
    )
    parser.add_argument("task_contents", help="What your task is about, in quotes")
    args = parser.parse_args()
    return args


# writes the tasks to the yaml file
def write_tasks(args, tasks, tasks_path):
    valid_task_types = ["qt", "pr", "ltg"]
    if args.task_type in valid_task_types:
        new_tasks = copy.deepcopy(tasks)
        new_tasks[args.task_type][args.task_contents] = None
        with open(tasks_path, "w") as fout:
            yaml.dump(new_tasks, fout)
    else:
        print("error: invalid task type")


# creates the folder to store tasks, if it does not exist
def make_yaml_path():
    tasks_path = Path.home() / "konote_files"
    yaml_path = tasks_path / "Tasks.yaml"
    already_made_dir = tasks_path.exists()
    if not already_made_dir:
        pathlib.Path(tasks_path).mkdir(exist_ok=False)
        create_file = open(yaml_path, "w+")
        create_file.close()
    return yaml_path


def main():
    yaml_path = make_yaml_path()
    tasks = read_tasks({}, yaml_path)
    ic(tasks)
    args = task_input()
    write_tasks(args, tasks, yaml_path)


if __name__ == "__main__":
    main()
