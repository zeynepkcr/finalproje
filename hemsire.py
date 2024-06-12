from personel import Personel

class Hemsire (Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad,soyad, departman, maas)
        self.calisma_saati= calisma_saati
        self.sertifika= sertifika
        self.hastane= hastane

    def __str__(self):
        return f"Personel numarasi: {self.personel_no}, Ad-Soyad. {self.ad} {self.soyad},
        Departman: {self.departman}, Maas: {self.maas}, Toplam calisma saati: {self.calisma_saati},
        Sertifika: {self.sertifika}, Hastane: {self.hastane}"
    
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
    def calisma_saati(self):
        return self.calisma_saati
    @calisma_saati.setter
    def calisma_saati(self, value):
        if value<0:
            raise ValueError("Calisma saati sifirdan az olamaz.")
        self.calisma_saati = value

    @property
    def sertifika(self):
        return self.sertifika
    @sertifika.setter
    def sertifika(self, value):
        self.sertifika = value

    @property
    def hastane(self):
        return self.hastane
    @hastane.setter
    def hastane(self, value):
        self.hastane = value
