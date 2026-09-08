def puiss(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("hell nah")
    result = 1
    if b<0:
       for i in range(-b):
          result *= a 
       if a == 0 :
          raise ValueError("pas poddible")		
       else : return (1/result)
    for i in range(b):
       result *= a
    return (result)
