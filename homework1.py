'''for letter in "учиться":
    print(letter.upper())'''









'''
def vozrast(v):
    if v<7:
        return "в сад"
    if v<=17:
        return "в школу"
    if v<=22:
        return "в ВУЗ"
    return "пашет"
x=int(input()) 
print(vozrast(x))
'''

'''
def prosto(str1,str2):
    if not isinstance(str1,str) or  not isinstance (str2,str):
        return 0
    if (str1!=str2) and (str2=="Learn"):
        return 3
    if len(str1)==len(str2):
        return 1
    if len(str1)>len(str2):
        return 2
    return 4
print (prosto("Долгая ","rewgrhtrtreghtehrn"))'''


'''while True:
    user_say = input("Напиши:")
    if user_say != "Хорошо":
        print ("Как дела")
    if user_say == "Хорошо":
        break'''


        
'''spr={2,4,8,10,11,15,18,20,22,24}
x=0

for number in spr:
    print(number+1)'''


school=[{'class': '4a', 'scores': [3,4,4,5,2]},
{'class': '5a', 'scores': [2,5,4,5,2]},
{'class': '6a', 'scores': [4]}, 
{'class': '7a', 'scores': [2]}]

po_vseyshkole=0
skool_count=0
for class_ in school:
    po_klassu = 0
    for score in class_['scores']:
        po_vseyshkole += score
        po_klassu += score
        skool_count+=1
    try:
        y=(po_klassu/len(class_['scores']))

        
    except ZeroDivisionError:
        y = None
    
    
    print(y,class_['class'])

print(po_vseyshkole/(skool_count))
#все скопом оценки у поделить на количество всех оценок и проверить ошибку
#  на делние на ноль и переименовать переменные, вывод на экран средний балл- наименование класса




'''def ask_user(): # программа справочник - вопрос - ответ
    spr={"как дела": "хорошо!","что делаешь?":"программирую", "почему": "надо учиться"}
    x=input()
    
    if x in spr:
        print(spr[x])
    else:
        print('Я вас не понял')
  
def ask_user(): # программа справочник - вопрос - ответ
    spr={"как дела": "хорошо!","что делаешь?":"программирую", "почему": "надо учиться"}
    while True:
        x=input()
    
        if x in spr:
            print(spr[x])
        else:
            print('Я вас не понял')
   '''
    
    
'''def ask_user(): # программа справочник - вопрос - ответ
    spr={"как дела": "хорошо!","что делаешь?":"программирую", "почему": "надо учиться"}
    while True:
        try:
            x=input()
            print(spr[x])
        except KeyboardInterrupt:
            print('Пока')
            return
        except Exception:
            print('Я вас не понял')
          

ask_user()'''




