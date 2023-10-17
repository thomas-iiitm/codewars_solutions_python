# https://www.codewars.com/kata/517abf86da9663f1d2000003/python

def to_camel_case(text):
    temp = text.replace('-','_')
    temp = temp.split('_')
    res = []
    res.append(temp[0])
    for i in range(1,len(temp)):
        res.append(temp[i].capitalize())
    return ''.join(res)

def to_camel_case2(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')