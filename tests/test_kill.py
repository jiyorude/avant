import sys, pytest

def kill(message: str = None, exit_code: int = 1):
        if exit_code not in [0, 1]:
            raise ValueError("ERR001: Termination of application only possible with exit code 0 or 1.")
        if message:
            print(message)
        sys.exit(exit_code)

def test_kill_invalid_code():
     with pytest.raises(ValueError):
          kill("Exiting without valid exit code", 2)

def test_kill_no_input():
     with pytest.raises(SystemExit) as e:
          kill()
          assert e.type == SystemExit
          assert e.value.code == 0

def test_kill_no_msg_invalid_number():
     with pytest.raises(ValueError):
          kill("", 3)

def test_kill_only_message():
     with pytest.raises(SystemExit) as e:
          kill("Exiting with only message")
          assert e.type == SystemExit
          assert e.value.code == 0

def test_kill_all_valid():
     with pytest.raises(SystemExit) as e:
          kill("Both message and code", 1)
          assert e.type == SystemExit
          assert e.value.code == 1

# 5 tests passed in 0.01s [100%]
