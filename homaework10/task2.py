# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

# Задача из семинара 2
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


class ATM:
    AMOUNT_MUL = Decimal(50)
    WITHDRAWAL_FEE_RATE = Decimal(1.5 / 100)
    WITHDRAWAL_FEE_MIN = Decimal(30)
    WITHDRAWAL_FEE_MAX = Decimal(600)
    BONUS_RATE = Decimal(3 / 100)
    WEALTH_TAX_RATE = Decimal(10 / 100)
    WEALTH_MIN = Decimal(5_000_000)

    class EventCounter:
        def __init__(self, threshold):
            self._threshold = threshold
            self._counter = 0

        def event(self):
            self._counter += 1
            if self._counter == self._threshold:
                self._counter = 0
                return True
            return False

    def __init__(self):
        self.__account_balance: Decimal = Decimal(0)
        self.__operation_counter = ATM.EventCounter(3)

    def run(self):
        while True:
            cmd = input("##################\nВыберите действие\n0 - Выйти\n1 - Пополнить\n2 - Снять\n> ")
            match cmd:
                case "0":
                    self.show_balance()
                    print("Выход")
                    break
                case "1":
                    self.check_wealth()
                    if self.refill():
                        self.check_bonus()
                case "2":
                    self.check_wealth()
                    if self.withdraw():
                        self.check_bonus()
                case _:
                    print("Команда не поддердивается")

    def show_balance(self):
        print(f"Балланс счета: {self.__account_balance:,.2f}")

    def get_amount(self) -> Decimal:
        text = input(f"Введите сумму (должна быть кратна {ATM.AMOUNT_MUL}): ")
        if text.isdigit():
            amount = Decimal(text)
            if amount % ATM.AMOUNT_MUL == 0:
                return amount
        return None

    def refill(self) -> bool:
        print("Пополнение счета")
        amount = self.get_amount()
        if amount is not None:
            self.__account_balance += amount
            print(f"Пополнение счета на сумму {amount:,.2f} выполнено успешно")
            self.show_balance()
            return True
        else:
            print("Операция отклонена: некорректная сумма")
            return False

    def withdraw(self) -> bool:
        print("Снятие со счет")
        amount = self.get_amount()
        if amount is not None:
            withdrawal_fee = round(amount * ATM.WITHDRAWAL_FEE_RATE, 2)
            if withdrawal_fee < ATM.WITHDRAWAL_FEE_MIN:
                withdrawal_fee = ATM.WITHDRAWAL_FEE_MIN
            elif withdrawal_fee > ATM.WITHDRAWAL_FEE_MAX:
                withdrawal_fee = ATM.WITHDRAWAL_FEE_MAX
            amount_total = amount + withdrawal_fee
            print(f"Комиссия за снятие: {withdrawal_fee:,.2f}. Общая сумма {amount_total:,.2f}")
            if amount_total <= self.__account_balance:
                self.__account_balance -= amount_total
                print(f"Со счета снято {amount_total:,.2f}")
                self.show_balance()
                return True
            else:
                print("Операция отклонена: не достаточно средств")
                return False
        else:
            print("Операция отклонена: некорректная сумма")
            return False

    def check_bonus(self):
        if self.__operation_counter.event():
            bonus: Decimal = Decimal(round(self.__account_balance * ATM.BONUS_RATE))
            self.__account_balance += bonus
            print(f"Начислен бонус за третью операцию. Сумма бонуса {bonus:,.2f}")
            self.show_balance()

    def check_wealth(self):
        if self.__account_balance > ATM.WEALTH_MIN:
            amount_wealth_tax = round(self.__account_balance * ATM.WEALTH_TAX_RATE, 2)
            self.__account_balance -= amount_wealth_tax
            print(f"Списан налог на богатство {amount_wealth_tax}")
            self.show_balance()

    def get_withdrawal_fee(self, amount: Decimal) -> Decimal:
        withdrawal_fee = round(amount * ATM.WITHDRAWAL_FEE_RATE, 2)
        if withdrawal_fee < ATM.WITHDRAWAL_FEE_MIN:
            withdrawal_fee = ATM.WITHDRAWAL_FEE_MIN
        if withdrawal_fee > ATM.WITHDRAWAL_FEE_MAX:
            withdrawal_fee = ATM.WITHDRAWAL_FEE_MAX
        return withdrawal_fee


if __name__ == '__main__':
    atm = ATM()
    atm.run()
