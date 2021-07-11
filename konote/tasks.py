#!/usr/bin/env python3
# from pathlib import Path
import argparse

import yaml

# from icecream import ic

tasks = {}
args = None


def read_tasks():
    with open("Tasks.yaml", "r") as fin:
        global tasks
        tasks = yaml.safe_load(fin)


def task_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_type", help="qt for quick todo, pr for project, ltg for long term goal"
    )
    parser.add_argument("task_contents", help="What your task is about, in quotes")
    global args
    args = parser.parse_args()


def write_tasks():
    valid_task_types = ["qt", "pr", "ltg"]
    if args.task_type in valid_task_types:
        tasks[args.task_type].append(args.task_contents)
        with open("Tasks.yaml", "w") as fout:
            yaml.dump(tasks, fout)


def main():
    read_tasks()
    task_input()
    write_tasks()
    # ic(tasks)


if __name__ == "__main__":
    main()
