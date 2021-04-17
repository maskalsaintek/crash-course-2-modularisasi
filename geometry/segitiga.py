def info():
    return 'Modul menghitung rumus-rumus segitiga'

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')
    return luas_segitiga