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


def test_read_json():
    in_dict = read_json()
    ic(in_dict)
    return in_dict


def test_write_json():
    write_to_json({"hi": "bye"})
    assert test_read_json() == {"hi": "bye"}


def test_edit_json():
    d = read_json()
    d["hi"] = "bye bye"
    write_to_json(d)
    ic(read_json())


def main():
    test_tmrw()
    test_days_between_dates()
    test_read_json()
    test_edit_json()


if __name__ == "__main__":
    main()
