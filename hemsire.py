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