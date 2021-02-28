
'''
time elapse
'''


import time


class ShowResult():

    def __init__(self, _function):
        print("A __init__ start")
        self.function = _function
        print("A __init__ end")

    def __call__(self, *_function):
        print("A __call__ start")
        print("A Before Function")
        result = self.function(*_function)  # execute function
        print("A After Function")
        print("A The result is: {}".format(result))
        print("A __call__ end")
        return result

class TimeElapse():

    def __init__(self, _function):
        print("B __init__ start")
        self.function = _function
        print("B __init__ end")

    def __call__(self, *_function):
        print("B __call__ start")
        print("B Before Function")
        start_time = time.time()
        result = self.function(*_function)  # execute function
        print("B After Function")
        print("Time elapse {} s for input = {}".format(n, time.time()-start_time))
        print("B __call__ end")
        return result

@ShowResult # A
@TimeElapse # B
def fibonacci_number(_n):
    print("fibonacci_number start")
    if _n<=1: return _n
    first, second = 1, 1
    for i in range(2, _n):
        first, second = second, second+first
    print("fibonacci_number end")
    return second


if __name__ == '__main__':
    n = 100
    print(n, fibonacci_number(n))

    """
    TimeElapse __init__ start
    TimeElapse __init__ end
    TimeElapse __call__ start
    fibonacci_number start
    Time elapse 1 s for input = 3.504753112792969e-05
    TimeElapse __call__ end
    1 1

    """