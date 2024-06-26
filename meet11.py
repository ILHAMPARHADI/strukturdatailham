def main():
    # Meminta pengguna untuk memasukkan angka-angka (dipisahkan oleh spasi)
    angka_input = input("Masukkan beberapa angka (pisahkan dengan spasi): ")

    # Pisahkan angka-angka menggunakan split() dan konversi ke dalam bentuk list of strings
    angka_strings = angka_input.split()

    # Inisialisasi variabel untuk menyimpan jumlah total
    total = 0

    # Looping untuk menjumlahkan angka-angka dalam list
    for angka_str in angka_strings:
        try:
            angka = float(angka_str)  # Konversi string angka menjadi float (agar bisa menerima bilangan desimal)
            total += angka
        except ValueError:
            print(f"Warning: '{angka_str}' bukan angka yang valid dan akan diabaikan.")

    # Menampilkan jumlah total
    print(f"Total dari angka-angka yang dimasukkan adalah: {total}")

if __name__ == "__main__":
    main()
