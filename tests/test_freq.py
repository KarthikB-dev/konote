from konote.freq import *

def test_read_json():
    in_dict = read_json()
    assert in_dict is not None


def test_write_json():
    write_to_json({"Finish konote": "TODO"})
    assert read_json() == {"Finish konote": "TODO"}


def test_edit_json():
    write_to_json({"Test edit": "May not work"})
    d = read_json()
    d["Test edit"] = "Works"
    write_to_json(d)
    assert read_json() == {"Test edit": "Works"}


def test_change_task_status():
    write_to_json({"Finish konote": None})
    d = read_json()
    d = todo_task(d, "Finish konote")
    assert d == {"Finish konote": "TODO"}
    d = in_progress_task(d, "Finish konote")
    assert d == {"Finish konote": "IN_PROGRESS"}
    d = complete_task(d, "Finish konote")
    assert d == {"Finish konote": "DONE"}
    d = todo_task(d, "Can this add new tasks")
    assert d == {"Finish konote": "DONE", "Can this add new tasks": "TODO"}
