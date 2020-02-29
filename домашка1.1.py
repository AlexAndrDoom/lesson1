'''b = 10098
p = 200
x=(b-p)
print(x)
if b > p:
    
    print('Спасибо за покупку:'+"x")
else:
    print('Пожалуйста, пополните баланс!')'''



'''def weather(temperature):
    if  0 > temperature>=-10:
        return 'На улице холодно!'
    elif -10 >= temperature <= -15:
        return 'На улице Очень ХОЛОДНО'
    elif 0 <= temperature <= 15:
        return 'На улице прохладно'
    elif 15 <= temperature <= 25:
        return 'На улице тепло'
    else:
        return 'На улице жарко'
print(weather(-9))'''

'''def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)'''

'''def discounted(price, discount, max_discount=20, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower():
        return price
    else:
        return price - (price * discount / 100)
dis_iphone = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
print(dis_iphone)
65432.1'''

'''
import random
def cat_ce(ludi): #программа про пирог 
    try:
        parts=1/ludi
        print(f"каждый получит{parts}")
    except ZeroDivisionError:
        print("Хрена вам лысого")
    except TypeError  :
        print ("Нафиг строку")
while True:
    p=random.randint(1,10)
    cat_ce(p)'''
    
       
'''for number in range(5):
    print(f"мир привет{number}!")

for letter in "phyton":
    print(letter.upper())'''

'''example_string = "Мне изучать язык Питон"
for word in example_string.split():
    print(f"Длина слова {word}: {len(word)}")

    print(len(word))
    a=int(len(word))
   
   # КАК МНЕ ПОСЧИТАТЬ СУММУ ВСЕХ БУКВ'''


stock = [{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25},
		{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}]
        from lesson_if import discounted
			
for phone in stock:
		phone["price_final"] = discounted(phone["price"], phone["discount"], name=phone["name"])
		
print(stock)
