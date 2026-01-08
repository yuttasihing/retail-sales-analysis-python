"""
Project: Retail Sales Data Analysis (Pure Python)
Author: Yutta Sihing Gusti
Date: January 2026
Description: 
    Program ini menganalisis data transaksi penjualan retail mentah (format list of dicts)
    untuk menghasilkan wawasan bisnis seperti total omzet, performa kota, dan produk terlaris.
    Kode ditulis menggunakan Python Murni (tanpa Pandas) untuk mendemonstrasikan logika algoritma.
"""

#1. Raw Data (Data Mentah)
# Data diambil dari agregasi AI Gemini sebagai metode pembelajaran simulasi data transaksi

data_penjualan = [
    {"tanggal": "2024-01-01", "produk": "Laptop", "qty": 1, "harga": 12000000, "kota": "Jakarta"},
    {"tanggal": "2024-01-01", "produk": "Mouse", "qty": 5, "harga": 100000, "kota": "Bandung"},
    {"tanggal": "2024-01-02", "produk": "Monitor", "qty": 2, "harga": 2500000, "kota": "Jakarta"},
    {"tanggal": "2024-01-02", "produk": "Laptop", "qty": 1, "harga": 12000000, "kota": "Surabaya"},
    {"tanggal": "2024-01-03", "produk": "Keyboard", "qty": 3, "harga": 500000, "kota": "Bandung"},
    {"tanggal": "2024-01-03", "produk": "Mouse", "qty": 2, "harga": 100000, "kota": "Jakarta"},
    {"tanggal": "2024-01-04", "produk": "Laptop", "qty": 2, "harga": 11500000, "kota": "Bandung"},
    {"tanggal": "2024-01-05", "produk": "Monitor", "qty": 1, "harga": 2500000, "kota": "Surabaya"}
]

#2. Calculating Grand Total
grand_total = 0

for data in data_penjualan:
    grand_total += data['qty']*data['harga']

print(f'1. Grand total of sales  = Rp{grand_total:,.0f}')

#3. Total omzet by cities (Regional Performance)
#Grand Total Report by cities
omzet_by_cities = {}

for data in data_penjualan:
    kunci = data['kota']
    nilai = data['qty']*data['harga']

    if kunci in omzet_by_cities:
        omzet_by_cities[kunci] = omzet_by_cities[kunci] + nilai
    else:
        omzet_by_cities[kunci] = nilai 

print("\n2. Total omzet by cities :")
for kota, total in omzet_by_cities.items():
    print(f'    - {kota} : {total}')

#City with The Highest Omzet
kota_tertinggi = max(omzet_by_cities,key=omzet_by_cities.get)
total_tertinggi = max(omzet_by_cities.values())
print(f'    The highest omzet by cities : {kota_tertinggi} = Rp{total_tertinggi:,.0f}')

#4. Top Selling Product Analysis 
product_by_qty = {}

for data in data_penjualan:
    kunci1 = data['produk']
    nilai1 = data['qty']

    if kunci1 in product_by_qty:
        product_by_qty[kunci1] = product_by_qty[kunci1] + nilai1
    else:
        product_by_qty[kunci1] = nilai1

produk_terlaris = max(product_by_qty,key=product_by_qty.get)
qty_terlaris = max(product_by_qty.values())

print(f'\n3. Top selling product : {produk_terlaris} with {qty_terlaris} selling')

#5. High Value Filter Transaction 
print('\n4. High Value Transaction (> 10 million) :')

for data in data_penjualan:
    total_nilai = data["qty"] * data["harga"]
    if total_nilai > 10000000:
        print(f' - {data['tanggal']} | {data['kota']} | {data['produk']} | Rp{total_nilai:,.0f} ')

print('\n ==== End of Report ====')