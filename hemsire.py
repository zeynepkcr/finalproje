import personel
class Hemsire (personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad,soyad, departman, maas)
        self.calisma_saati= calisma_saati
        self.sertifika= sertifika
        self.hastane= hastane