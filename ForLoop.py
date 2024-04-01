# python da for (tekrarı belirli) döngüsü ve listeler
print("*"*40)

liste = ["ali", "baki", "ceyda", "derya"]
print(liste)
print(type(liste))

print("*"*30)

print("baki" in liste)  # liste içerisinde eleman sorgusu
if "baki" in liste:
    print("mevcut")
else:
    print("mevcut değil")

print("*" * 30)

for i in liste:  # listenin döngü kullanılarak yazdırılması
    print(i)

print("*"*40)

liste2 = [1, 3, 8, 11, 23]
print(liste2)
print(type(liste2))
for i in liste2:
    print(f"*{i}*")  # f string ile sonuçları biçimlendirme

print("*"*40)

liste3 = "python"  # str ifadeyi for döngüsüyle kullanma
print(liste3)
print(type(liste3))
for i in liste3:
    print(i)

print("*"*40)

demet = (1, 5, 3, 4)  # tuple veri tipi
print(demet)
print(type(demet))
for i in demet:
    print(i)

print("*"*40)

for i in range(51):
    if i % 5 == 0:
        print(i)

print("*" * 40)

for i in range(10, 30, 4):  # 10 dan 30'akadar 4'er ekleyerek 3'e bölünebilen sayılar
    if i % 3 == 0:  # 10,14,18,22,26 sayıları arasından 3'e bölünenleri seçer
        print(i)  # sonuçta sadec 18 sayısını verir

print("*" * 40)

for i in range(40, 10, -3):  # 40 dan 10'akadar 3'er çıkararak 5'e bölünebilen sayılar
    if i % 5 == 0:  # 40,37,34,31,28,25,22,19,16,13 sayıları arasından 5'e bölünenleri seçer
        print(i)  # sonuçta 40 ve 25 sayılarını verir

print("*" * 40)

a = list(range(15))  # range sınıfı liste sınıfına dönüştürülebiliyor
print(a)
b = list(range(15, 25))
print(b)
c = list(range(15, 45, 4))
print(c)





