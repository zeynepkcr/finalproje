#hasta sınıfını oluşturuyoruz
class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self._hasta_no= hasta_no
        self._ad= ad
        self._soyad= soyad
        self._dogum_tarihi= dogum_tarihi
        self._hastalik= hastalik
        self._tedavi= tedavi
    #hasta sınıfının özellikleri için get ve set metotlarını ekliyoruz
    @property
    def hasta_no(self):
        return self._hasta_no
    @hasta_no.setter
    def hasta_no(self, value):
        if value<=0:
            raise ValueError("4 haneli hasta numarasini giriniz.")
        self._hasta_no = value

    @property
    def ad(self):
        return self._ad
    @ad.setter
    def ad(self, value):
        self._ad = value

    @property
    def soyad(self):
        return self._soyad
    @soyad.setter
    def soyad(self, value):
        self._soyad = value

    @property
    def dogum_tarihi(self):
        return self._dogum_tarihi
    @dogum_tarihi.setter
    def dogum_tarihi(self, value):
        self._dogum_tarihi = value

    @property
    def hastalik(self):
        return self._hastalik
    @hastalik.setter
    def hastalik(self, value):
        self._hastalik = value

    @property
    def tedavi(self):
        return self._tedavi
    @tedavi.setter
    def tedavi(self, value):
        self._tedavi = value
#özellikleri str metodu ile yazdırıyoruz
    def __str__(self):
        return f"Hasta numarasi: {self._hasta_no}, Ad-Soyad: {self._ad}  {self._soyad}, Dogum tarihi: {self._dogum_tarihi}, Hastalik: {self._hastalik}, Tedavi: {self._tedavi})"
    