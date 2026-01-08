# 📊 Retail Sales Data Analysis (Pure Python)

## 📖 Project Overview
Repository ini berisi proyek analisis data sederhana yang mensimulasikan pemrosesan data transaksi retail. Tujuan utamanya adalah mengekstrak wawasan bisnis (*business insights*) dari data mentah tanpa menggunakan library eksternal (seperti Pandas), melainkan menggunakan logika algoritma **Python Murni (Pure Python)**.

Proyek ini mendemonstrasikan pemahaman fundamental tentang:
- **Data Structures:** List of Dictionaries, Tuples.
- **Control Flow:** Loops (`for`), Conditional Logic (`if-else`).
- **Algorithm:** Accumulator Pattern untuk agregasi data & Filtering Logic.

## 💼 Business Problem
Sebuah toko retail elektronik memiliki data transaksi harian yang belum diolah. Manajemen membutuhkan laporan otomatis untuk menjawab pertanyaan berikut:
1. Berapa **total omzet** perusahaan?
2. Kota mana yang memiliki **performa penjualan terbaik**?
3. Apa **produk terlaris** berdasarkan jumlah unit terjual?
4. Transaksi mana saja yang bernilai besar (**High Value Transactions**) untuk keperluan audit?

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** None (Pure Python Built-in functions)

## 🔍 Key Code Logic
Berikut adalah cuplikan logika algoritma yang digunakan untuk melakukan agregasi data (menghitung total per kategori) secara manual:

```python
# Accumulator Pattern untuk menghitung Omzet per Kota
omzet_by_cities = {}

for data in data_penjualan:
    kota = data['kota']
    nilai = data['qty'] * data['harga']

    if kota in omzet_by_cities:
        omzet_by_cities[kota] += nilai  # Update nilai jika key sudah ada
    else:
        omzet_by_cities[kota] = nilai   # Buat key baru jika belum ada
