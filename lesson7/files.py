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

# with open("index.html", "r+", encoding='utf-8') as f:
#     while res := f.readline():
#         print("---------------")
#         print(res)
#         print(f.tell())

# with open("index.html", "r+", encoding='utf-8') as f:
#     f_it = iter(f)
#     print(next(f_it), end="")
#     print(next(f_it), end="")
#     print(next(f_it), end="")
#     print(next(f_it), end="")
#     print(next(f_it), end="")
#     print(*f_it, sep="", end="")


import os
from pathlib import Path

# print(os.getcwd())
# print(Path.cwd())
# os.chdir("..")
# print(Path.cwd())
# os.chdir("lesson7")
# print(Path.cwd())
# os.mkdir("new_dir1")
# Path("new_dir2").mkdir()

# os.makedirs("os_mkdirs/1/2/4")
# Path("path_mkdirs/5/6/10").mkdir(parents=True)
# os.rmdir("os_mkdirs/1/2/4")
# os.rmdir("os_mkdirs/1/2/3")
# os.rmdir("os_mkdirs/1/2")
# os.rmdir("os_mkdirs/1")
#
# Path("path_mkdirs/5/6/10").rmdir()
# Path("path_mkdirs/5/6/7").rmdir()
# Path("path_mkdirs/5/6").rmdir()
# Path("path_mkdirs/5").rmdir()

import shutil

# Path(r"path_mkdirs\5\6\10").mkdir(parents=True)

# with open(r"path_mkdirs\5\6\10\file.txt", "w", encoding="utf-8") as f:
#     print("abracatabra\n", file=f)

# shutil.rmtree("path_mkdirs")

f1 = os.path.join(os.getcwd(), 'path_mkdir')
print(f1)

f2 = Path.cwd() / 'path_mkdir'
