import pandas as pd
import os
import pyfiglet 
from tabulate import tabulate

def hiasan(apa):
    print(f"\033[96m",pyfiglet.figlet_format(apa, font='small'),f"\033[0m")

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    b = 130
    blue = "\033[34m"
    cyan = "\033[96m"
    endc = "\033[0m"

    print(blue + "=" * b + endc)
    print(cyan)
    print("███████╗███████╗██████╗ ███████╗████████╗ █████╗ ███╗   ███╗██╗   ██╗".center(b))
    print("██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗████╗ ████║██║   ██║".center(b))
    print("███████╗█████╗  ██████╔╝█████╗     ██║   ███████║██╔████╔██║██║   ██║".center(b))
    print("╚════██║██╔══╝  ██╔═══╝ ██╔══╝     ██║   ██╔══██║██║╚██╔╝██║██║   ██║".center(b))
    print("███████║███████╗██║     ███████╗   ██║   ██║  ██║██║ ╚═╝ ██║╚██████╔╝".center(b))
    print("╚══════╝╚══════╝╚═╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝".center(b))
    print(endc)
    print(blue + "=" * b + endc)
 
def cek(dicek):
    try:
        if not dicek.strip():
            raise ValueError("Tidak boleh kosong")
        elif dicek.isdigit():
            raise ValueError("Harus berupa huruf")
        else:
            return dicek
    except ValueError as e:
        print(e)
        return False

def dicek(angka):
    try:
        if not angka.strip():
            raise ValueError("Tidak boleh kosong")
        elif angka.isalpha():
            raise ValueError("Harus berupa angka")
        else:
            return angka
    except ValueError as e:
        print(e)
        return False
    
akun = "farmers.csv"
def register():
    while True:
        nama = input("Masukkan nama : ")
        if cek(nama) == False:
            continue
        else:
            break
    while True:
        while True:
            no_wa = input("Masukkan nomor whatsapp : ")
            if dicek(no_wa) == False:
                continue
            else:
                break
        if not no_wa.startswith("62"):
            print("Nomor harus berawal 62")
        elif len(no_wa) < 8:
            print("Nomor harus lebih dari 8 digit")
        elif no_wa.isdigit(): 
            break
        else:
            print("Mohon inputkan dengan benar")
    while True:
        askot = input("Masukkan asal kota : ")
        if cek(askot) == False:
            continue
        else:
            break
    buka = pd.read_csv(akun)
    while True: 
        username = input("Buat username : ")
        if not username.strip():
            print("Username tidak boleh kosong")
            continue
        if username in buka['Username'].values:
            print("Username telah terdaftar, buat yang lain")
        else:
            break
    while True:
        password = input("Buat pasword : ")
        if not password.strip():
            print("Password tidak boleh kosong")
        else:
            break
    ID = buka['ID'].max()
    ID += 1
    baru = pd.DataFrame({'ID':[ID],'Nama':[nama],'Asal Kota': [askot],'Nomor WA': [no_wa],'Username': [username],'Password': [password],'Role': ['user']})
    baru.to_csv(akun, mode='a', header=False, index=False)
    hiasan("Registrasi berhasil")
    input("Tekan enter untuk melanjutkan")
    clear_terminal()

def login():
    while True:
        username = input("Masukkan username : ")
        if cek(username) == False:
            continue
        else:
            break
    password = input("Masukkan password : ")
    buka = pd.read_csv(akun)
    if username in buka['Username'].values:
        sebaris = buka[buka["Username"]== username]
        if sebaris['Password'].values[0] == password:
            hiasan("Login berhasil")
            input("Tekan enter untuk melanjutkan")
            clear_terminal()
            role = sebaris['Role'].values[0]           
            id_user = sebaris["ID"].values[0]
            nama = sebaris["Nama"].values[0]
            Menu(role,id_user,nama)
        else:
            hiasan("Password salah")
            input("Tekan enter untuk melanjutkan")
            clear_terminal()
    else:        
        hiasan("Akun belum terdaftar")
        input("Tekan enter untuk melanjutkan")
        clear_terminal() 


