# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# +✔ Допустимые действия: пополнить, снять, выйти
# +✔ Сумма пополнения и снятия кратны 50 у.е.
# +✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
from decimal import Decimal

AMOUNT_MUL = Decimal(50)
WITHDRAWAL_FEE_RATE = Decimal(1.5 / 100)
WITHDRAWAL_FEE_MIN = Decimal(30)
WITHDRAWAL_FEE_MAX = Decimal(600)
BONUS_RATE = Decimal(3 / 100)
WEALTH_TAX_RATE = Decimal(10 / 100)
WEALTH_MIN = Decimal(5_000_000)

account_balance: Decimal = Decimal(0)
operation_counter: int = 0


def main():
    while True:
        cmd = menu()
        match cmd:
            case "0":
                show_balance()
                print("Выход")
                break
            case "1":
                check_wealth()
                if refill():
                    check_bonus()
            case "2":
                check_wealth()
                if withdraw():
                    check_bonus()
            case _:
                print("Команда не поддердивается")


def refill() -> bool:
    global account_balance
    print("Пополнение счета")
    amount = get_amount()
    if amount is not None:
        account_balance += amount
        print(f"Пополнение счета на сумму {amount:,.2f} выполнено успешно")
        show_balance()
        return True
    else:
        print("Операция отклонена: некорректная сумма")
        return False


def withdraw() -> bool:
    global account_balance
    print("Снятие со счет")
    amount = get_amount()
    if amount is not None:

        withdrawal_fee = round(amount * WITHDRAWAL_FEE_RATE, 2)
        if withdrawal_fee < WITHDRAWAL_FEE_MIN:
            withdrawal_fee = WITHDRAWAL_FEE_MIN
        elif withdrawal_fee > WITHDRAWAL_FEE_MAX:
            withdrawal_fee = WITHDRAWAL_FEE_MAX
        amount_total = amount + withdrawal_fee
        print(f"Комиссия за снятие: {withdrawal_fee:,.2f}. Общая сумма {amount_total:,.2f}")
        if amount_total <= account_balance:
            account_balance -= amount_total
            print(f"Со счета снято {amount_total:,.2f}")
            show_balance()
            return True
        else:
            print("Операция отклонена: не достаточно средств")
            return False
    else:
        print("Операция отклонена: некорректная сумма")
        return False


def check_bonus():
    global account_balance, operation_counter
    operation_counter += 1
    if operation_counter == 3:
        operation_counter = 0
        bonus: Decimal = round(account_balance * BONUS_RATE)
        account_balance += bonus
        print(f"Начислен бонус за третью операцию. Сумма бонуса {bonus}")
        show_balance()


def check_wealth():
    global account_balance
    if account_balance > WEALTH_MIN:
        amount_wealth_tax = round(account_balance * WEALTH_TAX_RATE, 2)
        account_balance -= amount_wealth_tax
        print(f"Списан налог на богатство {amount_wealth_tax}")
        show_balance()


def get_withdrawal_fee(amount: Decimal) -> Decimal:
    withdrawal_fee = round(amount * WITHDRAWAL_FEE_RATE, 2)
    if withdrawal_fee < WITHDRAWAL_FEE_MIN:
        withdrawal_fee = WITHDRAWAL_FEE_MIN
    if withdrawal_fee > WITHDRAWAL_FEE_MAX:
        withdrawal_fee = WITHDRAWAL_FEE_MAX
    return withdrawal_fee


def menu() -> str:
    return input("##################\nВыберите действие\n0 - Выйти\n1 - Пополнить\n2 - Снять\n> ")


def show_balance():
    print(f"Балланс счета: {account_balance:,.2f}")


def get_amount() -> Decimal:
    text = input(f"Введите сумму (должна быть кратна {AMOUNT_MUL}): ")
    if text.isdigit():
        amount = Decimal(text)
        if amount % AMOUNT_MUL == 0:
            return amount
    return None


if __name__ == "__main__":
    main()
