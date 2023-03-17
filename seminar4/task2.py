# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.


def func(text: str) -> list[int]:
    return sorted(list(set(map(ord, text))), reverse=True)


print(func(
    "вапыпвпыппshdfhfhdhdh"))
