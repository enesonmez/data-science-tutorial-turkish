""" Kod yazarken devamlı hatalar çıkar ve biz bunu konsoldan hata mesajı olarak
    alırız. Bu hata mesajları kullanıcı tarafından anlaşılmaz ve programı 
    yarıda keser. Peki bu mesajları yakalayıp kendi istediğimiz çıktıları ya da
    hataya göre yapılması gereken işlemleri programa yaptırmayız mı?
    Tabiki yaptırırız. Nasıl yapıldığına gelin birlikte bakalım. """

#try-except Hata Ayıklama
""" Bu blok yapısında try içine yazılanlar hata olmadığı müddetçe yapılacak
işlemlerdir. except içine yazılanlar ise hata çıkarsa yapılacak işlemlerdir."""
try:
    print(2/0)
except:
    print("Büyük ihtimal 0'a bölünme hatası")

#Belirili Bir Hatayı Yakalamak
try:
    print(2/0)
except IndexError:
    print("Bu pozisyonda eleman bulunmuyor.")
except (TypeError,ImportError):
    pass
except ZeroDivisionError:
    print("0' bölünme  hatası")
except:
    print("Bir hata oluştu.") 

#else ve finally
""" else hata yakalanamazsa çalışacak bloktur. Kullanımı sık görülmez. 
    Finally hata olsun olmasın her türlü çalışan yapıdır. Finally genelde bellekte
    kullanılan kaynakların serbest bırakılmasında kullanılır. """

def bol(liste):
    for sayi in liste:
        print(sayi/8)
try:
    liste = [15,45,11,"a"]
    bol(liste)
except:
    print("Hata oluştu...")
else:
    print("Hata oluşmadı..")
finally:
    print("Hata mesajı almadan bitirdik :)")

#raise Komutu
""" İstenildiği zamanda suni hata mesajı vermemize yarayan bir komuttur. Ortada hata
    olsa da olmasa da bu komut ile ekrana hata mesajlarından birini bastırabiliyoruz."""

sayi = int(input("Çift sayı gir : "))
"""
if sayi % 2 == 0:
    pass
else:
    raise ValueError("Çift sayı gir diye boşuna mı yazdım oraya!!!")"""

#asıl kullanım  şekli
try:
    if sayi % 2 == 0:
        pass
    else:
        raise ValueError("Çift sayı gir diye boşuna mı yazdım oraya!!!")
except ValueError as hatamesaji:
    print("Hata mesajı : " + str(hatamesaji))

#Hata Tipleri
""" Hata tipleri üç ana başlıkta toplanır:
    1. Syntax error: Bu hatalar genellikle Python sözdiziminin yanlış yazılması ile meydana
    gelir. Doğal bir dilde kelimeyi yanlış yazmak gibi düşünebilirsiniz.
    2. Runtime error: Program çalışırken aldığınız yanış değer ataması (ValueError), 0'a bölme hatası
    (divisonZeroError) gibi hatalar runtime error hatalarıdır.
    3. Semantic error: Bundan önceki iki madde compiler ve interpreter ile tespit edilirdi. Bu hata türü
    mantıksal hatadır. Programınızda yaptığınız mantıksal bir sorundur. Gösterim hataları, Matematiksel 
    işlem hataları, dosya işlemlerindeki dosyanın üstüne yazmak isterken devamlı silip yazmak gibi hatalar.
    Bazen semantic hatalar compiler'a takılır ve hata çıktısı alabilirsiniz. 

"""