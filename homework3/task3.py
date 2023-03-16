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


combinations = get_all_set(things, MAX_WEIGHT)
print("Возможные варианты комплектования рюкзака:")
for combination, weight in combinations.items():
    print(f"{combination}: масса {weight}")

optimal_combinations = {combination: weight for combination, weight in combinations.items() if
                        weight == max(combinations.values())}

print("\n------------------\nОптимальные варианты комплектования рюкзака:")
for combination, weight in optimal_combinations.items():
    print(f"{combination}: масса {weight}")