def kuasaAdmin(pilih):
    buka = pd.read_csv("daftarbarang.csv")
    while True:
        if pilih == "1":
            id_alat = buka["id alat"].max()
            id_alat += 1
            while True:
                nama_alat = input("Masukkan nama alat : ")
                if cek(nama_alat) == False:
                    continue
                else:
                    break
            while True:
                jenis = input("Masukkan jenis alat : ")
                if cek(jenis) == False:
                    continue
                else:
                    break
            while True:
                fungsi = input("Masukkan fungsi alat : ")
                if cek(fungsi) == False:
                    continue
                else:
                    break
            while True:
                try:
                    harga = input("Masukkan harga perharinya : ")
                    if dicek(harga) == False:
                        continue
                    else:
                        float(harga)
                        break
                except ValueError:
                    print("Harap masukkan nominal dengan benar")
            baru = pd.DataFrame({'Nama Alat':[nama_alat],'id alat':[id_alat],'Jenis Alat':[jenis],
                                 'Fungsi':[fungsi],'Harga Sewa per Hari (Rp)':[harga]})
            baru.to_csv("daftarbarang.csv", mode="a", header=False, index=False)
            hiasan("Data berhasil ditambahkan")
            input("Tekan enter untuk kembali")  
            clear_terminal()
            break
        elif pilih == "2":
            while True:
                try:
                    id_barang = int(input("Masukkan id barang yang ingin diubah : "))
                    break
                except ValueError:
                    print("Id barang yang dimasukkan harus angka")
            if id_barang in buka["id alat"].values:
                while True:
                    sebaris = buka[buka["id alat"] == id_barang]
                    print(tabulate(sebaris, headers='keys', tablefmt='fancy_grid'))
                    print("""
                          ╔══════════════════════════════════╗
                          ║     Pilih yang ingin diubah      ║
                          ║┌────────────────────────────────┐║
                          ║│        1. Nama Alat            │║
                          ║│        2. Jenis Alat           │║ 
                          ║│        3. Fungsi               │║
                          ║│        4. Harga Perhari        │║
                          ║│        5. Kembali              │║
                          ║└────────────────────────────────┘║
                          ╚══════════════════════════════════╝""")
                    while True:
                        pilihan = input("Silahkan pilih : ")
                        if dicek(pilihan) == False:
                            continue
                        elif pilihan == '1' or pilihan == '2' or pilihan == '3' or pilihan == '4' or pilihan == '5':
                            break
                        else:
                            print("Hanya masukkan (1/2/3/4/5)")
                    match pilihan:
                        case "1":
                            while True:
                                nama = input("Masukkan nama alat pengganti : ")
                                if cek(nama) == False:
                                    continue
                                else:
                                    break
                            buka.loc[buka["id alat"] == id_barang, "Nama Alat"] = nama
                            buka.to_csv("daftarbarang.csv", index=False)
                            hiasan(f"Nama alat berhasil diganti menjadi {nama}")
                            input("Tekan enter untuk kembali")
                            clear_terminal()
                        case "2":
                            while True:
                                jenis_alat = input("Masukkan jenis alat pengganti : ")
                                if cek(jenis_alat) == False:
                                    continue
                                else:
                                    break
                            buka.loc[buka["id alat"] == id_barang, "Jenis Alat"] = jenis_alat
                            buka.to_csv("daftarbarang.csv", index=False)
                            hiasan(f"Jenis alat berhasil diganti menjadi {jenis_alat}")
                            input("Tekan enter untuk kembali")
                            clear_terminal()
                        case "3":
                            while True:
                                fungsi = input("Masukkan fungsi pengganti : ")
                                if cek(fungsi) == False:
                                    continue
                                else:
                                    break
                            buka.loc[buka["id alat"] == id_barang, "Fungsi"] = fungsi
                            buka.to_csv("daftarbarang.csv", index=False)
                            hiasan(f"Fungsi alat berhasil diganti menjadi {fungsi}")
                            input("Tekan enter untuk kembali")
                            clear_terminal()
                        case "4":
                            while True:
                                try:
                                    harga = input("Masukkan harga sewa perhari pengganti : ")
                                    if dicek(harga) == False:
                                        continue
                                    else:
                                        float(harga)
                                        break
                                except ValueError:
                                    print("Harus berupa angka")
                            buka.loc[buka["id alat"] == id_barang, "Harga Sewa per Hari (Rp)"] = harga
                            buka.to_csv("daftarbarang.csv", index=False)
                            hiasan(f"Harga sewa alat berhasil diganti menjadi Rp{harga}")
                            input("Tekan enter untuk kembali")
                            clear_terminal()
                        case "5":
                            clear_terminal()
                            break
                        case _:
                            print("Menu tidak sesuai")
                            continue
                break
            else:
                print("Id barang tidak ditemukan")
        elif pilih == "3":
            while True:
                try:
                    id_barang = int(input("Masukkan id barang yang ingin dihapus : "))
                    break
                except ValueError:
                    print("Id yang anda masukkan salah")
            if id_barang in buka["id alat"].values:
                sebaris = buka[buka["id alat"] == id_barang]
                buka = buka[buka["id alat"] != id_barang]
                nama_alat = sebaris["Nama Alat"].values[0]
                buka.to_csv("daftarbarang.csv", index=False)
                hiasan(f"Data barang {nama_alat} berhasil dihapus")
                input("tekan enter untk kembali")
                clear_terminal()
                break
            else:
                print("Id barang tidak ditemukan")
        else:
            print("Tidak ada menu yang cocok")
            break

