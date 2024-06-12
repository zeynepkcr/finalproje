from personel import Personel 

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.uzmanlik= uzmanlik
        self.deneyim_yili= deneyim_yili
        self.hastane= hastane

    def __str__(self):
        return f"Personel numarasi: {self.personel_no}, Ad-Soyad: {self.ad} {self.soyad},
        Departman: {self.departman}, Maas: {self.maas}, Uzmanlik: {self.uzmanlik}, 
        Deneyim yili: {self.deneyim_yili}, Hastane: {self.hastane}"

    @property
    def personel_no(self):
        return self.personel_no
    @personel_no.setter
    def personel_no(self, value):
        if value==0 or len(value)<4:
            raise ValueError("4 haneli personel numarasini giriniz.")
        self.personel_no= value

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
    def departman(self):
        return self.departman
    @departman.setter
    def departman(self, value):
        self.departman = value
    
    @property
    def maas(self):
        return self.maas
    @maas.setter
    def maas(self, value):
        if value<=0:
            raise ValueError("Gecerli bir maas degeri giriniz.")
        self.maas = value
    
    @property
    def uzmanlik(self):
        return self.uzmanlik
    @uzmanlik.setter
    def uzmanlik(self, value):
        self.uzmanlik = value
    
    @property
    def deneyim_yili(self):
        return self.deneyim_yili
    @deneyim_yili.setter
    def deneyim_yili(self, value):
        if value<0:
            raise ValueError("Deneyim yili sifirdan kucuk olamaz.")
        self.deneyim_yili = value
    
    @property
    def hastane(self):
        return self.hastane
    @hastane.setter
    def hastane(self, value):
        self.hastane = value
    
    
    