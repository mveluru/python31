import time


def causesomeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1 / 0
    except ZeroDivisionError:
        print('Zero Division Error')
    except Exception:
        print("Oops Some thing is wrong")
    finally:
        print({time.time() - start}, 'Always executes')


causesomeError()
