from personel import Personel 

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self._uzmanlik= uzmanlik
        self._deneyim_yili= deneyim_yili
        self._hastane= hastane

    @property
    def personel_no(self):
        return self._personel_no
    @personel_no.setter
    def personel_no(self, value):
        if value==0:
            raise ValueError("4 haneli personel numarasini giriniz.")
        self._personel_no= value

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
    def departman(self):
        return self._departman
    @departman.setter
    def departman(self, value):
        self._departman = value
    
    @property
    def maas(self):
        return self._maas
    @maas.setter
    def maas(self, value):
        if value<=0:
            raise ValueError("Gecerli bir maas degeri giriniz.")
        self._maas = value
    
    @property
    def uzmanlik(self):
        return self._uzmanlik
    @uzmanlik.setter
    def uzmanlik(self, value):
        self._uzmanlik = value
    
    @property
    def deneyim_yili(self):
        return self._deneyim_yili
    @deneyim_yili.setter
    def deneyim_yili(self, value):
        if value<0:
            raise ValueError("Deneyim yili sifirdan kucuk olamaz.")
        self._deneyim_yili = value
    
    @property
    def hastane(self):
        return self._hastane
    @hastane.setter
    def hastane(self, value):
        self._hastane = value

    def __str__(self):
        return f"Personel numarasi: {self._personel_no}, Ad-Soyad: {self._ad} {self._soyad}, Departman: {self._departman}, Maas: {self._maas}, Uzmanlik: {self._uzmanlik}, Deneyim yili: {self._deneyim_yili}, Hastane: {self._hastane}"
    
    
    