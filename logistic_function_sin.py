import sys
import math

import matplotlib.pyplot as plt

sys.setrecursionlimit(100)

def logistic(x,constant):

    x2 = constant * math.sin(x) * (1 - math.sin(x))
    if x2 >= 1:
        print ("all dead")
        data.append(x2)
        return data
    if x2<= 0:
        print ("all dead")
        data.append(x2)
        return data
    else:
        print (x2)
        data.append(x2)



    try:
        logistic(x2, constant)

    except:
        print ("run out of puff")
    return data[-1]



data = []

constant_in = input ("constant = ")
starting_value = input ("starting value = ")
data.append(float(starting_value))
value = logistic(float(starting_value),float(constant_in))
plt.plot(data, color=("red"))
plt.title(f"Constant =  {constant_in}")
if data[-1] <= 0:
    plt.text(len(data),0.5,"All dead")
if data [-1]>=1:
    plt.text(len(data)-1, 0.5, "All dead")
plt.ylim(0,1)
plt.show()
plt.close("Figure 1")


