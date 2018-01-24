nama = input("Ketikkan nama yang akan dicoba \n").lower() # untuk menerima input, dapat menerima input huruf kapital/non kapital
nama = nama.replace(" ","") # digunakan untuk menghapus spasi dari input
jmlI = jmlB = jmlD = jmlO = jmlA = jmlU = jmlE = jmlT = jmlL = 0

# Mengecek setiap huruf yang ada di dalam nama
for huruf in nama: 
    if 'i' in huruf:
        jmlI += 1
    if 'b' in huruf:
        jmlB += 1
    if 'd' in huruf:
        jmlD += 1
    if 'o' in huruf:
        jmlO += 1
    if 'a' in huruf:
        jmlA += 1
    if 'u' in huruf:
        jmlU += 1
    if 'e' in huruf:
        jmlE += 1
    if 't' in huruf:
        jmlT += 1
    if 'l' in huruf:
        jmlL += 1

# Aturan klasifikasi
# Jika terdapat lebih banyak huruf I, A, U, E, T, dan L, maka gendernya akan 
# diklasifikasikan sebagai perempuan, jika sebaliknya, maka diklarifikasikan
# sebagai laki-laki.

if (jmlI+jmlA+jmlU+jmlE+jmlT+jmlL) > (jmlB+jmlD+jmlO):
    print("Gender anda adalah perempuan")
elif (jmlI+jmlA+jmlU+jmlE+jmlT+jmlL) == (jmlB+jmlD+jmlO):
    print("Gender anda tidak diketahui")
else:
    print("Gender anda adalah laki-laki")


# Data percobaan
# laki-laki : adityo nugroho, alda delas, alwan muzakki, bramantyo agung prabowo, kamal hasan mahmud
# Perempuan : qotrunnada firly ramadhanti, rina puspita, ulfa dewanti, septiana putri, vina fadriani effendi
# HASIL
# 1 unidentified
# 9 woman
# OPINI
# Setelah saya amati, sistem klasifikasi ini terlalu condong untuk mengklasifikasikan nama perempuan, 
# karena terlalu banyak feature yang menandakan perempuan, sedangkan laki-laki hanya sedikit.