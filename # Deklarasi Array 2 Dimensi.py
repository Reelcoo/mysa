# Deklarasi Array 2 Dimensi
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Menampilkan matriks
print("Matriks 3x3:")
for baris in matriks:
    print(baris)

# Mengakses elemen pada baris pertama dan kolom kedua (indeks dimulai dari 0)
print("\nElemen di baris pertama, kolom kedua: ", matriks[0][1])

# Mengubah elemen pada baris kedua dan kolom ketiga
matriks[1][2] = 10
print("\nSetelah perubahan elemen pada baris 2, kolom 3: ")
for baris in matriks:
    print(baris)
