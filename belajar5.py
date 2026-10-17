print("pilih 1 untuk menghitung luas persegi")
print("pilih 2 untuk menghitung luas lingkaran")
print("pilih 3 untuk menghitung luas segitiga")

pilihan = int(input("masukan pilihan (1/2/3)"))

match pilihan:
    case 1:
        s = int(input("masukan panjang sisi persegi: "))
        luas = s * s
        print(f"luas persegi adalah: {luas}")

    case 2:
        r = int(input("masukan panjang jari jari lingkaran: "))
        pi = 3.14
        luas = pi * r**2
        print(f"luas lingkaran adalah: {luas}")

    case 3:
        a = int(input("masukan panjang alas segitiga: "))
        t = int(input("masukan panjang tinggi segitiga: "))
        luas = a * t / 2
        print(f"luas segitiga adalah: {luas}")

    case _:
        print("masukan pilihan dengan benar")

kendaraan = ["supra", "motor", 200, "pink", 2]
tambahan = [5000, "matic"]
kendaraan.extend(tambahan)
kendaraan.insert(2, "honda")
print(kendaraan)