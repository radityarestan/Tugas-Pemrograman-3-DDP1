# Mengimpor module csv
import csv

# Fungsi yang berisi daftar perintah yang ada di program ini
def DAFTAR_PERINTAH(pilihan):
    
    # Menampilakn data semua perintah dan memberi ucapan kepada user
    if pilihan == "1" :
        print("Daftar Perintah di Program Ini")
        print("{:2s} {:44s} {}".format("No", "Perintah", "Kegunaan"))
        print("{:2d} {:44s} {}".format(0, "IMPOR namafile", 
              "untuk mengambil data yang akan diolah"))
        print("{:2d} {:44s} {}".format(1, "LIHAT" , 
              "untuk melihat nama budaya yang telah tersedia"))
        print("{:2d} {:44s} {}".format(2, "CARINAMA NamaBudaya", 
              "untuk melihat informasi dari budaya tersebut"))
        print("{:2d} {:44s} {}".format(3, "CARITIPE TipeBudaya", 
              "untuk melihat informasi dari tipe budaya tersebut"))
        print("{:2d} {:44s} {}".format(4, "CARIPROV Provinsi", 
              "untuk melihat informasi budaya dari provinsi tersebut"))
        print("{:2d} {:44s} {}".format(5, "TAMBAH Nama;;;Tipe;;;Provinsi;;;referenceurl", 
              "untuk menambahkan data yang belum ada"))
        print("{:2d} {:44s} {}".format(6, "UPDATE Nama;;;Tipe;;;Provinsi;;;referenceurl", 
              "untuk memperbarui data yang sudah ada"))
        print("{:2d} {:44s} {}".format(7, "HAPUS NamaBudaya", 
              "untuk menghapus data-data budaya tersebut"))
        print("{:2d} {:44s} {}".format(8, "STAT", 
              "untuk menampilkan jumlah total warisan budaya"))
        print("{:2d} {:44s} {}".format(9, "STATTIPE", 
              "untuk menampilkan jumlah warisan budaya per tipe dari yang terbanyak"))
        print("{:2d} {:44s} {}".format(10, "STATPROV", 
              "untuk menampilkan jumlah warisan budaya per provinsi dari yang terbanyak"))
        print("{:2d} {:44s} {}".format(11, "KELUAR", 
              "untuk mengakhiri program"))
        print()
        print("SELAMAT MENJALANI PROGRAM INI!")
        
    # Memberi ucapan kepada user sebelum menjalani program yang sebenarnya
    elif pilihan == "2" :
        print("SELAMAT MENJALANI PROGRAM INI!")
        
    # Penanganan eksepsi jika user memasukkan selain yang diperintahkan
    else :
        print("Pilihan anda salah, coba ulangi!")

# Fungsi untuk mengambil file yang berisi data untuk diolah        
def IMPOR(nama_file):
    data = {}
    
    # Menyoba membuka file dan menyalinnya ke dalam sebuah dictionary
    try :
        with open(nama_file, newline = '') as file:
            reader = csv.reader(file)
            for elemen in reader :
                data[elemen[0]] = elemen[1:]
            
            # Memberi nilai balik berupa dictionary
            return data
    
    # Kasus penanganan eksepsi jika file tidak ditemukan
    except FileNotFoundError :
        print("Berkas file yang anda cari tidak ditemukan!")
        print("Ketik 1 jika anda ingin memulai program tanpa mengimpor file")
        
        # Memberi pertanyaan ke user apakah mau melanjutkan program tanpa mengimpor file
        pilihan = input("Masukkan pilihan anda: ")
        if pilihan == "1" :
            return data

# Fungsi untuk melihat nama budaya apa saja yang tersedia
def LIHAT_DATA():
    # Kasus jika terdapat beberapa budaya dalam penyimpanan
    if len(data_budaya) != 0 :
        for nama_warisan in data_budaya :
            print(nama_warisan)
            
    # Kasus jika tidak terdapat budaya dalam penyimpanan
    else :
        print("Tidak ditemukan data budaya")

