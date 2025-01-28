# Program Kalkulator Sederhana
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa dibagi dengan nol!"

def main():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    choice = input("Masukkan pilihan (1/2/3/4): ")

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if choice == '1':
        print(f"{num1} + {num2} = {tambah(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {kurang(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {kali(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
