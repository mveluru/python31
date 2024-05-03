def handleException(func):
    def exceptionWrapper():
        try:
            func()
        except ZeroDivisionError:
            print('There was a zero division error')
        except Exception:
            print('Some Thing went wrong')
    return exceptionWrapper


@handleException
def causeSomeError():
    return 1 / 0


causeSomeError()
