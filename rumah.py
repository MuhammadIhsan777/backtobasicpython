class Rumah:
    
    def __init__(self, alamat, jumlah_kamar, warna, luas, sah, harga):
        self.alamat = alamat
        self.jumlah_kamar = jumlah_kamar
        self.warna= warna
        self.sah= sah
        self.luas = luas
        self.harga = harga


    # def tampilkan_info(self):
    #     status="Sah"
    #     if self.sah :
    #         status= "sah" 
    #     else:
    #         status="TIdak Sah"
        
    #     info = (
    #         "alamat: {self.alamat}",
    #         "jumlah Kamar: {self.jumlah_kamar}",
    #         "warna: {self.warna}",
    #         "luas: {self.luas} m²",
    #         "harga: Rp {self.harga:,}",
    #     )
    #     return info

    # x = Rumah("Jalan Tun Ismail", 7, "Putih", 120 , True, 750000000)
    
    rumahku = Rumah("Jalan Tun Ismail", 7, "Putih", 120 , True, 750000000)
    # print(rumahku.Tampilkan_info)
