class MyIteraror:
    def __init__(self, *args):
        self._data = args
        pass

    def __iter__(self):
        return iter(self._data)

class Fibonacci:
    def __init__(self, l_bound, u_bound=None):
        if u_bound:
            self._l_bound = l_bound
            self._u_bound = u_bound
        else:
            self._l_bound = 0
            self._u_bound = l_bound
        self._cur = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self._cur <= self._u_bound:
            self._cur, self._next = self._next, self._next + self._cur
            if self._l_bound <= self._cur <= self._u_bound:
                return self._cur
        raise StopIteration


if __name__ == '__main__':
    # it_ = MyIteraror(1, 2, 3, 6, 47, "fghjg")
    # print(*it_)

    fib = Fibonacci(100)
    print(*fib)
