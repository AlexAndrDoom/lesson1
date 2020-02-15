def get_summ(one,two, delimiter='&'):
    return str(one)+delimiter+str(two)

s = get_summ('Learn','python', delimiter='++')
s2 = get_summ('Learn','python', delimiter='&')
print(s,s2)