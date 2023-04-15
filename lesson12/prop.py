class PropTest:
    def __init__(self, value, rate=1.0):
        self._value = value
        self.rate = rate

    @property
    def value(self):
        return self._value * self._rate

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, new_value):
        if 0 <= new_value <= 2.0:
            self._rate = new_value
        else:
            raise ValueError("rate must be between 0.0 and 2.0")

    @rate.deleter
    def rate(self):
        self.rate = 1.0

    def __str__(self):
        return f"{self._value}; {self._rate}"


if __name__ == '__main__':
    obj = PropTest(100, 0.5)
    print(obj)
    print(obj.value)
    obj.rate = 0.99
    print(obj.value)
    del obj.rate
    print(obj)
    print(obj.value)
