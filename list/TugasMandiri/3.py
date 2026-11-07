#Tugas Mandiri no 3
#Dimas Bagus Pratama
#2606681

#input 10 teman sekaligus
listTeman = []

while True : 
    listTeman = input("masukkan nama teman anda: ").split(", ")

    if len(listTeman) < 10 :
        print("Nama teman yang anda masukkan kurang")
    else : 
        print("\nwow anda punya banyak teman")
        break

print(f"Berikut list berisi nama teman anda: \n{listTeman}")
