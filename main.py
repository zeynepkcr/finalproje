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