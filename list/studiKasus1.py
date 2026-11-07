#Studi Kasus 1
#Dimas Bagus Pratama
#2606681

kekayaanIndonesia = ["Flora", "Hutan", "Fauna", "Pantai", "Adat", "Toleransi"]

#1
kekayaanIndonesia[2] = "Lahan Sawit"
print(f"1. Ganti item dengan nama Hutan menjadi Lahan Sawit  \n{kekayaanIndonesia}")

#2
nama = (input("masukkan nama kekayaan lain: "))
index = int(input("masukkan index: "))
kekayaanIndonesia.insert(index, nama)
print(f"2. Tambahkan item dengan nama dan index yang ditentukan oleh User \n{kekayaanIndonesia}")

#3
kekayaanIndonesia.sort()
print(f"3. Urutkan item pada list sesuai dengan abjadnya \n{kekayaanIndonesia}")