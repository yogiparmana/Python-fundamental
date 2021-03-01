
print("List\n")
print("-------------\n")
#list digunakan untuk menyimpan banyak data
#contoh tanpa list
# namaMurid1 = "Ayu"
# namaMurid2 = "Bunga"
# namaMurid3 = "Cyntia"
# namaMurid4 = "Deni"
# namaMurid5 = "Elisa"
#gimana kalo murid ada 100 atau 1000? 
#maka agar lebih efisien kita gunakan list
#nama_list = []
print("---------- memasukkan data ke list\n")
nama_list_murid = [ # inisialisasi list dengan jumlah data 
#di phyton list bisa disisi type data apa saya, campur juga boleh 
"Ayu", #[0] ini adalah index, index dimulai dari 0,
#jika jumlah datanya 5 maka indexnya 0-4, 
"Bunga",
"Cyntia",
"Deni",
"Elisa"
]
#sama dong kayak yang di atas, kalo datanya ada 100 masak harus buat nama_list_murid[100]
#kita bisa membuat looping untuk mengisi datanya
#contoh membuat 10 data
nilai_list_murid = []
#buat object scanner unutk input
for i in range(10):
    nilai_list_murid.append(input("masukan nilai murid ke [" + str((i+1)) + "] : ")) # keterangan dan proses input
#append buat memasukkan value ke list
# i adalah angka yang akan di looping mulai dari 0-9
#maka kita akan menginputkan data sebanyak 10x
#kalo mau input ada 100 tinggal looping aja seratus kali

#atau bisa langsung di masukkan
absen_list_murid = [
1,2,3,4,5
] #1 memiliki index 0

print("---------- menampilkan list\n")
# cara menampilkan list
print("nama :{}\n".format(nama_list_murid[0])) 
#bagaimana kalo datanya ada banyak? ya looping aja

for i in range(5):
    print("nama murid ke [ {} ] : {}\n".format(str((i+1)),nama_list_murid[i]))#menampilkan list nama_list_murid 

for i in range(5):
    print("absen murid ke [ {} ] : {}\n".format(str((i+1)),str(absen_list_murid[i]))) #menampilkan list absen_list_murid 

# terus bagaimana kalo banyak datanya tidak diketahui? masak harus meriksa satu per satu?
#bisa gunakan len(nama_variable)
banyak = len(nilai_list_murid)
for i in range(banyak):
    print("nilai murid ke [ {} ] : {}\n".format(str((i+1)),str(nilai_list_murid[i]))) #menampilkan list nilai_list_murid 


for i in range(5):
    print("absen murid ke [ {} ] : {}\n".format((i+1),absen_list_murid[i])) #menampilkan list absen_list_murid 

# terus bagaimana kalo banyak datanya tidak diketahui? masak harus meriksa satu per satu?
#bisa gunakan len(nama_variable)
banyak = len(nilai_list_murid)
for i in range(banyak):
    print("nilai murid ke [ {} ] : {}\n".format((i+1),nilai_list_murid[i])) #menampilkan list nilai_list_murid 

