def factorial (x):
    if x < 2:
        int = 1
    else:
        int= x * factorial(x-1)
    return int


for i in range (50):
    value = factorial(i)
    print (f"{i}!= ", value)