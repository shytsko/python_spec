# f = open("index.html", encoding="utf-8")
#
# print(*list(f))
#
# f.close()

# f = open("bit_file.bin", "wb")
# f.write("Привет, ".encode('utf-8') + "мир".encode('cp1251'))
# f.close()
#
# f = open("bit_file.bin", "rb")
# print(list(f))
# f.close()

# f = open("bit_file.bin", "r", encoding='utf-8')
# print(list(f))
# f.close()
#
# f = open("bit_file.bin", "r", encoding='utf-8', errors='replace')
# print(list(f))
# f.close()

# with (
#     open("index.html", "rt", encoding='utf-8') as f1,
#     open("bit_file.bin", "rb") as f2
# ):
#     print(*list(f1))
#     print(*list(f2))

with open("index.html", "r+", encoding='utf-8') as f:
    while res := f.readline():
        print("---------------")
        print(res)
        print(f.tell())

