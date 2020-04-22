name = input('Введите Ваше имя: ').title()
monthly_salary = int(input('Введите заработную плату в месяц: '))
mortgage_percentage = int(input('Введите сколько процентов уходит на ипотеку: '))
percentage_on_life = int(input('Введите сколько процентов уходит на жизнь: '))
prize = int(input('Введите количество премий за год: '))

annual_salari = monthly_salary * 12
mortgage_age = annual_salari / 100 * mortgage_percentage
print(name + ',', 'на ипотеку вы потратили за год ', mortgage_age, 'рублей')
annual_expenses = annual_salari / 100 * percentage_on_life
accumulation = (2 * monthly_salary / 2) + (annual_salari - (annual_expenses + mortgage_age))
print(name + ',', 'Ваши  накопления за год ', accumulation, 'рублей')