def barang(role):
    clear_terminal()
    buka = pd.read_csv("daftarbarang.csv")
    print(tabulate(buka, headers='keys', tablefmt='fancy_grid'))
    if role == "admin":
        while True:
            print(
"""
╔══════════════════════════════════╗
║           Kelola Barang          ║
║┌────────────────────────────────┐║""")
            print("║│                                │║")
            print("║│  1. Tambah Barang              │║")
            print("║│  2. Ubah Barang                │║")
            print("║│  3. Hapus Barang               │║")
            print("║│  4. Kembali                    │║")
            print("║└────────────────────────────────┘║")
            print("╚══════════════════════════════════╝") 
            while True:   
                pilihan = input("Pilih program : ")
                if pilihan == "4":
                    clear_terminal()
                    break
                elif pilihan == '1' or pilihan == "2" or pilihan == "3":
                    kuasaAdmin(pilihan)
                    break
                else:
                    print("Hanya masukkan (1/2/3/4)")
            break
    else:
        input("Tekan enter untuk kembali")
        clear_terminal()

def link_wa(nama_user,id_user,id_peminjaman,id_alat,nama_alat,waktu,total,jaminan):
    hasil = total+jaminan
    link = "https://wa.me/6285655993964"
    pesan = (
        f"Halo admin, saya, atas nama:\n"
        f"Nama \t\t: {nama_user}\n"
        f"Id \t\t: {id_user}\n"
        f"Id peminjaman \t: {id_peminjaman}\n\n"
        f"Ingin meminjam:\n"
        f"Nama alat \t: {nama_alat}\n"
        f"Id alat \t\t: {id_alat}\n"
        f"Jangka waktu \t: {waktu} hari\n"
        f"Harga \t\t: Rp{total:,.2f}\n"
        f"Jaminan \t\t: Rp{jaminan:,.2f}\n"
        f"Harga total \t: Rp{hasil:,.2f}\n\n"
        f"Mohon untuk segera di acc, terimakasih"
    )
    link_jadi = pesan.replace(" ", "%20").replace("\n", "%0A").replace("\t", "%09")
    return f"{link}?text={link_jadi}"

