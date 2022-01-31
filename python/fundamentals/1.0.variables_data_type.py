#https://runestone.academy/
#Değişkenler
""" 
    Python'da konsola ya da bir python dosyasına 50 gibi bir değer girip çalıştırdığınızda
    programın çalıştığını göreceksiniz. Ancak bu değeri daha sonra kullanabilmek için bir 
    saklama alanına ihtiyaç duyacaksınız. İşte burada bize yardımcı olacak kelime değişkenler.
    Sistem değer değişken eşlemesi yapar ve programda değişkeni çağırdığınız zaman bu eşleşme sayesinde
    ihtiyacınız olan değer size getirilir.
    Python da değişkenler, diğer dillerde olduğu gibi veri tipini yazıp daha sonra 
    değişkeni tanımlamıyoruz. Direk değişkeni tanımlayıp herhangi bir değere 
    eşitliyoruz.
"""


x = 10
y = -5
sehir = "istanbul"
ulke = "turkiye"
z = 10.5


#Değişken İsimlendirme Kuralları
""" Sayı ile başlayamaz.
    Boşluk ve özel karakterler(?,!,],&,...) içeremez.
    Programlama diline ait anahtar kelimelerden (keyword) oluşamaz. """


#İlkel Veri Tipleri
""" String
    integer
    float
    bool 
    değişkenlerin hangi veri tipine ait olduğunu 'type' fonksiyonu ile anlayabiliriz."""

cicek = "gonca"
number = 155
weight = 85.5
sure = True
print(type(number))


#Boolean Veri Tipi
""" True (Doğru) ya da False (Yanlış) değer alan bir veri tipidir. Genelde bool değer tanımlamayız,
    bool değer döndüren yapılar tanımlarız. Bu yapıları karşılaştırma (comparison) operatörleri ile gerçekleştiririz.
    Karşılaştırma operatörlerine operatörler konusunda değinilmiştir. """

print(type(True))
a = True
print(a)
b = 1 < 3 # Küçük mü karşılaştırma operatörü
print(b)


#Complex Veri Tipi
""" Matematikten de bildiğimiz karmaşık sayılardır. Gerçek sanal olmak üzere iki kısmı olan sayılardır.
    Python da buna özgü bir veri tipi olan complex ile tanımlanmıştır. Örnek.: 1 + 3j 
    real : karmaşık sayının reel kısmını almamızı sağlar.
    imag : karmaşık sayının sanal kısmını almamızı sağlar."""

a = 1 +3j
b = 4 + 3j
print(a)
print(type(a))
c = a  + b
print(c)
print(c.real,c.imag)


#Veri Tipi Dönüşümleri
""" Python dilinde bir veri tipini diğer bir veri tipine dönüştürmek mümkündür. Örneğin: string -> int, int -> string, float -> int, vb.

    str() : Herhangi bir değişkeni stringe çevirir.
    int() : Integer veri türüne uygun değerleri integer'a çevirir.
    float() : Float veri türüne uygun değerleri float'a çevirir.
    bool() : Bool veri türüne uygun değerleri bool'a çevirir."""

number = 55
coman = 15.9
isSure = False

# Int to Float
int_to_float = float(number)
print(int_to_float)
print(type(int_to_float))

# Int to String
int_to_string = str(number)
print(int_to_string)
print(type(int_to_string))

# Int to Bool
int_to_bool = bool(1) # 1 ve üst değerler True değer verir, 0 False değer verir.
print(int_to_bool)
print(type(int_to_bool))


# Float to Int
float_to_int = int(coman)
print(float_to_int)
print(type(float_to_int))

# Float to String
float_to_string = str(coman)
print(float_to_string)
print(type(float_to_string))

# Float to Bool
int_to_bool = bool(0.0) # 1.0 ve üst değerler True değer verir, 0.0 False değer verir.
print(int_to_bool)
print(type(int_to_bool))

# String to Int
string_to_int = int("45")
print(string_to_int)
print(type(string_to_int))

# String to Float
string_to_float = float("45.8")
print(string_to_float)
print(type(string_to_float))

# String to Bool
string_to_bool = bool("") # Veri yoksa False, veri varsa True
print(string_to_bool)
print(type(string_to_bool))

# Bool to Int
bool_to_int = int(False) # False = 0 | True = 1
print(bool_to_int)
print(type(bool_to_int))

# Bool to Float
bool_to_float = float(True) # False = 0.0 | True = 1.0
print(bool_to_float)
print(type(bool_to_float))

# Bool to String
bool_to_string = str(True) # False = "False" | True = "True"
print(bool_to_string)
print(type(bool_to_string))


#Expressions and Statements
""" Değişkenler, değerler, operator işlemleri, fonksiyon çağrımları vb. bunlar expression'dır.
    Fonksiyonlar, atama operatörü, if, while, else gibi kavramlar ise statements'dır. Expression syntax ifadesini
    oluşturuken, statements ise işlevsel değişikliklere sebebiyet verir."""