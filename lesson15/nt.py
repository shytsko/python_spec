from collections import namedtuple
from datetime import datetime
import time

Data = namedtuple("Data", ["name", "age", "data123"])

d1 = Data("Чукча", 40, "fdgggeg")
print(f"{d1=}  |  {d1}")

print(type(Data))
print(type(d1))

print(d1.age)
