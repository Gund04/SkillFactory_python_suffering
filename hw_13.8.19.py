#Создаем перменные и присваиваем им значения
TICKET_PRICE = 1390  #базовая цена билета
DISCOUNT_THRESHOLD = 3  #количество билетов от которого начинается скидка
DISCOUNT_RATE = 0.9    # процент скидки, 10 процентов=сумма*0.9
#запрашиваем количество билетов
num_tickets = int(input("Сколько билетов вы хотите приобрести? "))
#запускаем цикл со счетчиком
total_price = 0
for i in range(num_tickets):
#в каждой итерации цикла запрашиваем возраст, с помощью elif  выбираем цену
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        price = 0
    elif age < 25:
        price = 990
    else:
        price = TICKET_PRICE
#прибавляем полученную цену
    total_price += price
#сверяем количество билетов с нужным для скидки, если оно больше или равно заданному значению-применям скидку.
if num_tickets >= DISCOUNT_THRESHOLD:
    discount = total_price * DISCOUNT_RATE
    total_price = discount
#отображаем итоговый результат
print(f"Сумма к оплате: {total_price} руб.")