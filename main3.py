# Напишите программу банкомат.

# ✔️ Начальная сумма равна нулю
# ✔️ Допустимые действия: пополнить, снять, выйти
# ✔️ Сумма пополнения и снятия кратны 50 у.е.
# ✔️ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔️ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔️ Нельзя снять больше, чем на счёте
# ✔️ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔️ Любое действие выводит сумму денег
# Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

def bancomat():
    balance = 0
    operation = 0
    list_operations = []

    while True:
        print("1. Пополнить")
        print("2. Снять")
        print("3. Показать историю операций")
        print("4. Выйти")
        choice = int(input("Выберите действие (1-3): "))

        if choice == 1:
            amount = int(input('Введите сумму пополнения: '))
            if amount % 50 == 0:
                balance += amount
                operation += 1
                if operation % 3 == 0:
                    bonus = balance * 0.03
                    balance += bonus
                if balance > 500000:
                    nalog = balance * 0.1
                    balance -= nalog
                list_operations.append(f'Пополнение: {round(amount, 2)}')
            else:
                print('Сумма пополнения должна быть кратна 50 у.е.')
        elif choice == 2:
            amount = int(input('Введите сумму снятия: '))
            if amount % 50 == 0:
                if balance >= amount:
                    balance -= amount
                    operation += 1
                    gaz = amount * 0.015
                    gaz = min(max(gaz, 30), 600)
                    balance -= gaz
                    if operation % 3 == 0:
                        bonus = balance * 0.03
                        balance += bonus
                    if balance > 500000:
                        nalog = balance * 0.1
                        balance -= nalog
                    list_operations.append(f'Пополнение: {round(amount, 2)}')
                else:
                    print('Недостаточно средств')
            else:
                print('Сумма снятия должна быть кратна 50 у.е.')
        elif choice == 3:
            print(list_operations)
        elif choice == 4:
            break

        print(f'Баланс: {balance} у.е.')

bancomat()