""" 
    JSON, Javascript Object Notation kısaltmasıdır. Okunabilir bilgi saklama
    ve veri transfer formatıdır. Oldukça hafif ve esnek yapıda olduğu için en çok tercih edilen 
    veri transfer formatıdır.
    Not: json söz dizimi python daki sözlük(dictioanry) veri tipine benzer.
"""


import json


#örnek json veri şekli
veri = '{"firstname":"emre","lastname":"demir"}'
veri = json.loads(veri)#string biçimindeki jsonu, jsona çevirme

print(veri["firstname"])
print(veri["lastname"])


#Sözlüğü JSON'a Çevirme
customer = {
    "firstName":"emre",
    "lastName":"demir",
    "email":"emre@gmail.com"
}
customerJson = json.dumps(customer)
print(customerJson)


#Json Örnek Çalışma
with open("files/users.json") as users:
    data = json.load(users)#dosyadan okuma yaparken load metodu kullanılır. String için loads kullanılır.
for x in range(5):
    print(data[x]["username"])
    print(data[x]["email"])
    print(data[x]["address"]["street"])
    print(data[x]["address"]["geo"]["lat"])
    print("\n")
print(users.closed)
