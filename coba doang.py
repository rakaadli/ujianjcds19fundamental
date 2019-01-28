num1 = int(input('ketikan bilangan pertama:'))
num2 = int(input('kerikan bilangan kedua'))

def hitungKPK(a,b):
    x = 1
    y = 1
    p = a*x
    q = b*y
    while p!= q:
        while p>q:
            y = y+1
            q = b*y
        while p<q:
            x = x+1
            p = a*x
    if p==q:
        print (p)






def hitungFPB(a,b):

    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            fpb = i
            
    return fpb

# print("KPK dari" + str(n)
print("FPB dari"+ str(num1),"dan", str(num2)," =", hitungFPB(num1, num2))