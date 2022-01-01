import sys
sys.setrecursionlimit(9000)

def Ackerman (m,n):
    ans = 0
    if m == 0:
        ans = n+1
    elif n == 0:
        ans = Ackerman(m-1,1)
    else:
        ans = Ackerman (m-1,Ackerman(m,n-1))
    return ans


for count1 in range(5):
    for count2 in range (5):
        Value = Ackerman (count1,count2)
        print(f"m=1 {count1} n= {count2} Ackerman = ",Value)


