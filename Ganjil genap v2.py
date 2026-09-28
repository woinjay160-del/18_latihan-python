def cek_bilangan():
    while True:
        print("===== PROGRAM CEK BILANGAN =====")

        angka = int(input("Masukkan sebuah bilangan: "))

        if angka % 2 == 0:
            print("Bilangan", angka, "adalah GENAP")
        else:
            print("Bilangan", angka, "adalah GANJIL")

        pilihan = input("Apakah ingin mengulang? (y/n): ")

        if pilihan.lower() == "n":
            print("Program selesai.")
            break


def cek_prima():
    while True:
        print("===== PROGRAM CEK BILANGAN PRIMA =====")

        angka = int(input("Masukkan sebuah bilangan: "))

        if angka < 2:
            print("Bilangan", angka, "BUKAN prima")
        else:
            prima = True
            for i in range(2, int(angka ** 0.5) + 1):
                if angka % i == 0:
                    prima = False
                    break

            if prima:
                print("Bilangan", angka, "adalah PRIMA")
            else:
                print("Bilangan", angka, "BUKAN prima")

        pilihan = input("Apakah ingin mengulang? (y/n): ")

        if pilihan.lower() == "n":
            print("Program selesai.")
            break