# Fungsi untuk mendapatkan informasi detail mengenai budaya yang dicari
def CARINAMA(nama_warisan):
    # Membuat default nama warisan tidak ditemukan dan mengubahnya jika ternyata ditemukan dalam penyimpanan
    ditemukan = False
    for warisan in data_budaya :
        if warisan == nama_warisan :
            ditemukan = True
    
    # Menampilkan data-data yang ada pada budaya yang dicari
    if ditemukan :
        print(nama_warisan, end = ", ")
        for detail_warisan in data_budaya[nama_warisan]:
            if detail_warisan != data_budaya[nama_warisan][-1]:
                print(detail_warisan, end = ", ")
            else :
                print(detail_warisan)
    
    # Menampilkan pesan bahwa budaya yang dicari tidak ditemukan
    else :
        print(nama_warisan, "tidak ditemukan")

# Fungsi untuk mendapatkan informasi budaya yang termasuk dalam tipe tersebut
def CARITIPE(nama_tipe):
    # Membuat default bahwa tipe tidak ditemukan
    ditemukan = False
    jumlah = 0
    
    # Memeriksa dan menghitung tipe budaya yang dicari
    for nama_warisan in data_budaya:
        detail_warisan = data_budaya[nama_warisan]
        if detail_warisan[0] == nama_tipe :
            ditemukan = True
            jumlah += 1
            print(nama_warisan, end = ", ")
            
            # Menampilkan detail dari budaya yang termasuk dalam tipe yang dimaksud
            for detail_warisan in data_budaya[nama_warisan]:
                if detail_warisan != data_budaya[nama_warisan][-1]:
                    print(detail_warisan, end = ", ")
                else :
                    print(detail_warisan)
                    
    # Menampilkan pesan kepada user apakah tipe yang dicari ditemukan atau tidak                
    if ditemukan :
        print("* Ditemukan", jumlah, nama_tipe, "*" )
    else :
        print("Tipe yang anda cari tidak ditemukan")

# Fungsi untuk mendapatkan informasi budaya yang ada di provinsi tersebut
def CARIPROV(nama_provinsi):
    # Membuat default bahwa provinsi yang dicari tidak tersedia
    ditemukan = False
    jumlah = 0
    
    # Memeriksa dan menghitung budaya provinsi yang dicari
    for nama_warisan in data_budaya:
        detail_warisan = data_budaya[nama_warisan]
        if detail_warisan[1] == nama_provinsi :
            ditemukan = True
            jumlah += 1
            print(nama_warisan, end = ", ")
            
            # Menampilkan detail dari budaya yang termasuk dalam provinsi yang dimaksud
            for detail_warisan in data_budaya[nama_warisan]:
                if detail_warisan != data_budaya[nama_warisan][-1]:
                    print(detail_warisan, end = ", ")
                else :
                    print(detail_warisan)
                    
    # Menampilkan pesan kepada user apakah provinsi yang dicari ditemukan atau tidak
    if ditemukan :
        print("* Ditemukan", jumlah, "warisan budaya *" )
    else :
        print("Provisi yang anda cari tidak ditemukan")
        
# Fungsi untuk menambahkan budaya beserta detail informasinya
def TAMBAH(data_warisan):
    # Memisahkan detail data budaya
    data_warisan = data_warisan.split(";;;")
    
    # Kasus jika jumlah detail budaya tidak memenuhi
    if len(data_warisan) != 4 :
        print("Terdapat kesalahan atau kekurangan penginputan")
        print("Ketik 1 jika anda ingin melihat daftar perintah dan ketik SELAIN 1 jika merasa tidak perlu")
        
        # Menanyakan kepada user apakah ingin melihat kembali perintah untuk memasukkan perintah dengan benar
        pilihan = input("Masukkan pilihan anda: ")
        if pilihan == "1" :
            DAFTAR_PERINTAH("1")
        perintah = input("Masukkan kembali perintah penambahan dengan benar: ")
        TAMBAH(perintah[perintah.index(" ") + 1 : ])
        
    # Menambahkan ke dalam penyimpanan dan memberi pesan keberhasilan dalam menambahkan
    else :
        data_budaya[data_warisan[0]]= data_warisan[1:]
        print(data_warisan[0], "ditambahkan")
        
