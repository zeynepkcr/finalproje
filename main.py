from hasta import Hasta
from personel import Personel
from doktor import Doktor
from hemsire import Hemsire

personel1 = Personel(1452, "Ahmet", "Soyak", "Ortopedi", 20000)
personel2 = Personel(5789, "Sinem", "Acar", "Kardiyoloji", 20000)

doktor1 = Doktor(1234, "Ahmet", "Yılmaz", "Kardiyoloji", 10000, "Kardiyolog", 10, "Ankara Hastanesi")
doktor2 = Doktor(5678, "Ayşe", "Kaya", "Nöroloji", 12000, "Nörolog", 8, "İstanbul Hastanesi")
doktor3 = Doktor(9101, "Mehmet", "Demir", "Ortopedi", 11000, "Ortopedist", 15, "İzmir Hastanesi")

hemsire1 = Hemsire(2345, "Fatma", "Öztürk", "Pediatri", 7000, 160, "Pediatri Hemşireliği", "Ankara Hastanesi")
hemsire2 = Hemsire(6789, "Ali", "Çelik", "Onkoloji", 7500, 170, "Onkoloji Hemşireliği", "İstanbul Hastanesi")
hemsire3 = Hemsire(1122, "Zeynep", "Acar", "Acil", 6800, 180, "Acil Hemşireliği", "İzmir Hastanesi")

hasta1 = Hasta(1015, "Mehmet", "Yılmaz", "01.01.1980", "Kalp Hastalığı", "Bypass Ameliyatı")
hasta2 = Hasta(1022, "Ayşe", "Demir", "15.05.1990", "Diyabet", "İnsülin Tedavisi")
hasta3 = Hasta(1037, "Ali", "Kaya", "20.08.1975", "Hipertansiyon", "Diyet ve Egzersiz")

# Personel örneklerini yazdır
print(personel1)
print(personel2)

# Doktor örneklerini yazdır
print(doktor1)
print(doktor2)
print(doktor3)

# Hemşire örneklerini yazdır
print(hemsire1)
print(hemsire2)
print(hemsire3)

# Hasta örneklerini yazdır
print(hasta1)
print(hasta2)
print(hasta3)

#dataframe oluşturma kısmı
import pandas as pd

data = [
    [personel1.personel_no, personel1.ad, personel1.soyad, personel1.departman, personel1.maas, None, None, None, None, None, None, None, None, None],
    [personel2.personel_no, personel2.ad, personel2.soyad, personel2.departman, personel2.maas, None, None, None, None, None, None, None, None, None],
    [doktor1.personel_no, doktor1.ad, doktor1.soyad, doktor1.departman, doktor1.maas, doktor1.uzmanlik, doktor1.deneyim_yili, doktor1.hastane, None, None, None, None, None, None],
    [doktor2.personel_no, doktor2.ad, doktor2.soyad, doktor2.departman, doktor2.maas, doktor2.uzmanlik, doktor2.deneyim_yili, doktor2.hastane, None, None, None, None, None, None],
    [doktor3.personel_no, doktor3.ad, doktor3.soyad, doktor3.departman, doktor3.maas, doktor3.uzmanlik, doktor3.deneyim_yili, doktor3.hastane, None, None, None, None, None, None],
    [hemsire1.personel_no, hemsire1.ad, hemsire1.soyad, hemsire1.departman, hemsire1.maas, None, None, hemsire1.hastane, hemsire1.calisma_saati, hemsire1.sertifika, None, None, None, None],
    [hemsire2.personel_no, hemsire2.ad, hemsire2.soyad, hemsire2.departman, hemsire2.maas, None, None, hemsire2.hastane, hemsire2.calisma_saati, hemsire2.sertifika, None, None, None, None],
    [hemsire3.personel_no, hemsire3.ad, hemsire3.soyad, hemsire3.departman, hemsire3.maas, None, None, hemsire3.hastane, hemsire3.calisma_saati, hemsire3.sertifika, None, None, None, None],
    [None, hasta1.ad, hasta1.soyad, None, None, None, None, None, None, None, hasta1.hasta_no, hasta1.dogum_tarihi, hasta1.hastalik, hasta1.tedavi],
    [None, hasta2.ad, hasta2.soyad, None, None, None, None, None, None, None, hasta2.hasta_no, hasta2.dogum_tarihi, hasta2.hastalik, hasta2.tedavi],
    [None, hasta3.ad, hasta3.soyad, None, None, None, None, None, None, None, hasta3.hasta_no, hasta3.dogum_tarihi, hasta3.hastalik, hasta3.tedavi]
]

columns = [
    "personel_no", "ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastane", "calisma_saati", "sertifika", "hasta_no", "dogum_tarihi", "hastalik", "tedavi"
]

df = pd.DataFrame(data, columns=columns)

# Boş olan değişken değerleri için 0 atama
df.fillna(0, inplace=True)

# Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama
doktor_gruplama = df[df["uzmanlik"] != 0].groupby("uzmanlik").size()
print("Uzmanlik alanlarina göre doktor sayisi:")
print(doktor_gruplama)

# 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
deneyim = df[(df["deneyim_yili"] > 5) & (df["deneyim_yili"] != 0)]
print("\n5 yildan fazla deneyime sahip doktor sayisi:", len(deneyim))

# Hasta adına göre DataFrame'i alfabetik olarak sıralama
alfabetik_hasta = df[df["hasta_no"] != 0].sort_values("ad")
print("\nHasta adina göre alfabetik siralama:")
print(alfabetik_hasta)

# Maaşı 7000 TL üzerinde olan personelleri bulma
maas_yuksek_personel = df[df["maas"] > 7000]
print("\nMaaşi 7000 TL üzerinde olan personeller:")
print(maas_yuksek_personel)

# Doğum tarihi 1990 ve sonrası olan hastaları gösterme
df["dogum_tarihi"] = pd.to_datetime(df["dogum_tarihi"], errors='coerce', format='%d.%m.%Y')
dogum_1990_sonrasi = df[(df["dogum_tarihi"] >= '1990-01-01') & (df["dogum_tarihi"] != 0)]
print("\nDoğum tarihi 1990 ve sonrasi olan hastalar:")
print(dogum_1990_sonrasi)

# Var olan DataFrame'den ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastalik, tedavi bilgilerini içeren yeni bir DataFrame elde etme
yeni_df = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
print("\nYeni DataFrame:")
print(yeni_df)