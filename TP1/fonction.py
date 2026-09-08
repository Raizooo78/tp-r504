def puiss(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("hell nah")
    if a == 0 and b < 0:
        raise ValueError("pas poddible")
    if a == 0:
        return 0
    result = 1
    if b < 0:
        for i in range(-b):
            result *= a
        return 1 / result
    for i in range(b):
        result *= a
    return result

puissance = puiss
