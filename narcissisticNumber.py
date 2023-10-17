def narcissistic(num):
    temp = num
    res = []

    while (num // 10) > 0:
        res.append(num % 10)
        num = num // 10
    res.append(num)
    exp_val = len(res)

    sum = 0
    for elm in res:
        sum += (elm**exp_val)
    return True if sum == temp else False


def narcissistic2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))