def cek_pinjam(id_user,nama):
    buka = pd.read_csv("data_pinjaman.csv")
    while True:
        if id_user in buka["id user"].values:
            sebaris = buka[buka["id user"] == id_user]
            ID = sebaris["id peminjaman"].max()
            sebarisID = buka[buka["id peminjaman"] == ID]
            status = sebarisID["status"].values[0]
            nama_alatPinjam = sebarisID["nama alat"].values[0]
            if status == "dikembalikan":
                pinjam(id_user,nama)
                break
            elif status == "proses verivikasi":
                hiasan(f"{nama_alatPinjam} yang ingin kamu pinjam masih {status}")
                input("Tekan enter untuk kembali")
                clear_terminal()
            elif status == "ditolak":
                pinjam(id_user,nama)
                break
            else:
                hiasan(f"Mohon kembalikan dulu {nama_alatPinjam}nya")
                input("Tekan enter untuk kembali")
                clear_terminal()
            break
        else:
            pinjam(id_user,nama)
            break

def kecerdasan():
    import google.generativeai as ai
    model = ai.GenerativeModel("gemini-pro")
    rhs = 'AIzaSyBAce6MFOhpPVdbCIdJg-DnlMovFaniUDw'
    ai.configure(api_key=rhs)
    while True:
        tanya = input("""Masukkan quit atau exit untuk kembali\n
        Pertanyaan : """)
        if cek(tanya) == False:
            continue
        elif tanya == "quit" or tanya == "exit":
            hiasan("Terimaksih telah bertaya pada saya")
            input("Tekan enter untuk kembali")
            clear_terminal()
            break
        else:
            jawab = model.generate_content(tanya)
            print("Jawab : \n")
            try:
                print("\033[34m",jawab.text,"\n","\033[30m")
            except ValueError:
                print("Pertanyaan yang anda masukkan mengandung kata yang dilarang")
            print("\033[34m","="*120,"\n\033[30m")
            
def help(id_user):
    print("""
                    1. Daftar Barang
                       Berisi kumpulan barang yang bisa dipinjam, lengkap dengan informasi seperti id barang, nama, fungsi, haraga sewa, dan lain sebagainya
                    2. Pinjam
                       Ini adalah menu peminjaman, jika anda ingin meminjam barang, anda tinggal masuk ke menu ini
                    3. Pengembalian
                       Menu ini digunakan jika anda ingin mengembalikan barang yang anda pinjam
                    4. Riwayat Peminjama
                       Menu ini berisikan seluruh data peminjaman yang pernah dan sedang anda lakukan
                    5. Informasi Akun
                       Menu ini berisikan seluruh data diri anda""")
    while True:
        tanya = input("Apakah ada yang masih dibingungkan? (ya/tidak) : ").lower()
        if cek(tanya) == False:
            continue
        elif tanya == 'ya' or tanya == 'tidak':
            break
        else:
            print('Hanya masukkan (ya/tidak)')
            continue
    if tanya == "ya":
        while True:
            apa = input("Silahkan tuliskan apa yang anda bingungkan? : ")
            if cek(apa) == False:
                continue
            else:
                break
        print("""
              ╔══════════════════════════════════════════════╗
              ║            Pilih Salah Satu Admin            ║
              ║┌────────────────────────────────────────────┐║
              ║│      1. Admin 1                            │║
              ║│         Nama : Nadine Alfina Azzahwa       │║
              ║│         NIM  : 242410103040                │║
              ║│      2. Admin 2                            │║
              ║│         Nama : Muhammad Fajrul Falah       │║
              ║│         NIM  : 242410103052                │║
              ║│      3. Admin 3                            │║
              ║│         Nama : Muhammad Raihan Ramdhani    │║
              ║│         NIM  : 242410103059                │║
              ║│      4. Admin 4                            │║
              ║│         Nama : Kecerdan Buatan             │║
              ║└────────────────────────────────────────────┘║
              ╚══════════════════════════════════════════════╝""")
        buka = pd.read_csv("farmers.csv")
        sebaris = buka[buka["ID"] == id_user]
        nama = sebaris["Nama"].values[0]
        while True:
            hubung = input("Silahkan pilih salah satu admin untuk dihubungi : ")
            if dicek(hubung) == False:
                continue
            elif hubung == '1' or hubung == '2' or hubung == '3' or hubung == '4':
                break
            else:
                print("Hanya masukkan angka (1/2/3/4)")
                continue
        pesan = (
            "Halo admin, saya:\n"
            f"Nama \t: {nama}\n"
            f"Id user \t: {id_user}\n"
            f"Ingin menanyakan tentang, {apa}?\n"
            "Terimakasih admin")
        link_jadi = pesan.replace(" ", "%20").replace("\n", "%0A").replace("\t", "%09")    
        if hubung == "1":
            link = f"https://wa.me/6285655993964?text={link_jadi}"
            print(link)
            print("Silahkan kunjungi link tersebut")
            input("Tekan enter untuk kembali")
            clear_terminal()
            return
        elif hubung == "2":
            link = f"https://wa.me/6287863306466?text={link_jadi}"
            print(link)
            print("Silahkan kunjungi link tersebut")
            input("Tekan enter untuk kembali")
            clear_terminal()
            return
        elif hubung == "3":
            link = f"https://wa.me/6289505122959?text={link_jadi}"
            print(link)
            print("Silahkan kunjungi link tersebut")
            input("Tekan enter untuk kembali")
            clear_terminal()
            return
        elif hubung == "4":
            kecerdasan()
            return
        else:
            print("Yang anda masukkan tidak sesuai")

    elif tanya == "tidak":
        clear_terminal()
        return
    else:
        print("Apa yang anda masukkan tidak sesuai")


