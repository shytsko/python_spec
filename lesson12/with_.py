from datetime import datetime


class Loger:
    def __init__(self, file_name):
        self._file_name = file_name
        self._file = None

    def __enter__(self):
        self._file = open(self._file_name, "a", encoding="UTF-8")
        self._file.write(f"Start loging at: {datetime.now()}\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.write(f"Stop loging at: {datetime.now()}\n")
            self._file.close()
            self._file = None

    def loging(self, msg):
        if self._file:
            self._file.write(f"{msg}\n")


if __name__ == '__main__':
    log = Loger("log.txt")
    with log as l:
        l.loging("dfhgdhfhf")
        l.loging("g,likkjjfhg")

    with log as l:
        l.loging("111111111111111111")
        l.loging("222222222222222")
