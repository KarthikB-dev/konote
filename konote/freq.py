from datetime import datetime, timedelta, date


def get_today():
    today = date.today()
    return today


def get_tmrw(today):
    tmrw = today + timedelta(days=1)
    return tmrw


def get_days_from_now(today, days_from_today):
    new_date = today + timedelta(days=days_from_today)
    return new_date


def days_between_dates(d1, d2):
    return (d2 - d1).days


def due_today(days_between, freq):
    return days_between % freq == 0


def main():
    today = get_today()
    five_days = get_days_from_now(today, 5)
    print(five_days)


if __name__ == "__main__":
    main()
