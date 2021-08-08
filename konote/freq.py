from datetime import datetime, timedelta, date
import ujson


def get_tmrw(today):
    return today + timedelta(days=1)


def get_days_from_now(today, days_from_today):
    new_date = today + timedelta(days=days_from_today)
    return new_date


def days_between_dates(d1, d2):
    return (d2 - d1).days


def due_today(days_between, freq):
    return days_between % freq == 0


def write_to_json(d):
    with open("hi.json", "w") as fout:
        ujson.dump(d, fout)


def main():
    today = date.today()
    five_days = get_days_from_now(today, 5)
    print(five_days)


if __name__ == "__main__":
    main()
