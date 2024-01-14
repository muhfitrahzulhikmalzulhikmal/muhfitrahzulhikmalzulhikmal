class TiketBus:
    def _init_(self, tujuan, jam, harga):
        self.tujuan = tujuan
        self.jam = jam
        self.harga = harga

class Pemesanan:
    def _init_(self):
        self.daftar_tiket = []

    def tambah_tiket(self, tujuan, jam, harga):
        self.daftar_tiket.append(TiketBus(tujuan, jam, harga))

    def hapus_tiket(self, index):
        self.daftar_tiket.pop(index)

    def tampilkan_tiket(self):
        for i, tiket in enumerate(self.daftar_tiket):
            print(f"{i+1}. Tujuan: {tiket.tujuan}, Jam: {tiket.jam}, Harga: {tiket.harga}")

    def total_harga(self):
        return sum(tiket.harga for tiket in self.daftar_tiket)

# Program pemesanan tiket bus
def program_pemesanan():
    pemesanan = Pemesanan()

    while True:
        print("\nMenu:")
        print("1. Tambah tiket")
        print("2. Hapus tiket")
        print("3. Tampilkan tiket")
        print("4. Total harga")
        print("5. Keluar")

        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            tujuan = input("Masukkan tujuan: ")
            jam = input("Masukkan jam: ")
            harga = int(input("Masukkan harga: "))
            pemesanan.tambah_tiket(tujuan, jam, harga)
        elif pilihan == 2:
            index = int(input("Masukkan nomor tiket yang ingin dihapus: ")) - 1
            pemesanan.hapus_tiket(index)
        elif pilihan == 3:
            pemesanan.tampilkan_tiket()
        elif pilihan == 4:
            print(f"Total harga: {pemesanan.total_harga()}")
        elif pilihan == 5:
            break
        else:
            print("Pilihan tidak valid.")

if _name_ == "_main_":
    program_pemesanan()