def pinjam(id_user,nama):
    clear_terminal()
    buka = pd.read_csv("daftarbarang.csv")
    print(tabulate(buka, headers="keys", tablefmt="fancy_grid"))
    while True:
        try:
            id_alat = int(input("Masukkan id alat yang ingin dipinjam : "))
            break
        except ValueError:
            print("Id alat yang anda masukkan tidak sesuai")
    if id_alat in buka["id alat"].values:
        while True:
            try:
                waktu = int(input("Lama peminjaman (hari) : "))
                break
            except ValueError:
                print("Masukkan waktu dalam jumlah hari")
        sebaris = buka[buka["id alat"] == id_alat]
        harga = int(sebaris["Harga Sewa per Hari (Rp)"].values[0])
        sebaris = buka[buka["id alat"] == id_alat]
        nama_alat = sebaris["Nama Alat"].values[0]
        total = waktu * harga
        jaminan = total * 10//100
        hasil = total + jaminan
        print(f"""
                Atas nama \t: {nama}
                Alat dipinjam \t: {nama_alat} 
                Jangka waktu \t: {waktu} hari 
                Harga sewa \t: Rp {total:,.2f}
                Jaminan \t: Rp {jaminan:,.2f}
                Total biaya \t: Rp {hasil:,.2f}
                Jaminan diambil dari 10% total biaya sewa, dan akan dikembalikan ketika barang kembali""")
        while True:
            while True:
                tanya = input("Apakah sudah sesuai (ya/tidak) : ").lower()
                if cek(tanya) == False:
                    continue
                elif tanya == 'ya' or tanya == 'tidak':
                    break
                else:
                    print('Hanya masukkan (ya/tidak)')
            if tanya == "ya":
                buka_dataPinjam = pd.read_csv("data_pinjaman.csv")
                id_peminjaman = int(buka_dataPinjam["id peminjaman"].max())
                id_peminjaman += 1
                buka = "data_pinjaman.csv"
                baru = pd.DataFrame({"id peminjaman":[id_peminjaman],"id user":[id_user],"id alat":[id_alat],"nama alat":[nama_alat],"jangka waktu":[waktu],"jaminan":[jaminan],"status":["proses verivikasi"]})
                baru.to_csv(buka, mode="a", header=False, index=False)
                link_wa(nama,id_user,id_peminjaman,id_alat,nama_alat,waktu,total,jaminan)
                wa_link = link_wa(nama,id_user,id_peminjaman,id_alat,nama_alat,waktu,total,jaminan)
                hiasan("Proses peminjaman diproses...")
                input("Silahkan tekan enter untuk membuat link WA konfirmasi ke admin")
                clear_terminal()
                print("Silahkan buka link whatsapp berikut untuk melakukan konfirmasi")
                print(wa_link)
                input("Tekan enter untuk melanjutkan")
                clear_terminal()
                break
            elif tanya == "tidak":
                pinjam(id_user,nama)
                break
            elif tanya == " ":
                print("Ngak ada isian, apa itu?")
            else:
                print("Silahkan masukkan ulang")
    elif id_alat == "":
        print("Mohon masukkan id alat yang ingin dipinjam")
    else:
        print("Id alat tidak ditemukan")
        tanya = input("Tidak jadi meminjam (jadi/tidak) : ").lower()
        if tanya == "tidak":
            hiasan("Peminjaman dibatalkan")
            input("Tekan enter untuk melanjutkan")
            clear_terminal()
            return
        else:
            pinjam(id_user,nama)

