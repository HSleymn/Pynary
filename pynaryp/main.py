
def binconv(x):
    value= x
    if value < 0:
        quotient = value  - 2*value
    else:
        quotient = value
    result = []
    while quotient != 0:
        reste = quotient % 2
        quotient = quotient // 2
        result.append(reste)
    result.reverse()
    b = ""
    for elt in result:
        a = str(elt)
        b = b +a
    b = int(b)
    if value < 0:
        return -b
    else:
        return b


