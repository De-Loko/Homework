Ticket = int(input('Введите количество билетов: '))
Age = [int(input('Введите возраст: ')) for i in range(Ticket)]
Price = 0
A = "Бесплатно"
B = 990
C = 1390
for a in range(len(Age)):
    if Age[a] < 18:
        print(A)
    elif 18 <= Age[a] < 25:
        print(B ,"руб.")
        Price = Price + B
    elif Age[a] >= 25:
        print(C ,"руб.")
        Price = Price + C
if Ticket <= 3:
    print("Цена: ", Price)
else:
    Discount = Price * 10 // 100
    print("Ваша скидка:" , Discount)
    print("Цена со скидкой:", Price - Discount)
