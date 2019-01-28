#INPUT
try:
    angka = int(input('ketik angka:'))
except (ValueError,TypeError,KeyboardInterrupt,KeyError):
    print('harus dalam bentuk angka')


jenisangka = []

#LOGIC
if angka >= 0 or angka <= 0:
    jenisangka.append('Bulat')

if angka >= 0: # bilangan cacah
    jenisangka.append('cacah')

if angka < 0: # bilangan negatif
    jenisangka.append('negatif')

if angka == 0: # bilangan nol
    jenisangka.append('nol')

if angka > 0: # bilangan asli
    jenisangka.append('asli')

if angka % 2 != 0: # bilangan ganjil 
    jenisangka.append('ganjil')


if angka % 2 == 0: # bilangan genap
    jenisangka.append('genap')

# if angka >= 2 or angka % 3 == 0 or angka % 5 == 0 or angka % 7 == 0 or angka % 11 == 0 : prima

if angka > 1 : # bilangan prima
    for i in range(2,angka):
        if (angka % i) != 0:
            jenisangka.append('prima')
        break
    

if angka == 2: # bilangan prima tambahan
    jenisangka.append('prima')
     

if angka > 1 : # komposit
    for i in range(2,angka):
        if (angka % i) == 0:
            jenisangka.append('komposit')
        break
    
#output
print(list(jenisangka))
