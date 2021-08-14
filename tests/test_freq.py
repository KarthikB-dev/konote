from konote.freq import *


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
