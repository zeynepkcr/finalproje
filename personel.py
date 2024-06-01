class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.personel_no= personel_no
        self.ad= ad
        self.soyad= soyad
        self.departman= departman
        self.maas= maas

    def __str__(self):
        return f"{self.personel_no} / {self.ad} {self.soyad} / {self.departman} / {self.maas}"