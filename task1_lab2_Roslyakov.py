# Начальные данные
reserve_fund = 20000      # Подушка безопасности
monthly_income = 5000     # Ежемесячная зарплата
expenses = 6000           # Траты за первый месяц
price_increase_rate = 0.05  # Ежемесячный рост цен

# Переменная для подсчета количества месяцев
months_without_debt = 0

# Цикл проверки, пока есть средства в подушке безопасности
while reserve_fund >= 0:
    # Обновляем подушку безопасности после учета доходов и расходов
    reserve_fund += monthly_income - expenses
    # Увеличиваем счетчик месяцев
    months_without_debt += 1
    # Увеличиваем траты на 5% для следующего месяца
    expenses *= (1 + price_increase_rate)

# Вывод результата
print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt - 1)





