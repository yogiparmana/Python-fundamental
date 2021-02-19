# Hello World program in Python
    
print "Hello World!\n"
print "---------------\n"

#buat komen pake pagar
#boleh lupa titik koma
'''
string yang di tidak di jalankan karena tidak ada variable maka bisa 
digunakan untuk line komentar
'''
'''
perhatikan tab saat penulisan!!!!!!!!!!!!!
'''
   
   #deklarasi Variable
#type data di phyton hanya menggunakan namavariable, jika ingin menggunakan int maka nilainya saja yang di ganti int
   
   #akan lebih efectif tanpa deklarasi
   
   #pemberian nilai pada variable / inisialisasi
umur = 21 #jadi int
nama  = "Yogi"; #jadi string
PI = 3.14; #jadi float
PI2 = 3.33 #jadi double
udahmakan = "udah"#jadi boolean
indexprestasi = 'A'; #jadi // char menggunakan petik 1 sedangkan string menggunakan petik 2
   
   #output 
   #output di phton menggunakan print
print "Nama : " + nama #tanda + menggunakan untuk menyambung variable
print "umur : " + str(umur) #str digunakan untuk convert ke string
print "Sudah Makan? : " + str(bool(udahmakan == "udah")) 
print "Index Prestasi : " + str(indexprestasi)
print "PI = {}  dan PI 2 = {}".format(PI,PI2); #teknik format untuk mempermudah 
   # print otomatis menggunakan line (enter) untuk mematikannya menggunkan perintah end='' 
   #print("hai",end='')
