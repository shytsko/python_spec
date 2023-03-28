# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.


def fun(nums_file_name, alias_file_name, result_file_name):
    with (
        open(nums_file_name, 'r', encoding='utf-8') as nums_f,
        open(alias_file_name, 'r', encoding='utf-8') as alias_f,
    ):
        numbers = [int(a) * float(b) for a, b in map(lambda x: x.split('|'), nums_f)]
        aliases = [a[:-1] for a in alias_f]

    with open(result_file_name, 'w', encoding='utf-8') as f:
        for i in range(max(len(aliases), len(numbers))):
            index_alias = i % len(aliases)
            index_num = i % len(numbers)
            if numbers[index_num] < 0:
                f.write(f"{aliases[index_alias].lower()}|{abs(numbers[index_num])}\n")
            elif numbers[index_num] > 0:
                f.write(f"{aliases[index_alias].upper()}|{round(numbers[index_num])}\n")


if __name__ == '__main__':
    fun("file1.txt", "alias.txt", "result.txt")