# Fungsi untuk memperbarui budaya beserta detail informasinya
def UPDATE(data_warisan):
    # Memisahkan detail data budaya dan mengecek apakah sudah ada di dalam program
    data_warisan = data_warisan.split(";;;")
    nama_warisan = data_warisan[0]
    ditemukan = False
    for warisan in data_budaya :
        if warisan == nama_warisan :
            ditemukan = True
            
    if ditemukan :
        # Kasus jika jumlah detail budaya tidak memenuhi
        if len(data_warisan) != 4 :
            print("Terdapat kesalahan atau kekurangan penginputan")
            print("Ketik 1 jika anda ingin melihat daftar perintah dan ketik SELAIN 1 jika merasa tidak perlu")
            
            # Menanyakan kepada user apakah ingin melihat kembali perintah untuk memasukkan perintah dengan benar
            pilihan = input("Masukkan pilihan anda: ")
            if pilihan == "1" :
                DAFTAR_PERINTAH("1")
            perintah = input("Masukkan kembali perintah pembaruan dengan benar: ")
            TAMBAH(perintah[perintah.index(" ") + 1 : ])
        
        # Memperbarui data yang sudah ada dan memberi pesan keberhasilan dalam memperbarui
        else :
            data_budaya[data_warisan[0]]= data_warisan[1:]
            print(data_warisan[0], "diperbarui")

    else :
        print("Maaf, data yang ingin anda ubah tidak ada dalam program")
        
# Fungsi untuk menghapus budaya beserta detail informasinya
def HAPUS(nama_warisan):
    # Menyoba menghapus suatu data dari penyimpanan
    try :
        del data_budaya[nama_warisan]
        print(nama_warisan, "dihapus")
        
    # Penanganan eksepsi jika data tidak ditemukan dalam penyimpanan
    except KeyError :
        print("Nama budaya tersebut memang tidak terdaftar")
    
# Fungsi untuk menampilkan jumlah budaya yang tersedia di dalam program ini    
def STAT():
    print("Di program ini terdapat", len(data_budaya), "warisan budaya")
    
# Fungsi untuk menampilkan jumlah dari masing-masing tipe budaya yang ada di program ini
def STATTIPE():
    # Kasus jika terdapat data dalam penyimpanan
    if len(data_budaya) != 0 :  
        
        # Menghitung masing-masing jumlah tipe budaya
        jumlah_tipe_warisan = {}
        for nama_warisan in data_budaya :
            tipe_warisan = data_budaya[nama_warisan][0] 
            if  tipe_warisan not in jumlah_tipe_warisan :
                jumlah_tipe_warisan[tipe_warisan] = 1
            else :
                jumlah_tipe_warisan[tipe_warisan] += 1
        
        # Mengurutkan dan menampilkan tipe budaya dari yang jumlah yang terbanyak        
        stat_tipe = sorted([(jumlah, tipe) for tipe, jumlah in jumlah_tipe_warisan.items()], reverse = True)
        statistik_tipe = [(tipe,jumlah) for jumlah, tipe in stat_tipe]
        print(statistik_tipe)
        
    # Memberi pesan jika tidak terdapat data dalam penyimpanan
    else :
        print("Tipe yang anda cari tidak terdapat dalam program")

# Fungsi untuk menampilkan jumlah budaya dari masing-masing provinsi yang ada di program ini 
def STATPROV():    
    # Kasus jika terdapat data dalam penyimpanan
    if len(data_budaya) != 0 :
        
        # Menghitung jumlah budaya per provinsi
        jumlah_warisan_provinsi = {}
        for nama_warisan in data_budaya :
            provinsi_warisan = data_budaya[nama_warisan][1] 
            if  provinsi_warisan not in jumlah_warisan_provinsi :
                jumlah_warisan_provinsi[provinsi_warisan] = 1
            else :
                jumlah_warisan_provinsi[provinsi_warisan] += 1
                
        # Mengurutkan provinsi berdasarkan jumlah budaya dari yang terbanyak
        stat_prov = sorted([(jumlah, prov) for prov, jumlah in jumlah_warisan_provinsi.items()], reverse = True)
        statistik_provinsi = [(prov,jumlah) for jumlah, prov in stat_prov]
        print(statistik_provinsi)
    
    # Memberi pesan jika tidak terdapat data dalam penyimpanan    
    else :
        print("Provinsi yang anda cari tidak terdapat dalam program")
    