def pengembalian(nama,id_user):
    buka_dataPinjam = pd.read_csv("data_pinjaman.csv")
    while True:
        if id_user in buka_dataPinjam["id user"].values:
            sebaris = buka_dataPinjam[buka_dataPinjam["id user"] == id_user]
            ID = sebaris["id peminjaman"].max()
            sebarisID = buka_dataPinjam[buka_dataPinjam["id peminjaman"] == ID]
            dipinjam = sebarisID["nama alat"].values[0]
            jaminan = sebarisID["jaminan"].values[0]
            status = sebarisID["status"].values[0]
            if status == "dipinjam":
                print(f"""
                Atas nama \t: {nama}
                Alat dipinjam \t: {dipinjam}
                Jaminan \t: Rp {jaminan:,.2f}""")
                while True:
                    while True:
                        jawab = input("Apakah ingin dikembalikan (ya/tidak) : ").lower()
                        if cek(jawab) == False:
                            continue
                        else:
                            break
                    if jawab == "ya":
                        buka_dataPinjam.loc[buka_dataPinjam["id peminjaman"] == ID, "status"] = "dikembalikan"
                        buka_dataPinjam.to_csv("data_pinjaman.csv", index=False)
                        hiasan(f"{dipinjam} yang dipinjam telah dikembalikan")
                        print(f"Silahkan minta uang jaminan anda sebesar Rp {jaminan:,.2f} ke admin")
                        input("Tekan enter untuk kembali")
                        clear_terminal()
                        hiasan(f"Terimakasih Telah Meminjam dan Mengembalikan {dipinjam} kami")
                        input("Tekan enter untuk kembali")
                        clear_terminal()
                        break
                    elif jawab == "tidak":
                        break
                    else:
                        clear_terminal()
                        break
                clear_terminal()
                break
            elif status == "proses verivikasi":
                hiasan(f"{dipinjam} yang ingin kamu pinjam masih {status}")
                input("Tekan enter untuk kembali")
                clear_terminal()
                break
            else:
                hiasan(f"{nama} tidak meminjam apa-apa")
                input("Tekan enter untuk ke menu utama")
                clear_terminal()
                break
        else:
            hiasan(f"{nama} tidak meminjam apa-apa")
            input("Tekan enter untuk ke menu utama")
            clear_terminal()
            break

def  riwayat_peminjaman(id_user,role):
    if role == "user":
        clear_terminal()
        buka = pd.read_csv("data_pinjaman.csv")
        buka = buka[buka["id user"] == id_user]
        print(tabulate(buka, headers='keys', tablefmt='fancy_grid'))
        input("Tekan enter untuk kembali")
        clear_terminal()
    else:
        clear_terminal()
        buka = pd.read_csv("data_pinjaman.csv")
        print(tabulate(buka, headers="keys", tablefmt="fancy_grid"))
        input("Tekan enter untuk kembali")
        clear_terminal()

