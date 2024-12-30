import pytest, sys, time

def wait(sec: float):
    if not float(sec) or sec < 0:
        sys.exit("ERR003: Cannot leave wait function empty or execute negative function call.")
    return time.sleep(sec)

def test_wait_negative():
    with pytest.raises(SystemExit) as e:
        wait(-1)
        assert str(e.value) == "ERR003: Cannot leave wait function empty or execute negative function call."

def test_wait_string():
    with pytest.raises(ValueError) as e:
        wait("Cat")
        assert str(e.value) == "ERR003: Cannot leave wait function empty or execute negative function call."

def test_wait_positive():
    try:
        wait(4)
    except SystemExit:
        pytest.fail("Function raised Sys.Exit!")

# 3 passed in 4.01s, had to change line 14 to ValueError and also implement a manual ValueError raise for wait function in Utilities.
