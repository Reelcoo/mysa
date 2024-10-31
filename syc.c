#include <stdio.h>  // Memasukkan pustaka standar input-output

int main() {
    // Bagian C Comments
    // Komentar satu baris
    
    /*
       Komentar lebih dari satu baris
       untuk menjelaskan bagian kode berikut
    */

    // Bagian Variables
    int umur = 21;           // Deklarasi variabel umur bertipe integer
    float tinggi = 1.73;     // Deklarasi variabel tinggi bertipe float
    char inisial = 'M';      // Deklarasi variabel inisial bertipe char

    // Bagian Output (Print Text)
    printf("Contoh Program C\n");       // Mencetak teks dengan baris baru (\n)
    printf("Ini adalah contoh output dalam bahasa C\n");

    // C Statements
    printf("Umur saya adalah: %d tahun\n", umur);  // Menggunakan variabel integer
    printf("Tinggi badan saya: %.2f meter\n", tinggi); // Menggunakan variabel float
    printf("Inisial nama saya adalah: %c\n", inisial); // Menggunakan variabel char

    return 0;  // Mengakhiri program dengan return 0
}