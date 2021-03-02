def tampil_kata() :
    print("hello\n"); # ini adalah program yang dijalankan apabila kita memanggil fungsi tersebut


def tampil():
    print("hai\n" )

# ada 2 jenis fungsi yaitu fungsi dengan mengembalikan sebuah nilai / atau tanpa dikembalikan
#tanpa kembalian yaitu tanpa return
#kalau mengembalikan nilai kasih retrun

def kembalian_angka(): # return type int
    return 12


def kembalian_bool(): # return type boolean
    return 1


def kembalian_float(): # return type float
    return 19.5



# fungsi dengan parameter
# jika dalam fungsi memiliki masukkan yang tidak di ketahui / memiliki banyak 
# Parameter ini akan menyimpan nilai yang diinputkan ke fungsi 
#contoh fungsi untuk mencetak string namun string tidak di ketahui / mau di diinputkan
def cetak_kata(kata):
    print("kata yang di masukkan ke parameter : ",kata)



#contoh fungsi untuk mengembalikan 2 nilai yang di tambahkan namun 2 nilai ini tidak di ketahui angkanya

def tambah(nilai_1, nilai_2): #nilai_1 dan nilai_2  itu Parameter
    hasil = nilai_1 + nilai_2 # proses menghitung nilai
    return hasil # mengembalikan nilai hasil

# membuat fungsi untuk menampilkan keterangan print perjumlahannya
def cetak_perjumlahan( angka_1,  angka_2):
    print("{} + {} = {}\n".format(str(angka_1), str(angka_2), str(tambah(angka_1,angka_2)))) # mengambil fungsi di dalam fungsi





print("function\n" )
print("-------------\n" )
#function / fungsi adalah suatu bagian dari program yang dipergunakan untuk mengerjakan suatu tugas tertentu yang menghasilkan 
#suatu nilai untuk dikembalikan ke program pemanggil dan letaknya dipisahkan dari bagian program yang menggunakannya
#penulisan fungsi
'''
def nama_fungsi():
    print "Hello ini Fungsi"
'''
print("----------------- penulisan fungsi\n" )
a = "ini adalah kata yang akan di cetak\n";
cetak_kata(a)
tampil()

print("ini adalah int yg di kembalian : ", kembalian_angka(), "\n")
print("ini adalah bool yg di kembalian : ", kembalian_bool(), "\n")
print("ini adalah float yg di kembalian : ", kembalian_float(), "\n")
# ini 2 nilai yang mau di tambahkan
angka_1 = 10
angka_2 = 20
print("----------------- fungsi dengan parameter\n" )
# lalu masukkan ke 2 nilai ini ke fungsi
#tambah(angka_1, angka_2) # cara memasukkan nilai ke parameter
#ini tidak akan di cetak ke console karena belum di cout
print("{} + {} = {}\n".format(str(angka_1), str(angka_2), str(tambah(angka_1,angka_2))))
# ini adalah fungsi yg sangat sederhana, mungkin akan lebih baik langsung membuatnya tanpa fungsi
#namun bagaimana kalau kita akan menambahkan banyak penjumalahan?
#kita tidak mungkin membuatnya satu per-satu,
# maka dengan adanya fungsi kita dengan mudah mengganti parameternya saja
#contoh
angka_1 = 5 # nilainya akan di timpa
angka_2 = 5# nilainya akan di timpa
print("{} + {} = {}\n".format(str(angka_1), str(angka_2), str(tambah(angka_1,angka_2))))
#atau agar lebih mudah kita bisa menggunakan void untuk membuat coutnya
angka_1 = 7
angka_2 = 9
cetak_perjumlahan(angka_1,angka_2) # mencetak dengan fungsi



