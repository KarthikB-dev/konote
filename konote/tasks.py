#!/usr/bin/env python3
# from pathlib import Path
import argparse

import yaml

# from icecream import ic


def read_tasks(tasks):
    # TODO store Tasks.yaml in home directory
    with open("Tasks.yaml", "r") as fin:
        tasks = yaml.safe_load(fin)
    return tasks


def task_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_type", help="qt for quick todo, pr for project, ltg for long term goal"
    )
    parser.add_argument("task_contents", help="What your task is about, in quotes")
    global args
    args = parser.parse_args()
    return args


def write_tasks():
    valid_task_types = ["qt", "pr", "ltg"]
    if args.task_type in valid_task_types:
        tasks[args.task_type].append(args.task_contents)
        with open("Tasks.yaml", "w") as fout:
            yaml.dump(tasks, fout)
    else:
        print("error: invalid task type")


def main():
    tasks = {}
    tasks = read_tasks(tasks)
    args = task_input()
    write_tasks(args)
    # ic(tasks)


if __name__ == "__main__":
    main()
