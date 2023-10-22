money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
incr = spend
month = 0
while money_capital > 0:
    month+=1
    if month>=1:
        incr= incr + incr * increase
        money_capital = money_capital + salary - incr
    else:
        money_capital = money_capital + salary - incr

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month)
