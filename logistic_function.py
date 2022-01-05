import sys

import matplotlib.pyplot as plt

sys.setrecursionlimit(100) # sets the number of iterations before an error is called

def logistic(x,constant):

    x2 = constant * x * (1 - x)
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
        print ("run out of puff") # we run to for the total amount of iterations set
    return data[-1]

# programme starts here
data = []

constant_in = input ("constant, between 0 and 4 = ")
start_value = input ("Start value between 0 and 1  = ")
data.append(float(start_value)
value = logistic(float(start_value),float(constant_in))
plt.plot(data, color=("red"))
plt.title(f"Constant =  {constant_in}, Starting value = {start_value}")
if data[-1] <= 0:
    plt.text(len(data),0.5,"All dead")
if data [-1]>=1:
    plt.text(len(data)-1, 0.5, "All dead")
plt.ylim(0,1)
plt.show()



