#LOGIC
def FPB(a,b): 
    batas = a 
    if b>a:
        batas = b 
    fpb = 1 
    for i in range(1,batas+1): 
        if (a%i==0) and (b%i==0): 
            fpb = i 
    return fpb 

def KPK(a,b): 
    return int((a*b)/(FPB(a,b))) 

# INPUT
try:
    A = int(input("Masukkan bilangan A: "))
except (ValueError,TypeError,KeyboardInterrupt,KeyError):
    print('harus dalam bentuk angka')

try:
    B = int(input("Masukkan bilangan B: "))
except (ValueError,TypeError,KeyboardInterrupt,KeyError):
    print('harus dalam bentuk angka')


# OUTPUT
print("KPK dari " + str(A) + " dan " + str(B) + " adalah " + str(KPK(A,B)) + ".")
print("FPB dari "+ str(A),"dan", str(B),"=", FPB(A, B))