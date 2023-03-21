def event_counting(multiplicity):
    counter = 0
    while True:
        counter += 1
        counter %= multiplicity
        yield counter == 0


print(event_counting(4))

i = iter(event_counting, 10)
print(*i)

