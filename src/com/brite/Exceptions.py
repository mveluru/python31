import time


def throwexception():
    try:
        return 1 / 0
    except Exception as e:
        return e


print(throwexception())


def throwexceptions():
    start = time.time()
    try:
        return 1 / 0
    except Exception as e:
      print(e.__cause__)
    finally:
        print(f"{time.time() - start}")

throwexceptions()
