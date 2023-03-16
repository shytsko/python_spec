# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


things = ["фонарик", "спички", "котелок", "топор", "нож", "компас"]


def get_permutations(sequence):
    """
    Получает все возможные перестановки элементов заданной последовантельности
    Источники:
    https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9D%D0%B0%D1%80%D0%B0%D0%B9%D0%B0%D0%BD%D1%8B
    https://prog-cpp.ru/permutation/
    :param sequence: исходная последовательность
    :return: список возможных перестановок
    """
    current_set = sorted(sequence)

    permutations = [current_set.copy()]
    end = False
    while not end:
        j = len(sequence) - 2
        while j != -1 and current_set[j] >= current_set[j + 1]:
            j -= 1
        if j != -1:
            k = len(sequence) - 1
            while current_set[j] >= current_set[k]:
                k -= 1
            current_set[j], current_set[k] = current_set[k], current_set[j]
            left = j + 1
            right = len(sequence) - 1
            while left < right:
                current_set[left], current_set[right] = current_set[right], current_set[left]
                left += 1
                right -= 1
            permutations.append(current_set.copy())
        else:
            end = True
    return permutations


permutations = get_permutations(things)

for p in permutations:
    print(p)

print(len(permutations))
