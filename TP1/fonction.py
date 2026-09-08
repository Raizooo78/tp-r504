def puiss(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("hell nah")
    return a ** b
