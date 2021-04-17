"""
Program menghitung luas segitiga
luas segitiga = 1/2 * alas * tinggi
"""

print('Menghitung Luas Segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2

print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nMenghitung Luas Segitiga 2 dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2

print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nMenghitung fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')
    return luas_segitiga

hitung_luas_segitiga(10, 6)
hitung_luas_segitiga(20, 2)
