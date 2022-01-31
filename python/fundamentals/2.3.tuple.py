""" 
    Listeden çok fazla bir farkı yoktur. İlkel veri tiplerini ve koleksiyonları
    kendi içinde barındıran koleksiyon veri tipidir.
    Listelerden tek bir farkı vardır. O da eklenen elemanlar değiştirilemez. (unmutable)
"""


demet = (1,2,3,4,5,6)
demet_one = 1,2,3,4,5
karisik_demet = ("yazi",155,12.5,[45,21,45],{"ev":"home","at":"horse"})


#Demette Elemana Ulaşmak (İndisleme)
print(demet[0]) # [-1] veya [len(list_name) - 1] ile son liste elemanına ulaşabiliyoruz.


#Tuple Slice (Dilimlemek)
""" Belli tuple eleman aralığını almamızı sağlar."""
demet2 = demet[:2] #Başlangı. indisinden 2. indise kadar değerleri alıp demet2'ye atar.


#Demete Elaman Ekleme
""" 
    Demet tek bir değer ile oluşmaz isminden de ötürü. Ancak bazen mecbur oluşturmak zorunda
    kalabiliyoruz. Oluştururken aşağıdaki yöntemi uyguluyoruz.
"""

demet += (7,)
print(demet)


#Demetleri Birleştirme
extends_tuple = demet + demet_one
print(extends_tuple)


#Demet Metodları
print(extends_tuple.count(1))
print(extends_tuple.index(5))

empty_tuple = tuple()
full_tuple = tuple([1,2,3,4])

print(empty_tuple)
print(full_tuple)


# Döngülerde Tuple'lar içinde dolaşma
""" 
    Tuple içindeki değerleri direk değişkenlere atayabiliyoruz. Bu sayede for döngüsünde 
    değerleri değişkenlere atayarak işlemlerimizi gerçekleştiriyoruz.
"""
authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)


#Enumerate
""" 
    Bazen bir listedeki elemanlerın liste sırasına ihtiyaç duyarız işte bu noktada 
    enumerate yardımımıza yetişir ve bize istediğimizi verir. bu fonkisyon obje return 
    eder ve liste elemanı ve indisini bir demette tutar.
"""
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)