def laporanTransaksi():
    buka = pd.read_csv("data_pinjaman.csv")
    buka_akun = pd.read_csv("farmers.csv")
    print(tabulate(buka, headers="keys", tablefmt="fancy_grid"))
    print("""
            1. Ubah Status
            2. Kembali""")
    while True:
        jawab_angka = input("Menu yang dipilih : ")
        if dicek(jawab_angka) == False:
            continue
        elif jawab_angka == "1" or jawab_angka == "2":
            break
        else:
            print("Hanya masukkan angka (1/2)")
    if jawab_angka == "1":
        while True:
            try:
                id_user = int(input("Masukkan id user yang ingin diubah statusnya : "))
            except ValueError:
                print("Id user yang dimasukkan tidak sesuai")
                continue
            if id_user not in buka["id user"].values:
                print("Id yang anda masukkan tidak ada di daftar")
                continue
            sebaris = buka[buka["id user"] == id_user]
            ID = sebaris["id peminjaman"].max()
            sebaris_akun = buka_akun[buka_akun["ID"] == id_user]
            sebarisID = sebaris[sebaris["id peminjaman"] == ID]
            nama = sebaris_akun["Nama"].values[0]
            alat = sebarisID["nama alat"].values[0]
            waktu = sebarisID["jangka waktu"].values[0]
            if sebarisID["status"].values[0] == "dikembalikan":
                hiasan(f"{alat} yang dipinjam oleh {nama} sudah dikembalikkan")
                input("Tekan enter untuk kembali")
                clear_terminal()
                break
            elif sebarisID["status"].values[0] == "ditolak":
                hiasan(f"{alat} yang dipinjam oleh {nama} sudah ditolak")
                input("Tekan enter untuk kembali")
                clear_terminal()
                break
            elif sebarisID["status"].values[0] == "dipinjam":
                hiasan(f"{alat} telah dipinjam oleh {nama}")
                input("Tekan enter untuk kembali")
                clear_terminal()
                break
            print(f"""Apakah yakin ingin menyetujui peminjaman: 
                Alat dipinjam \t: {alat}
                Nama peminjam \t: {nama}
                Lama peminjaman \t: {waktu} hari
""")
            while True:
                jawab = input("Peminjamannya di acc? (ya/tidak) : ").lower()
                if cek(jawab) == False:
                    continue
                elif jawab == 'ya' or jawab == 'tidak':
                    break
                else:
                    print('Hanya masukkan (ya/tidak)')
            if jawab == "ya":
                buka.loc[buka["id peminjaman"] == ID, "status"] = "dipinjam"
                buka.to_csv("data_pinjaman.csv", index=False)
                hiasan(f"Peminjaman alat {alat} berhasil di acc")
                input("Tekan enter untuk kembali") 
                clear_terminal()
                break
            elif jawab == "tidak":
                while True:
                    jawab = input("Apakah ingin menolak pengajuan peminjaman (ya/tidak) : ")
                    if cek(jawab) == False:
                        continue
                    elif jawab == 'ya' or jawab == 'tidak':
                        break
                    else:
                        print("Hanya masukkan (ya/tidak)")
                if jawab == "ya":
                    buka.loc[buka["id peminjaman"] == ID, "status"] = "ditolak"
                    buka.to_csv("data_pinjaman.csv", index=False)
                    hiasan(f"Peminjaman {alat} berhasil di tolak")
                    input("Tekan enter untuk kembali")
                    clear_terminal()
                    break
                else:
                    clear_terminal()
                    break
            else:
                print("Menu yang anda pilih tidak ada")
                continue
    elif jawab_angka  == "2":
        clear_terminal()
    else:
        print("Menu yang dipilih tidak tersedia")

