
print("Pengulangan\n")
print("-----------\n")
    
    
print("----------- for\n")
#pengulangan dalam bahasa pemrogramman umumnya ada 3 pengulangan
#pengulangan menggunakan -------------------- for
#contoh pengulangan 5x
#bentuk for di python agak berbeda dari bahasa umum lainnya
#for indek in range(banyak_perulangan):
 # jalankan kode ini
 # jalankan juga kode ini
#kode ini tidak akan diulang karena berada di luar for
#baru tau ternyata tab berpengaruh di python
for i in range(0,5):
    print("{}\n".format(str(i))) #01234 karena i dimulai dari o
print("ini tidak kena for\n")
#kenapa 0 karena umumnya for digunakan untuk menampilkan isi array
#karena index array di mulai dari 0
# angka 5 adalah jumlah banyaknya pengulangan
   
print("\n")

#agar dimulai 1 langsung saja isikan (1,6) 
for i in range(1,6):
    print("{}\n".format(str(i))) #12345 karena i dimulai dari 1
print "ini tidak kena for"
   
print("\n")
#contoh pengulangan 5 tapi decrement
for i in range (6,0,-1): #untuk decrement menggunakan tanda negativ agar python bisa tau bahwa decrement
    print("{}\n".format(str(i))) # 54321 karena i dimulai dari 5 
    print("ini kena for")
print("ini tidak kena for")



print("----------- do while\n")
#pengulangan menggunakan -------------------- while 
#do while enggk ada
# i = 0
# do{
# i++ #i + 1
# print("{}\n".format(str(i))) # cetak i 

# }while(i < 5) # sampai i lebih kecil 5
# hasil 12345
print("\n")
i = 5 #ubah i = 5
#---------------while
#while(True):
  # jalankan kode ini
# baris ke 2 ini berada di luar perulangan while
while(i > 0): #cek apakah i lebih besar dari 0 jika true
    print("{}\n".format(str(i))) #cetak i
    i-=1 #i kurang 1
print("ini tidak kena while")


