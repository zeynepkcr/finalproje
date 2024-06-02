#not1
'''__init__ metodu, Python'da bir sınıfın örneği (instance) oluşturulduğunda otomatik olarak
çağrılan ve bu sınıfın örnek özelliklerini başlatmak için kullanılan özel bir metottur.'''

#not2
'''Dekoratör, Python'da bir fonksiyonun veya metodun işlevselliğini değiştirmek veya genişletmek 
için kullanılan özel bir fonksiyondur. Dekoratörler, fonksiyonları veya metodları sararak, onların 
giriş ve çıkışlarını kontrol etmenizi sağlar. Bu, kodunuzu daha temiz, daha okunaklı ve yeniden 
kullanılabilir hale getirir. Dekoratörler, Python'da yaygın olarak kullanılan ve fonksiyonel 
programlama tarzını destekleyen güçlü bir araçtır.
Dekoratörler genellikle @ sembolü ile fonksiyon veya metodun üzerine yazılır. 
Bir dekoratör, başka bir fonksiyonu argüman olarak alan ve yeni bir fonksiyon döndüren bir fonksiyondur.'''

#not3
'''get ve set metodları (getter ve setter) bir sınıfın özelliklerine erişim ve bu özelliklerin 
değiştirilmesi işlemlerini kontrollü bir şekilde yönetmek için kullanılır. 
Getter metodları bir özelliğin değerini döndürürken, setter metodları bir özelliğin değerini 
ayarlamak için kullanılır. Bu metotlar, özelliklerin doğrudan erişilmesini ve değiştirilmesini 
engelleyerek veri kapsüllemeyi (encapsulation) sağlar.'''

class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.personel_no= personel_no
        self.ad= ad
        self.soyad= soyad
        self.departman= departman
        self.maas= maas

    def __str__(self):
        return f"{self.personel_no} / {self.ad} {self.soyad} / {self.departman} / {self.maas}"