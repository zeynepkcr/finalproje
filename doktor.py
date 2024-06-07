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
    def doktor(self):
        return 