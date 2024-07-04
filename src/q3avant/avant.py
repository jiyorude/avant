from avantlib import init, connect, exception, mame, cre, ex, htu, start

def exec():
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
exec()