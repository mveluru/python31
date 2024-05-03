def handleException(func):
    def exceptionWrapper():
        try:
            func()
        except ZeroDivisionError:
            print('There was a zero division error')
    return exceptionWrapper


@handleException
def causeSomeError():
    return 1 / 0


causeSomeError()
