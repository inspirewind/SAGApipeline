import time

class timer:
    def __init__(self) -> None:
        pass

    def timeit(method):
        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            print('methed: {0}, time: {1}f sec'.format(method.__name__, te - ts))
            return result
        return timed

        