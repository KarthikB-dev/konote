from konote.freq import *


def test_days_between_dates():
    d1 = date.fromisoformat("2020-01-01")
    d2 = date.fromisoformat("2020-01-31")
    days_between = days_between_dates(d1, d2)
    assert days_between == 30


def test_read_json():
    in_dict = read_json()
    return in_dict


def test_write_json():
    write_to_json({"hi": "bye"})
    assert read_json() == {"hi": "bye"}


def test_edit_json():
    d = read_json()
    d["hi"] = "bye bye"
    write_to_json(d)
