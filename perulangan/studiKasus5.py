#DIMAS BAGUS PRATAMA
#2606681
#1C
#Studi Kasus 5

usernameAsli = "dasproRPL"
passwordAsli = "RPLfire!123"
kesempatan = 3

while kesempatan > 0 :
     username = input("Masukkan username anda: ")
     password = input("Masukkan password anda: ")
     if username == usernameAsli and password == passwordAsli :
          print("Selamat Username anda benar")
          break
     elif kesempatan > 0 : 
          kesempatan -= 1
          if kesempatan == 0 :
               print("Kesempatan anda habis")
               break
     print(f"Kesempatan anda {kesempatan}")

          