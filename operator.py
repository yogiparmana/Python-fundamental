print( "Operator\n");
print( "-----------\n");
    
    #-----------operator---------------
    #simbol untuk melakukan operasi
    
    #----------------Operator Aritmatika
'''
Penjumlahan +
Pengurangan -
Perkalian   *
Pembagian   /
Sisa Bagi   %
    
'''
print("----------------------aritmatika\n");

angka1 = 10;
angka2 = 20;

#tambah
hasil = angka1+angka2;
print( "Hasil dari {} + {} = {}\n".format(angka1,angka2,hasil));
#kurang
hasil = angka1-angka2;
print( "Hasil dari {} - {} = {}\n".format(angka1,angka2,hasil));
#kali
hasil = angka1 * angka2;
print( "Hasil dari {} x {} = {}\n".format(angka1,angka2,hasil));
#bagi
hasil = angka2 / angka1;
print( "Hasil dari {} : {} = {}\n".format(angka1,angka2,hasil));
#modulus atau sisa bagi
hasil = angka1 % angka2;
print( "Hasil dari {} mod {} = {}\n".format(angka1,angka2,hasil));

    
    
print( "----------------------penugasan\n");
    
    #----------------Operator penugasan (Assignment Operator) 
    # fungsinya untuk mengisi nilai
    
'''
Pengisian Nilai      =
Pengisian dan Penambahan    +=
Pengisian dan Pengurangan   -=
Pengisian dan Perkalian     *=
Pengisian dan Pembagian     /=
Pengisian dan Sisa bagi     %=
'''
    
    
#=
a = 1;
b = 2;

#+=
print("a : {}, b : {}\n".format(a,b));
a+=b; # artinya a = a + b; 3
print( "a+=b : {}\n".format(a));
a-=b; # artinya a = a - b; -1
print( "a-=b : {}\n".format(a));
a*=b; # artinya a = a x b; 2
print( "a*=b : {}\n".format(a));
a/=b; # artinya a = a / b; 0,5 / 1 karena int
print( "a/=b : {}\n".format(a));
a%=b; # artinya a = a % b;  1
print( "a%=b : {}\n".format(a));

#-----------operator bitwise dengan style penugasan
#operasi berdasarkan biner
'''
AND             &
OR              |
XOR             ^
NOT/komplemen   ~
Left Shift      <<
Right Shift     >>
'''
print("a : {}, b : {}\n".format(a,b));
a<<=b; # artinya a = a << b; menggunakan rumus biner | 0101010
print( "a<<=b : {}\n".format(a));
a>>=b; # artinya a = a >> b; menggunakan rumus biner | 0101010
print( "a>>=b : {}\n".format(a));
a&=b; # artinya a = a & b; menggunakan rumus biner | 0101010
print( "a&=b : {}\n".format(a));
a|=b; # artinya a = a | b; menggunakan rumus biner | 0101010
print( "a|=b : {}\n".format(a));
a^=b; # artinya a = a ^ b; menggunakan rumus biner | 0101010
print( "a^=b : {}\n".format(a));
cc = ~a;
print( "~a : {}\n".format(cc));
cc = ~b;
print( "~b : {}\n".format(cc));
    
    
    
print( "----------------------perbandingan\n");
    
    #----------------perbandingan
    #untuk membandingkan 2 buah nilai
    # menghasilkan true 1, dan false 0
    
'''
Lebih Besar             >
Lebih Kecil             <
Sama Dengan             ==
Tidak Sama dengan       !=
Lebih Besar Sama dengan >=
Lebih Kecil Sama dengan <=
'''
print("a : {}, b : {}\n".format(a,b));
c = a > b;
print( "a>b : {}\n".format(c));
c = a < b;
print( "a<b : {}\n".format(c));
c = a == b;
print( "a==b : {}\n".format(c));
c = a != b;
print( "a!=b : {}\n".format(c));
c = a >= b;
print( "a>=b : {}\n".format(c));
c = a <= b;
print( "a<=b : {}\n".format(c));
  
 
 #---------------operator logika
 
print( "-------------------logika\n");
 
'''
Logika AND        true  && true = true, sisanya false 
Logika OR         false  || false = false, sisanya true
Negasi/kebalikan    !true = false, !false = true

di ptython mengguna nama tanpa simbol
'''
# a=1, b=2

print("a : {}, b : {}\n".format(a,b));
print("a && b : {}\n".format((a==3 and b==2))); #false
print("a || b : {}\n".format((a==3 or b==2))); #true
print( "!a : {}\n".format(not(a==3 or b==2))); #false
print( "!b : {}\n".format(not(a==3 and b==2)));#true


#---------------operator lain-lain

print( "---------------------- operator lain-lain\n");

'''
Alamat memori   &   untuk mengambil alamat memori
Pointer         *   untuk membuat pointer
Ternary         ? : untuk membuat kondisi
Increment       ++  untuk menambah 1
Decrement       --  untuk mengurangi 1

'''
#python tidak support pointer
#int *d;
#print("ambil tempat memori variable d : "+ &d);

#format penulisan ternary di python <Nilai True> if Kondisi else <Nilai False>
print("apakah 1 = 2 ? : {}\n".format( ("iya" if 1 == 2  else "tidak")));
var = 7;
#di pyton ++ / -- menggunkan +1 / -1
print("{} ditambahkan satu kali : {}\n".format(var,var+1)); 
print("{} dikurangkan satu kali : {}\n".format(var,var-1));


    

