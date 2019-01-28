import requests



print(' Selamat datang, mau tahu berita apa hari ini?')
print('[1] Berita seputar teknologi')
print('[2] Berita seputar bisnis')
print('[3] Berita seputar olahraga')
print('[4] Berita seputar kesehatan')
print('[5] Berita seputar science')

try:
    pil = input('Ketik pilihan Anda  (1/2/3/4) : ')
except (ValueError,TypeError,KeyboardInterrupt,KeyError):
    print('ndak bisaaa')


if pil == '1':
   for i in range(6):
        url='https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=8004a711db2e44cd857e3b14982d2a2d'
        data = requests.get(url)
        data = data.json()  
        a = 1 
        for i in range(0,5):
            print(str(a) + '. ' +data['articles'][i]['title'])
            a += 1
        break
        

elif pil == '2':
    for i in range(6):
        url='https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=8004a711db2e44cd857e3b14982d2a2d'
        data = requests.get(url)
        data = data.json()  
        a = 1 
        for i in range(0,5):
            print(str(a) + '. ' +data['articles'][i]['title'])
            a += 1
        break
elif pil == '3':
    for i in range(6):
        url='https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=8004a711db2e44cd857e3b14982d2a2d'
        data = requests.get(url)
        data = data.json()  
        a = 1 
        for i in range(0,5):
            print(str(a) + '. ' +data['articles'][i]['title'])
            a += 1
        break
elif pil == '4':
     for i in range(6):
        url='https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=8004a711db2e44cd857e3b14982d2a2d'
        data = requests.get(url)
        data = data.json()  
        a = 1 
        for i in range(0,5):
            print(str(a) + '. ' +data['articles'][i]['title'])
            a += 1
        break
elif pil == '5':
     for i in range(6):
        url='https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=8004a711db2e44cd857e3b14982d2a2d'
        data = requests.get(url)
        data = data.json()  
        a = 1 
        for i in range(0,5):
            print(str(a) + '. ' +data['articles'][i]['title'])
            a += 1
        break
else:
    print('pilihannya hanya sampai 5 pakk')

