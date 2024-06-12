class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self._personel_no= personel_no
        self._ad= ad
        self._soyad= soyad
        self._departman= departman
        self._maas= maas
    
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

    def __str__(self):
        return f"Personel numarasi: {self._personel_no}, Ad-soyad: {self._ad} {self._soyad}, Departman: {self._departman}, Maas: {self._maas}"