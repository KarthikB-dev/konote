#!/usr/bin/env python3
# from pathlib import Path
import argparse

import yaml

# from icecream import ic
import copy


def read_tasks(tasks):
    # TODO store Tasks.yaml in home directory
    with open("Tasks.yaml", "r") as fin:
        tasks = yaml.safe_load(fin)
    # if the program has been run for the first time
    if tasks == None:
        tasks = {"qt": [], "pr": [], "ltg": []}
    return tasks


def task_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_type", help="qt for quick todo, pr for project, ltg for long term goal"
    )
    parser.add_argument("task_contents", help="What your task is about, in quotes")
    args = parser.parse_args()
    return args


def write_tasks(args, tasks):
    valid_task_types = ["qt", "pr", "ltg"]
    if args.task_type in valid_task_types:
        new_tasks = copy.deepcopy(tasks)
        new_tasks[args.task_type] = new_tasks[args.task_type] + [args.task_contents]
        with open("Tasks.yaml", "w") as fout:
            yaml.dump(new_tasks, fout)
    else:
        print("error: invalid task type")


def main():
    tasks = read_tasks({})
    args = task_input()
    write_tasks(args, tasks)


if __name__ == "__main__":
    main()
