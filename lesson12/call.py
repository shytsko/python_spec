class MyFun:

    def __init__(self):
        pass

    def __call__(self, msg):
        return msg + "!!!"


if __name__ == '__main__':
    fun = MyFun()
    print(callable(fun))
    print(fun("Hello"))
