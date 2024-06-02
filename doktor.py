from personel import Personel 

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.uzmanlik= uzmanlik
        self.deneyim_yili= deneyim_yili
        self.hastane= hastane

    def maas_arttir():
        if deneyim_yili >= 5 :
            maas = maas + (maas*0,5)
#           return maas