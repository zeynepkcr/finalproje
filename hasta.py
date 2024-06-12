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
    
    @property
    def hasta_no(self):
        return self.hasta_no
    @hasta_no.setter
    def hasta_no(self, value):
        if value<=0 or len(value)<4:
            raise ValueError("4 haneli hasta numarasini giriniz.")
        self.hasta_no = value

    @property
    def ad(self):
        return self.ad
    @ad.setter
    def ad(self, value):
        self.ad = value

    @property
    def soyad(self):
        return self.soyad
    @soyad.setter
    def soyad(self, value):
        self.soyad = value

    @property
    def dogum_tarihi(self):
        return self.dogum_tarihi
    @dogum_tarihi.setter
    def dogum_tarihi(self, value):
        self.dogum_tarihi = value

    @property
    def hastalik(self):
        return self.hastalik
    @hastalik.setter
    def hastalik(self, value):
        self.hastalik = value

    @property
    def tedavi(self):
        return self.tedavi
    @tedavi.setter
    def tedavi(self, value):
        self.tedavi = value
    