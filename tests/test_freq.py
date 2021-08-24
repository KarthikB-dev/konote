from konote.freq import *
from datetime import datetime, timedelta, date

# from icecream import ic


# def test_read_json():
#     in_dict = read_json()
#     assert in_dict is not None
#
#
# def test_write_json():
#     write_to_json({"Finish konote": "TODO"})
#     assert read_json() == {"Finish konote": "TODO"}
#
#
# def test_edit_json():
#     write_to_json({"Test edit": "May not work"})
#     d = read_json()
#     d["Test edit"] = "Works"
#     write_to_json(d)
#     assert read_json() == {"Test edit": "Works"}
#
#
# def test_change_task_status():
#     write_to_json({"Finish konote": None})
#     d = read_json()
#     d = todo_task(d, "Finish konote")
#     assert d == {"Finish konote": "TODO"}
#     d = in_progress_task(d, "Finish konote")
#     assert d == {"Finish konote": "IN_PROGRESS"}
#     d = complete_task(d, "Finish konote")
#     assert d == {"Finish konote": "DONE"}
#     d = todo_task(d, "Can this add new tasks")
#     assert d == {"Finish konote": "DONE", "Can this add new tasks": "TODO"}
#
#
# def test_get_max_date():
#     d1 = date.fromisoformat("2021-01-01")
#     d2 = date.fromisoformat("2021-11-01")
#     d3 = date.fromisoformat("2021-03-01")
#     date_list = [d1, d2, d3]
#     max_item = max(date_list)
#     min_item = min(date_list)
#     assert max_item.isoformat() == "2021-11-01"
#     assert min_item.isoformat() == "2021-01-01"


# def test_init_freq_dict():
#     init_freq_dict()


def test_add_all_dates():
    msg = add_all_dates()
    assert msg == "SUCCESSFUL_RUN" or "SUCCESS: ALL_DATES_ALREADY_PRESENT"


def test_add_task():
    freq_dict = add_task(read_json(), "bicep curls", 2)
    assert freq_dict["todos"]["bicep curls"] == {"frequency": 2, "init_date": get_today()}


def test_get_due_dates():
    five_day = get_due_dates(
        {"init_date": date.isoformat(date.today() - timedelta(days=25)), "frequency": 5}
    )
    for i in range(6):
        assert date.isoformat(date.today() - timedelta(days=i * 5)) in five_day


def test_due_today():
    # Test 1: With dates
    init_date = date.today() - timedelta(days=5)
    assert due_today(init_date, 5) == True
    # Test 2: With weekly todos
    init_date = "NO_DATE"
    freq = get_day_of_week(date.today())
    assert due_today(init_date, freq) == True
