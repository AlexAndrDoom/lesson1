x=int(input())   
def vozrast(v):
    if v<7:
        return "в сад"
    if v<=17:
        return "в школу"
    if v<=22:
        return "в ВУЗ"
    return "пашет"
print (vozrast(x))