# Fungsi yang digunakan untuk menyiapkan data yang akan diekspor
def PERSIAPAN_EKSPOR():
    # Memasukkan data sesuai format agar bisa diekspor
    data = []
    for i, j in data_budaya.items():
        list_elemen = []
        list_elemen.append(i)
        for k in j :
            list_elemen.append(k)
        data.append(list_elemen)
    
    # Mengembalikan data yang sudah sesuai format
    return data

# Fungsi yang digunakan untuk mengekspor file
def EKSPOR(nama_file, data_ekspor):
    # Mengekspor data-data ke dalam file
    with open(nama_file, 'w', newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(data_ekspor)
    
    # Memberi pesan keberhasilan dalam mengekspor
    print("EKSPOR berhasil dilakukan!")
    
# Program utama 
if __name__ == "__main__" :
    # Ucapan selamat datang dan memberi 2 pilihan di awal program
    print("Selamat Datang di Program Data Budaya Indonesia!")
    print("Ketik 1 untuk melihat daftar perintah yang bisa dikerjakan oleh program ini!")
    print("Ketik 2 untuk menjalankan program!")
    
    # Meminta user memasukkan pilihannya
    while True:
        pilihan = input("Masukkan pilihan anda: ") 
        DAFTAR_PERINTAH(pilihan)
        if pilihan == "1" or pilihan == "2" :
            break
    
    # Meminta user memasukkan perintah yang diinginkannya
    perintah = input("Masukkan perintah yang ingin anda lakukan: ")
    while perintah :
        
        # Mencoba menjalankan perintah yang dimasukkan
        try :
            if "IMPOR" in perintah :
                data_budaya = IMPOR(perintah[perintah.index(" ") + 1 : ])
                print("Terimpor", len(data_budaya), "baris")
                
            elif perintah == "LIHAT":
                LIHAT_DATA()
                
            elif "CARINAMA" in perintah :
                CARINAMA(perintah[perintah.index(" ") + 1 : ].title())
                
            elif "CARITIPE" in perintah :
                CARITIPE(perintah[perintah.index(" ") + 1 : ].title())
                
            elif "CARIPROV" in perintah :
                CARIPROV(perintah[perintah.index(" ") + 1 : ].title())
                
            elif "TAMBAH" in perintah :
                TAMBAH(perintah[perintah.index(" ") + 1 : ])
                
            elif "UPDATE" in perintah :
                UPDATE(perintah[perintah.index(" ") + 1 : ])
                
            elif "HAPUS" in perintah :
                HAPUS(perintah[perintah.index(" ") + 1 : ].title())
                
            elif perintah == "STAT" :
                STAT()
                
            elif perintah == "STATTIPE" :
                STATTIPE()
                
            elif perintah == "STATPROV":
                STATPROV()
                
            elif "EKSPOR" in perintah :
                data_ekspor = PERSIAPAN_EKSPOR()
                EKSPOR(perintah[perintah.index(" ") + 1 : ], data_ekspor)
                
            elif perintah == "KELUAR" :
                print("Matur nuwun kanggo nggunakake program kami!")
                print("Aja lali tresna warisan budaya Indonesia!")
                break
            
            # Menangani kasus jika terdapat ketidaksesuaian dengan daftar perintah
            else :
                print("Instruksi anda tidak dikenali, coba perhatikan kembali daftar perintah :)")
                print("Ketik 1 jika anda ingin melihat daftar perintah dan ketik SELAIN 1 jika merasa tidak perlu")
                pilihan = input("Masukkan pilihan anda: ")
                if pilihan == "1" :
                    DAFTAR_PERINTAH("1")
                
        # Menangani kasus untuk perintah yang kurang lengkap
        except ValueError:
            print("Perintah yang anda masukkan kurang lengkap")
            
        perintah = input("Masukkan perintah yang ingin anda lakukan: ")
