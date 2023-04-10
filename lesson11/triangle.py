class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def get_area(self):
        p = (self._a + self._b + self._c) / 2
        return (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5

    def __str__(self):
        return f"Треугольник со сторонами a={self._a}, b={self._b} c={self._c}"

    def __repr__(self):
        return f"Triangle({self._a}, {self._b}, {self._c})"

    def __eq__(self, other):
        return sorted((self._a, self._b, self._c)) == sorted((other._a, other._b, other._c))

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __hash__(self):
        return hash(tuple(sorted((self._a, self._b, self._c))))


if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(5, 3, 4)
    triangle3 = Triangle(6, 9, 4)
    triangle4 = Triangle(1, 1, 1)
    triangle5 = Triangle(3, 3, 3)

    print(triangle1, triangle3, sep="\n")
    print(f"{triangle1 == triangle2 = }")
    print(f"{triangle3 == triangle4 = }")
    print(f"{triangle3.get_area() = }")
    print(f"{triangle4.get_area() = }")
    print(f"{triangle3 < triangle4 = }")
    print(f"{triangle3 > triangle4 = }")
    print(hash(triangle1))

    tr_list = [triangle1, triangle2, triangle3, triangle4, triangle5]
    print(tr_list)
    tr_list.sort(reverse=True)
    print(tr_list)
    print(hash(triangle1))
    print(hash(triangle2))
