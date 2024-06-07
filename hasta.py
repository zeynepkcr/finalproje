class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.hasta_no= hasta_no
        self.ad= ad
        self.soyad= soyad
        self.dogum_tarihi= dogum_tarihi
        self.hastalik= hastalik
        self.tedavi= tedavi

    def __str__(self):
        return f"Hasta numarasi: {self.hasta_no}, Ad-Soyad: {self.ad}  {self.soyad}, 
        Dogum tarihi: {self.dogum_tarihi}, Hastalik: {self.hastalik}, Tedavi: {self.tedavi})"