money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital > 0:
    money_capital = money_capital + salary - spend
    if money_capital < 0:
        break
    spend = spend * (1 + increase)
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
