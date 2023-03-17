# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

MAX_WEIGHT = 10

things = {"фонарик": 1.0, "спички": 0.5, "котелок": 2.0, "топор": 1.0, "нож": 0.5, "компас": 0.5, "вода": 3.0,
          "лодка": 7.0, "палатка": 5.0, "еда": 2.0}


def get_all_set(things_set: dict[str, float], max_backpack_weight: float):
    things_list = list(enumerate(things_set.keys()))
    number_combinations = 2 ** len(things_list)
    valid_combinations = {}

    for comb in range(1, number_combinations):
        combination_bin = f"{bin(comb).replace('0b', ''):0>{len(things_list)}}"[::-1]
        current_set = frozenset({thing[1] for thing in things_list if combination_bin[thing[0]] == '1'})
        current_set_weight = sum([things_set[thing] for thing in current_set])
        if current_set_weight <= max_backpack_weight:
            valid_combinations[current_set] = current_set_weight

    return valid_combinations


def get_optimal_set_dynamic(things_set: dict[str, float], max_backpack_weight: float, weight_step: float) -> set[str]:
    """https://neerc.ifmo.ru/wiki/index.php?title=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BE_%D1%80%D1%8E%D0%BA%D0%B7%D0%B0%D0%BA%D0%B5#.D0.97.D0.B0.D0.B4.D0.B0.D1.87.D0.B0_.D0.BE_.D1.81.D1.83.D0.BC.D0.BC.D0.B0.D1.85_.D0.BF.D0.BE.D0.B4.D0.BC.D0.BD.D0.BE.D0.B6.D0.B5.D1.81.D1.82.D0.B2"""
    things_list = list(enumerate(things_set.keys(), start=1))
    weights_list = list(enumerate([i * weight_step for i in range(int(max_backpack_weight / weight_step) + 1)]))

    d = [[0] * len(weights_list)]
    for i, current_thing in things_list:
        d.append([])
        w_i = int(things_set[current_thing] / weight_step)
        for c, current_weight in weights_list:
            if c < w_i or d[i - 1][c] > d[i - 1][c - w_i] + w_i:
                d[i].append(d[i - 1][c])
            else:
                d[i].append(d[i - 1][c - w_i] + w_i)

    result_set = set()

    def restore_result_set(k, s):
        nonlocal result_set, d, things_list, things_set, weight_step
        if d[k][s] == 0:
            return
        if d[k - 1][s] == d[k][s]:
            restore_result_set(k - 1, s)
        else:
            w_k = int(things_set[things_list[k - 1][1]] / weight_step)
            restore_result_set(k - 1, s - w_k)
            result_set.add(things_list[k - 1][1])

    restore_result_set(len(things_list), len(weights_list) - 1)

    return result_set


combinations = get_all_set(things, MAX_WEIGHT)
print("Возможные варианты комплектования рюкзака:")
for combination, weight in combinations.items():
    print(f"{combination}: масса {weight}")

optimal_combinations = {combination: weight for combination, weight in combinations.items() if
                        weight == max(combinations.values())}

print("\n------------------\nОптимальные варианты комплектования рюкзака:")
for combination, weight in optimal_combinations.items():
    print(f"{combination}: масса {weight}")


print("\n------------------\nКомплектование рюкзака методом динамического программирования:")
print(get_optimal_set_dynamic(things, MAX_WEIGHT, 0.5))
