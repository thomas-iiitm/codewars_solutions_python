#https://www.codewars.com/kata/54e6533c92449cc251001667/python

def unique_in_order(sequence):
    res = []
    prev_itm = 'DELIMITTER'
    for itm in list(sequence):
        if len(res) == 0:
            res.append(itm)
            prev_itm = itm
        else:
            if itm != prev_itm:
                res.append(itm)
                prev_itm = itm
    return res


def unique_in_order2(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