def info_akun(id_user):
    buka = pd.read_csv("farmers.csv")
    sebaris = buka[buka["ID"] == id_user]
    iD = sebaris["ID"].values[0]
    nama = sebaris['Nama'].values[0]
    askot = sebaris['Asal Kota'].values[0]
    nomorWA = sebaris['Nomor WA'].values[0]
    username = sebaris['Username'].values[0]
    password = sebaris["Password"].values[0]
    role = sebaris["Role"].values[0]
    buka = pd.read_csv("data_pinjaman.csv")
    print(f"""
                Nama \t\t: {nama}
                ID \t\t: {iD}
                Asal Kota \t: {askot}
                Nomor WA \t: {nomorWA}
                Username \t: {username}
                Password \t: {password}
                Role \t\t: {role}""")
    if role == "user":
        sebaris = buka[buka["id user"] == id_user]
        jumlah_peminjaman = len(sebaris)
        print(f"                Riwayat pinjam \t: {jumlah_peminjaman}")
        input("Tekan enter untuk kembali")
        clear_terminal()
    else:
        total = len(buka)
        di_pinjam = buka[buka["status"] == "dipinjam"]
        di_kembalikan = buka[buka['status'] == "dikembalikan"]
        prose_veriv = buka[buka['status'] == "proses verivikasi"]
        di_tolak = buka[buka['status'] == "ditolak"]
        di_pinjam = len(di_pinjam)
        di_kembalikan = len(di_kembalikan)
        prose_veriv = len(prose_veriv)
        di_tolak = len(di_tolak)
        print(f"""              Alat dipinjam \t: {di_pinjam}
            Alat dikembalikan \t: {di_kembalikan}
            Alat ditolak \t: {di_tolak}
            Proses verivikasi \t: {prose_veriv}
            Total peminjaman \t: {total}""")
        input("Tekan enter untuk kembali")
        clear_terminal()

def Menu(role,id_user,nama):
    w = "\033[96m"
    e = "\033[0m"
    while True:
        banner()
        b = 138
        print(f"{w}╔══════════════════════════════════╗{e}".center(b))
        print(f"{w}║{e}     Sewa Alat Pertanian Murah    {w}║{e}".center(b+8))
        print(f"{w}║┌────────────────────────────────┐║{e}".center(b))
        if role=="user":
            print(f"{w}║│                                │║{e}".center(b))
            print(f"{w}║│{e}  1. Daftar Barang              {w}│║{e}".center(b+8)) 
            print(f"{w}║│{e}  2. Pinjam                     {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  3. Pengembalian               {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  4. Riwayat Peminjaman         {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  5. Informasi Akun             {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  6. Help                       {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  7. Kembali                    {w}│║{e}".center(b+8))
            print(f"{w}║├────────────────────────────────┤║{e}".center(b))
            print(f"{w}║│{e}           Menu User            {w}│║{e}".center(b+8))
            print(f"{w}║└────────────────────────────────┘║{e}".center(b))
        else:
            print(f"{w}║│                                │║{e}".center(b))
            print(f"{w}║│{e}  1. Kelola Barang              {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  2. Laporan Transaksi          {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  3. Riwayat Peminjaman         {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  4. Info Akun                  {w}│║{e}".center(b+8))
            print(f"{w}║│{e}  5. Kembali                    {w}│║{e}".center(b+8))
            print(f"{w}║├────────────────────────────────┤║{e}".center(b))
            print(f"{w}║│{e}           Menu Admin           {w}│║{e}".center(b+8))
            print(f"{w}║└────────────────────────────────┘║{e}".center(b))
        print(f"{w}╚══════════════════════════════════╝{e}".center(b) ) 

        if role == "user":
            pilihan = input("Menu yang dipilih : ")
            match pilihan:
                case "1":
                    barang(role)
                case "2":
                    cek_pinjam(id_user,nama)
                case "3":
                    pengembalian(nama,id_user)
                case "4":
                    riwayat_peminjaman(id_user,role)
                case "5":
                    info_akun(id_user)
                case "6":
                    help(id_user)
                case "7":
                    clear_terminal()
                    break
                case _:
                    clear_terminal()
                    print("Menu tidak sesuai")
        
        else:
            pilihan = input("Menu yang dipilih : ")
            match pilihan:
                case "1":
                    barang(role)
                case "2":
                    laporanTransaksi()
                case "3":
                    riwayat_peminjaman(id_user,role)
                case "4":
                    info_akun(id_user)
                case "5":
                    clear_terminal()
                    break
                case _:
                    clear_terminal()
                    print("Menu tidak sesuai")

while True:
    hiasan("Selamat datang di toko SEPETAMU")
    print("""
1. Login
2. Register
3. Keluar""")
    pilih = input("Silahkan pilih : ")
    if pilih == '1':
        login()
    elif pilih == '2':
        register()
    elif pilih == '3':
        clear_terminal()
        break
    else:
        clear_terminal()
        print("Pilihan yang kamu masukkan tidak sesuai")

