# belajar perbandingian lanjutan, ELIF

nama = input("masukan nama :")

if nama=="edy": # kondisi 1
    print("Dosen ganteng") # aksi true 1
elif nama=="haryanto": # kondisi 2
    print("dosen ganteng banget") # aksi true 2
elif nama=="ilham": # kondisi 3
    print("anda kn mahasiswa") # aksi true 3
else:
    print("bukan dosen ganteng") # aksi false
print("program selesai")

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

print("Selamat datang di aplikasi penjumlahan/pengurangan!")
print("Pilih operasi yang ingin Anda lakukan:")
print("1. Penjumlahan")
print("2. Pengurangan")

pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

if pilihan == '1':
    bil1 = float(input("Masukkan bilangan pertama: "))
    bil2 = float(input("Masukkan bilangan kedua: "))
    hasil = penjumlahan(bil1, bil2)
    print("Hasil penjumlahan:", hasil)
elif pilihan == '2':
    bil1 = float(input("Masukkan bilangan pertama: "))
    bil2 = float(input("Masukkan bilangan kedua: "))
    hasil = pengurangan(bil1, bil2)
    print("Hasil pengurangan:", hasil)
else:
    print("Pilihan tidak valid.")


    

    