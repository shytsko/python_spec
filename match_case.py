cmd = "ghdggfh"

match cmd:
    case int() as c if 0 <= c <= 10:
        print(1)
    case str() as c if c.isdigit():
        print("digits str")
    case str():
        print("not digits str")
    case c:
        print(c)
