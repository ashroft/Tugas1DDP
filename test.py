# Fitur Belanja
total_item=0
total=0
nama= "Ashrof Firzatullah - SI05"
print(nama)
print("Fitur Belanja")
while True :
    produk=input("Masukkan nama produk yang akan dibeli [Ketik X untuk berhenti]: ")
    if produk == "X":
        print("Terima kasih. Sampai jumpa.")
        break
    else:
        harga=int(input("Masukkan harga produk tersebut : "))
    print("Telah berhasil menambahkan", produk , "seharga", harga)
    total += int(harga)
    total_item += 1

if produk == "X":
    print("")
    print("total produk yang di beli : ",total_item)
    print("total harga yang dibayarkan : ",total)

# Keanggotaan Pelanggan
if total_item > 0 :
    while True:
        pelanggan=input("Apakah anda merupakan anggota [Y/n]? : ")
        if pelanggan == "n":
            print("Total harga yang harus dibayarkan", total)
            print("Terima kasih telah berbelanja di NFElectrics.")
        else:
            if pelanggan.upper == "Y" :
                while True:
                    email=input("Masukkan email : ")
                    if email.endswith(".com") and email[-5] !="@" and not email.startswith("@") and email.count("@"):
                        else:
                    break    
                while True:
                    password=input ("Masukkan password: ")
                    if len(password) >= 8 and password.upper() and password.lower() and "!" in password or "@" in password or "#" in password or "$" in password:
                        break
                    else:
                        if len(password) <= 8:
                            print("Password tidak valid")
            if pelanggan == "Y" :
                while True :
                    level=input("Masukkan level Anda : ")
                    if level == "Gold" and total_item < 5 :
                        print("Selamat! Anda mendapat potongan harga sebesar 5%")
                        potongan=total*0.05
                    elif level == "Gold" and total_item >= 5 :
                        print("Selamat! Anda mendapat potongan harga sebesar 10%")
                        potongan=total*0.1
                    elif level == "Silver" and total_item < 5 :
                        print("Selamat! Anda mendapat potongan harga sebesar 10%")
                        potongan=total*0.1
                    elif level == "Silver" and total_item >= 5 :
                        print("Selamat! Anda mendapat potongan harga sebesar 15%")
                        potongan=total*0.15
                    elif level == "Diamond" and total_item < 5 :
                        print("Selamat! Anda mendapat potongan harga sebesar 15%")
                        potongan=total*0.15
                    elif level == "Diamond" and total_item >= 5 :
                        print("Selamat! Anda mendapat potongan harga sebesar 20%") 
                        potongan=total*0.20
                    else:
                        print("Total harga yang harus dibayar : ", total-potongan)
                        print("Terima kasih telah berbelanja di NFElectronics.")

