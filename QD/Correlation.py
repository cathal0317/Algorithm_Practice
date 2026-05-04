x = [0.01, 0.02, -0.01, 0.03]
y = [0.02, 0.01, -0.02, 0.04]

import math

def Corr_Return(x: list[float], y: list[float])-> list[float]:
    sum_x = sum(p for p in x)
    sum_y = sum(q for q in y)

    mean_x = sum_x / len(x)
    mean_y = sum_y / len(y)

    sum_x2 = sum(p * p for p in x)
    sum_y2 = sum(q * q for q in y)

    var_x = sum_x2 / len(x) - mean_x**2 
    var_y = sum_y2 / len(y) - mean_y**2 

    sum_xy = sum(p * q for p, q in zip(x,y))

    cor_xy = ((sum_xy/len(x)) - (mean_x * mean_y)) / ((math.sqrt(var_x)) * (math.sqrt(var_y)))

    return cor_xy

print(Corr_Return(x,y))