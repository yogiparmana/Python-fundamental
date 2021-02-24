print("Pengulangan lanjutan x latihan\n")
print("-----------------\n")


print("----------- perulangan 2 dimensi\n")
   #pengulangan 2 dimensi yaitu baris dan kolom
   #000
   #000
   #
   #contoh pengulangan 2 dimensi
for i in range(5): # ini untuk baris 
    for j in range(4): # ini untuk kolom | 5 baris 4 kolom
        print("baris ke-{} kolom ke-{}| ".format(i,j))  
    print("\n")
print("\n")
   
   
print(" ------------ perulangan 3 dimensi\n")
   #perulangan 3 dimensi yaitu baris kolom 1 isi
'''
| 1| 1| 1| | 1| 1| 2| | 1| 1| 3| -> baris
| 1| 2| 1| | 1| 2| 2| | 1| 2| 3| 
| 1| 3| 1| | 1| 3| 2| | 1| 3| 3| 
    isi         isi         isi
| 2| 1| 1| | 2| 1| 2| | 2| 1| 3| 
| 2| 2| 1| | 2| 2| 2| | 2| 2| 3| 
| 2| 3| 1| | 2| 3| 2| | 2| 3| 3| 
    isi         isi         isi
| 3| 1| 1| | 3| 1| 2| | 3| 1| 3| 
| 3| 2| 1| | 3| 2| 2| | 3| 2| 3| 
| 3| 3| 1| | 3| 3| 2| | 3| 3| 3| 
    isi         isi         isi
    
kolom
'''
for i in range(3): # baris
    for j in range(3): #kolom
        for k in range(3):   #isi (kolom baris)
            print("| {}| {}| {}|\t ".format(i,j,k))
        print("\n")
    print("\n")

print(" ------------ perulangan 3 dimensi ++ \n")
  
    # lebih dari 3 dimensi sama kayak 3 dimensi tapi isinya 
'''
| 1| 1| 1| 1|   | 1| 1| 1| 2|   | 1| 1| 1| 3|   
| 1| 1| 2| 1|   | 1| 1| 2| 2|   | 1| 1| 2| 3|   
| 1| 1| 3| 1|   | 1| 1| 3| 2|   | 1| 1| 3| 3|   
    isi1isi1isi1
| 1| 2| 1| 1|   | 1| 2| 1| 2|   | 1| 2| 1| 3|   
| 1| 2| 2| 1|   | 1| 2| 2| 2|   | 1| 2| 2| 3|   
| 1| 2| 3| 1|   | 1| 2| 3| 2|   | 1| 2| 3| 3|   
  isi1isi1isi1
| 1| 3| 1| 1|   | 1| 3| 1| 2|   | 1| 3| 1| 3|   
| 1| 3| 2| 1|   | 1| 3| 2| 2|   | 1| 3| 2| 3|   
| 1| 3| 3| 1|   | 1| 3| 3| 2|   | 1| 3| 3| 3|   
  isi1isi1isi1
isi 2

| 2| 1| 1| 1|   | 2| 1| 1| 2|   | 2| 1| 1| 3|   
| 2| 1| 2| 1|   | 2| 1| 2| 2|   | 2| 1| 2| 3|   
| 2| 1| 3| 1|   | 2| 1| 3| 2|   | 2| 1| 3| 3|   
  isi1            isi1            isi1
| 2| 2| 1| 1|   | 2| 2| 1| 2|   | 2| 2| 1| 3|   
| 2| 2| 2| 1|   | 2| 2| 2| 2|   | 2| 2| 2| 3|   
| 2| 2| 3| 1|   | 2| 2| 3| 2|   | 2| 2| 3| 3|   
  isi1            isi1            isi1
| 2| 3| 1| 1|   | 2| 3| 1| 2|   | 2| 3| 1| 3|   
| 2| 3| 2| 1|   | 2| 3| 2| 2|   | 2| 3| 2| 3|   
| 2| 3| 3| 1|   | 2| 3| 3| 2|   | 2| 3| 3| 3|   
  isi1            isi1            isi1
              isi2

| 3| 1| 1| 1|   | 3| 1| 1| 2|   | 3| 1| 1| 3|   
| 3| 1| 2| 1|   | 3| 1| 2| 2|   | 3| 1| 2| 3|   
| 3| 1| 3| 1|   | 3| 1| 3| 2|   | 3| 1| 3| 3|   
  isi1            isi1            isi1
| 3| 2| 1| 1|   | 3| 2| 1| 2|   | 3| 2| 1| 3|   
| 3| 2| 2| 1|   | 3| 2| 2| 2|   | 3| 2| 2| 3|   
| 3| 2| 3| 1|   | 3| 2| 3| 2|   | 3| 2| 3| 3|   
  isi1            isi1            isi1
| 3| 3| 1| 1|   | 3| 3| 1| 2|   | 3| 3| 1| 3|   
| 3| 3| 2| 1|   | 3| 3| 2| 2|   | 3| 3| 2| 3|   
| 3| 3| 3| 1|   | 3| 3| 3| 2|   | 3| 3| 3| 3|   
  isi1            isi1            isi1
            isi3
'''

for i in range(3):# baris
    for j in range(3):#kolom
        for k in range(3):# 1 isi (kolom, baris)
            for l in range(3): # 2 isi(kolom, baris)
                print("| {}| {}| {}| {}|".format(i,j,k,l)) 
            print("\n")
        print("\n")
    print("\n")



 


print("--------------perulangan dengan kondisi\n")
   #perulangan juga bisa memiliki kondisi 
   #seperti saat kita membuat perulangan angka ganjil
print("Membuat bilangan ganjil\n")
for i in range(10):
       #kondisi
    if i%2 != 0:
        print("{} ".format(i))
print("\n")
   
print("Membuat bilangan genap\n")
for i in range(10):
       #kondisi
    if i%2 == 0:
        print("{} ".format(i))
print("\n")
   

   
print("\n")
