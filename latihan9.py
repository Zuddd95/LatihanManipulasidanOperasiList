# List menyimpan beberapa nilai

# data_angka = [1, 2, 3, 4, 5]
# print(data_angka)

# data_string = ["ucup", "adit", "surya"]
# print(data_string)

# data_campuran = ["ucup", 3, True]
# print(data_campuran)

# # cara cepat membuat list berlaku untuk integer

# data = range(0,10,3) #(start, stop, step)

# print(data)
# data_list = list(data)
# print(data_list)

# list = [i **2 for i in range(0, 10)]
# print(list)

# list = [i  for i in range(0, 10) if i != 5]
# print(list)

# MAnipulasi

data = ["bambang", "ucup", "asep"]
# data[0]

# print(data[0])
# #Menghitung Jumlah Data
# banyak_data = len(data)
# print(banyak_data)

#insert(posisi, item)

# data.insert(1, "joko")
# # print(data)
# data.append("Slamet")
# bajak_laut = ["Lufy", "zoro", "Nami"]

# data.extend(bajak_laut)
# print(data)

# angka = [1,4,3,2,5,6,7]

# print(angka.index(6))
# print(angka.count(2))
# angka.sort()
# print(angka)

# angka.reverse()
# print(angka)

data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
print(data_barang[1][1])
for barang in data_barang:
    print(f"Nama barang: {barang[0]}")
    print(f"Harga barang: {barang[1]}")
    # print(barang)

