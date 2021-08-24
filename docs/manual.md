# konote

Konote is designed to be a multipurpose productivity tool. It currently only supports task generation.

## Tasks

There are three main types of tasks - long term goals, projects, and quick todos.

The main purpose of these tasks is to log todos that do not have a due date.

### Long Term Goals

These are things like learning a new language, acquiring a new skill, or taking a course.

In the console, type `konote ltg <name of long term goal>` to add one to your list.

### Projects

These are the next level below.
It might be something like learning a specific grammar structure within the language, learning a certain skill, or completing a project within that course.

In the console, type `konote pr <name of long term goal>` to add one to your list.

### Quick Todos

These are things you can get done in less than an hour, like doing a problem set,
getting a workout done, or cleaning your room.

In the console, type `konote qt <name of long term goal>` to add one to your list.

### Viewing Tasks You Made

Go to your home directory, then a folder named `konote_files` and find a file called `Tasks.yaml`.

This file stores all the tasks you have made. You can edit it directly, and new tasks will be created

## Coming Features

### Frequency Based todos

Each tasks has a certain frequency associated with it.

For example you might brush your teeth twice a day, go for a walk once a day, and do bicep curls every other day.

If you do bicep curls once every two days, then the JSON file would list the task with a frequency of 2.

If you walk every day, then the JSON file would list the task with a frequency of 1.

The program stores an `init_date`, which is the date of when you first added that todo.

The number of days between the current date and the `init_date` are calculted, and modular arithmetic is
done on the value stored in the `freq` field for the todo. 

Eg. if you initialized the program `2021-08-04` and the current date was `2021-08-08` and the frequency of bicep curls was 2, then konote would find the number of days between these two days (which is 4 days), then take this value modulo 2, and get 0. Because the result is 0, you have to do bicep curls today.

Konote would be able to remind you of this.

#### __JSON Structure__

`todos`

* `task_name`
  * `frequency`
  * `init_date`

`freq_log`

* isoformat date
  * dictionary of tasks due on that date, and if they are IN_PROGRESS, DONE, or TODO

#### __Konote console input__

Konote will let you do this by having you enter `konote freq init`. The date that you entered this will be recorded.

To add new frequency based todos, you enter `konote freq add <name of task> <frequency of task>`

Certain tasks must be done weekly on a given day of the week. For example, you may need
to take your dog out for a walk every Monday, or take the trash out every Sunday. If this is the case, then the frequency listed
will not be an integer, but a given day of the week.

For example, for putting out the trash, we would have

* "Put the trash out":
  * `frequency`: "Sunday"
  * `init_date`: "2020-01-01"
