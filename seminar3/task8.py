# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends = {
    "Гоша":
        {"фонарик", "телефон", "лодка", "спички", "спальный мешок", "рюкзак", "палатка", "удочка", "котелок", "пауэрбанк"},
    "Эдик":
        {"спички", "рюкзак", "топор", "свисток", "весло", "спальный мешок", "чайник", "радио", "телефон", "пауэрбанк"},
    "Арнольд":
        {"спальный мешок", "рюкзак", "телефон", "фонарик", "весло", "спички", "мангал", "нож", "удочка", "компас"}
}


def have_all(friends: dict) -> set[str]:
    have_all_things = set()
    for name, things in friends.items():
        if len(have_all_things) == 0:
            have_all_things |= things
        else:
            have_all_things &= things
    return have_all_things


def have_only_one(friends: dict) -> dict[str, set[str]]:
    have_only_one_things = {}
    for name, things in friends.items():
        have_only_this = set(things)
        for name_other, things_other in friends.items():
            if name_other != name:
                have_only_this -= things_other
        have_only_one_things[name] = have_only_this
    return have_only_one_things


def have_all_but_one(friends: dict) -> dict[str, set[str]]:
    have_all_but_one_things = {}
    for name, things in friends.items():
        have_all_other = set()
        for name_other, things_other in friends.items():
            if name_other != name:
                if len(have_all_other) == 0:
                    have_all_other |= things_other
                else:
                    have_all_other &= things_other
        have_all_but_one_things[name] = have_all_other - things
    return have_all_but_one_things


print(f"Предметы, которые есть у всех: {have_all(friends)}")
print(f"Предметы, которые есть только у одного: {have_only_one(friends)}")
print(f"Предметы, которые есть у всех, кроме одного: {have_all_but_one(friends)}")
