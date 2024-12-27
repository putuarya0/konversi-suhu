# konversi-suhu
Deskripsi Proyek

Program ini adalah implementasi sederhana dari konversi suhu menggunakan Python. Pengguna dapat memilih konversi dari berbagai skala suhu, yaitu Celsius, Fahrenheit, Kelvin, dan Reamur. Program ini memungkinkan pengguna untuk:

Mengkonversi suhu ke salah satu dari empat skala yang tersedia.

Memilih sumber suhu dari salah satu skala lainnya.

Program ini menggunakan logika if-else untuk memproses input pengguna dan menghitung hasil konversi berdasarkan rumus yang sesuai.

Fitur Utama

Pilihan Menu:

Pengguna dapat memilih skala suhu tujuan: Celsius, Fahrenheit, Kelvin, atau Reamur.

Setelah memilih tujuan, pengguna dapat memilih sumber suhu untuk dikonversi.

Rumus Konversi:

Celsius ke Fahrenheit: F = (C * 9/5) + 32

Celsius ke Kelvin: K = C + 273

Celsius ke Reamur: Re = C * 4/5

Fahrenheit ke Celsius: C = (F - 32) * 5/9

Fahrenheit ke Kelvin: K = (F - 32) * 5/9 + 273

Fahrenheit ke Reamur: Re = (F - 32) * 4/9

Kelvin ke Celsius: C = K - 273

Kelvin ke Fahrenheit: F = (K - 273) * 9/5 + 32

Kelvin ke Reamur: Re = (K - 273) * 4/5

Reamur ke Celsius: C = Re * 5/4

Reamur ke Fahrenheit: F = (Re * 9/4) + 32

Reamur ke Kelvin: K = Re * 5/4 + 273

Validasi Input:

Program akan menampilkan pesan kesalahan jika pengguna memasukkan pilihan yang tidak valid.

Cara Menggunakan Program

Jalankan program Python.

Pilih menu konversi suhu dengan memilih salah satu dari 4 opsi utama:

1: Celsius

2: Fahrenheit

3: Kelvin

4: Reamur

Setelah memilih skala tujuan, pilih sumber skala suhu.

Masukkan nilai suhu yang ingin dikonversi.

Program akan menghitung dan menampilkan hasil konversi.

Contoh Penggunaan

Contoh 1: Konversi dari Fahrenheit ke Celsius

Masukkan 1 untuk memilih konversi ke Celsius.

Masukkan 1 untuk memilih sumber suhu Fahrenheit.

Masukkan nilai suhu Fahrenheit, misalnya 100.

Program akan menghitung hasil: (100 - 32) * 5/9 = 37.78 dan menampilkan hasilnya.

Contoh 2: Konversi dari Kelvin ke Fahrenheit

Masukkan 2 untuk memilih konversi ke Fahrenheit.

Masukkan 2 untuk memilih sumber suhu Kelvin.

Masukkan nilai suhu Kelvin, misalnya 300.

Program akan menghitung hasil: (300 - 273) * 9/5 + 32 = 80.6 dan menampilkan hasilnya.

Persyaratan

Python versi 3.6 atau lebih baru.

Saran Perbaikan

Tambahkan loop untuk memungkinkan pengguna melakukan konversi berkali-kali tanpa harus menjalankan ulang program.

Gunakan fungsi untuk memisahkan logika konversi dan antarmuka pengguna agar kode lebih terorganisir.

Tambahkan validasi input untuk menangani kesalahan seperti memasukkan huruf saat program meminta angka.

Catatan

Jika pengguna memasukkan pilihan menu yang salah, program akan menampilkan pesan kesalahan dan keluar. Pastikan untuk mengikuti instruksi dengan benar.
