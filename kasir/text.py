def kasir():
    # List untuk menyimpan barang belanjaan dan harga
    barang_list = []  
    harga = []
    
    # Akun default untuk login
    account = {'username': 'cahyo', 'password': '12345'}  

    print("=" * 21)
    print("\tKASIR\n")
    print("=" * 21)

    while True:
        try:
            # Tanya apakah user sudah punya akun
            matching = input("Sudah punya akun? (y/n): ")

            if matching.lower() == "y":
                # Login user
                login = input("Silahkan masukan username: ")
                password = input("Silahkan masukan password: ")

                # Periksa apakah username dan password cocok
                if login == account['username'] and password == account['password']:
                    print(f"""
                          
Selamat datang {account['username']}""")
                    while True:
                        try:
                            # Menu utama
                            milih = int(input("""
    Silahkan pilih menu\n
    1. Memasukan barang belanjaan
    2. List barang belanjaan anda
    3. Info account
    4. Membayar
    5. Keluar
                    : """))
                        except ValueError:
                            print("Input tidak valid, silahkan masukkan angka.")
                            continue  # Kembali ke awal loop jika input tidak valid

                        if milih == 1:
                            print("Ketik 'selesai' apabila sudah selesai")
                            # Loop untuk menambahkan barang
                            while True:
                                barang = input("Silahkan masukan barang anda: ")
                                if barang.lower() == "selesai":
                                    print("Barang sudah masuk ke daftar belanjaan anda.")
                                    break
                                try:
                                    rp = int(input("Masukan harganya: "))
                                except ValueError:
                                    print("Input harga harus berupa angka!")
                                    continue
                                barang_list.append(barang)  # Tambah barang ke list
                                harga.append(rp)  # Tambah harga ke list

                        elif milih == 2:
                            # Menampilkan daftar barang belanjaan
                            if not barang_list:
                                print("Belum ada barang di daftar belanjaan.")
                            else:
                                for i, (item, price) in enumerate(zip(barang_list, harga)):
                                    print(f"{i + 1}. {item} - Rp.{price}")

                        elif milih == 3:
                            # Menu untuk mengubah dan menampilkan informasi akun
                            sandi = len(account['password'])
                            print("Informasi akun anda")
                            print (f"""
Username: {account['username']}
Password: {'*'*sandi}
""")
                            while True :
                                ubah = input("apakah ingin di ubah ? (y/n) :")
                                if ubah.lower() == "y" :
                                    new_username = input("Masukkan username baru: ")
                                    new_password = input("Masukkan password baru: ")
                                    account['username'] = new_username
                                    account['password'] = new_password
                                    print("Akun berhasil diperbarui.")
                                elif ubah.lower() == "n" :
                                    break

                                else :
                                    print("Input tidak valid, silahkan masukkan y atau n.")

                        elif milih == 4:
                            # Membayar dan menampilkan struk
                            try:
                                total_harga = sum(harga)
                                print(f'total harga belanjaan anda sebesar Rp. {total_harga}') 
                                uang_user = int(input("Masukkan uang anda: Rp. "))
                            except ValueError:
                                print("Input harus berupa angka!")
                                continue

                              # Hitung total harga
                            kembalian = uang_user - total_harga

                            print("\n========= STRUK KASIR =========")
                            for item, price in zip(barang_list, harga):
                                print(f"{item:<15} Rp. {price:>7}")  # Format rata kiri & kanan
                            print("===============================")
                            print(f"Uang Anda       Rp. {uang_user}")
                            print(f"Total Harga     Rp. {total_harga}")
                            if kembalian >= 0:
                                print(f"Kembalian       Rp. {kembalian}")
                            else:
                                print(f"Kekurangan      Rp. {-kembalian}")
                            print("===============================")
                            print("Terima kasih, sampai jumpa!")
                            return      # Keluar dari program
                        
                        elif milih ==  5 :
                            print("terima kasih, sampai jumpa!!")
                            break
                            
                        else:
                            print("Pilihan tidak valid, silahkan coba lagi.")

                else:
                    print("Username atau password salah, silahkan ulangi kembali.")
                    continue

            elif matching.lower() == "n":
                # Membuat akun baru
                print("Silahkan buat akun terlebih dahulu.")
                create_account = input("Ingin membuat akun? (y/n): ")
                if create_account.lower() == "y":
                    user = input("Masukkan username: ")
                    pw = input("Masukkan password: ")
                    account['username'] = user
                    account['password'] = pw
                    print("Akun baru telah dibuat. Silakan login.")
                else:
                    print("Kembali ke menu utama.")
                    continue

            else:
                print("Input tidak valid, silahkan masukkan 'y' atau 'n'.")

        except ValueError:
            print("Terjadi kesalahan, silahkan ulangi kembali.")
            continue

kasir()
