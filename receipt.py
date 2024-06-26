name = input()
c = int(input())
v = int(input())
money = int(input())
price = str(v) + "кг" + " * " + str(c) + "руб/кг"
result = str(c * v) + "руб"
get = str(money) + "руб"
getback = str(money - c * v) + "руб"
print("=" * 16, "Чек", "=" * 16, sep="")
print(f'Товар: {name:>28}') 
print(f'Цена: {price:>29}') 
print(f'Итого: {result:>28}') 
print(f'Внесено: {get:>26}') 
print(f'Сдача: {getback:>28}') 
print("=" * 35)