from personel import Personel

class Hemsire (Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad,soyad, departman, maas)
        self._calisma_saati= calisma_saati
        self._sertifika= sertifika
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
    def calisma_saati(self):
        return self._calisma_saati
    @calisma_saati.setter
    def calisma_saati(self, value):
        if value<0:
            raise ValueError("Calisma saati sifirdan az olamaz.")
        self._calisma_saati = value

    @property
    def sertifika(self):
        return self._sertifika
    @sertifika.setter
    def sertifika(self, value):
        self._sertifika = value

    @property
    def hastane(self):
        return self._hastane
    @hastane.setter
    def hastane(self, value):
        self._hastane = value

    def __str__(self):
        return (f"Personel numarasi: {self._personel_no}, Ad-Soyad. {self._ad} {self._soyad}"
               f"Departman: {self._departman}, Maas: {self._maas}, Toplam calisma saati: {self._calisma_saati}"
               f"Sertifika: {self._sertifika}, Hastane: {self._hastane}")
