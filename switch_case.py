print("switch case\n")
print("-----------------\n")
#switch case adalah percabangan kode program dimana kita membandingkan isi sebuah variabel dengan beberapa nilai
#contoh
#number = 2 #langsung input atau
number = input("masukkan angka : ")
''' format switch case di python
def f(x): function
    return { kembalian
        'a': 1, x == a jalankan 1
        'b': 2, x == b jalankan 2
    }.get(var, default) jika x != a || b
'''
def angka(number): #variable yg akan di switch / di periksa
    return{
        0: 0, #jika number == 0 jalankan ini
        1: 1, #jika number == 1 kalankan ini
        3: 3 # jika number == 3 jalankan ini
    }.get(number,4) # jika number tidak sama dengan case #jalankan ini

if angka(number) != 4:
    print("number == ",angka(number))
else:
    print("number != 0,1,3")
 
