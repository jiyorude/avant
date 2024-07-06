from avantlib import init, connect, mame, cre, htu, start
from avantutils import exception, ex

def run_avant():
    try:
        init()
        connect()
        while True:
            ch = mame()
            if ch == 1:
                if start():
                    continue
            elif ch == 2:
                if htu():
                    continue
            elif ch == 3:
                if cre():
                    continue
            else:
                ex()
                break
    except KeyboardInterrupt:
        ex()
    except Exception as err:
        exception(err, 5)
run_avant()