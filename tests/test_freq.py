from konote.freq import *
from icecream import ic


def test_tmrw():
    today = date.today()
    ic(today)


def test_days_between_dates():
    d1 = date.fromisoformat("2020-01-01")
    d2 = date.fromisoformat("2020-01-31")
    days_between = days_between_dates(d1, d2)
    ic(days_between)
    assert days_between == 30


def main():
    test_tmrw()
    test_days_between_dates()


if __name__ == "__main__":
    main()
