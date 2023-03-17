# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


s = "text"
users = ['user1', 'user2']
values = (0, 1, 2, 3)
text = "dndmjymhdgfb"
var = 10


def change_variables():
    variables = globals()

    variables_name_s = list(filter(lambda x: len(x) > 1 and x[-1] == 's', variables.keys()))

    for var_name in variables_name_s:
        variables[var_name[:-1:]] = variables[var_name]
        variables[var_name] = None


change_variables()
print(f"{s=}, {users=}, {user=}, {values=}, {value=}, {text=}, {var=}")
