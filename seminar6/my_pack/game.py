from random import randint

__all__ = ["guess_number", "riddles", "riddles_all", "view_result"]

def guess_number(lower_limit: int, upper_limit: int = 1000, attempt_available: int = 10) -> bool:
    secret_number = randint(lower_limit, upper_limit)
    attempts_left = attempt_available
    while attempts_left > 0:
        number = int(input(f"Отгадайте число от {lower_limit} до {upper_limit} (осталось попыток: {attempts_left}): "))
        if number == secret_number:
            return True
            break
        elif secret_number > number:
            print("Загадонное числое больше вашего.")
        else:
            print("Загадонное числое меньше вашего.")
        attempts_left -= 1
    else:
        return False


def riddles(text: str, correct_answers: list[str], attempt_available: int = 10) -> int:
    attempts_left = attempt_available
    print(f"Отгадайте загадку:\n{text}")
    while attempts_left > 0:
        answer = input(f"Ваш ответ (осталось попыток: {attempts_left}): ")
        if answer.lower() in correct_answers:
            return attempt_available - attempts_left + 1
            break
        attempts_left -= 1
    else:
        return 0


def riddles_all():
    riddles_dict = {
        "Зимой и летом одним цветом": ["елка", "ель", "елочка"],
        "Сто одежек и все без застежек": ["капуста"],
        "Падают с ветки золотые монетки": ["лист", "листья"]
    }

    for text, answers in riddles_dict.items():
        _registration_results(text, riddles(text, answers, 3))


_riddle_results: dict[str, int] = {}


def _registration_results(text: str, attempt_number: int):
    global _riddle_results
    _riddle_results[text] = attempt_number


def view_result():
    global _riddle_results
    return "\n".join(
        f"Загадка '{text}' отгадана с попытки {attempt_number}"
        if attempt_number > 0
        else
        f"Загадка '{text}' не отгадана"
        for text, attempt_number in _riddle_results.items())
