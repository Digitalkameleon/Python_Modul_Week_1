#soru1_cevap

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sayilar)

#soru2_cevap
n = int(input("Bir sayı girin: "))

for i in range(0, n+1, 2):  # 0'dan n'e kadar 2'şer artırarak döner
    print(i)
---------------------------------------------------------------------------
n = int(input("Bir sayı girin: "))

i = 0
while i <= n:
    print(i)
    i += 2 

#soru3_cevap

start = int(input("Başlangıç değerini girin: "))
end = int(input("Bitiş değerini girin: "))

for i in range(start, end + 1):
    print(i)
  
#soru4_cevap

number = int(input("Bir sayı girin: "))

if number % 2 == 0:
    print("Çift sayı")
else:
    print("Tek sayı")
  
#soru5_cevap

number = int(input("Bir pozitif tam sayı girin: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Faktöriyel:", factorial)

#soru6_cevap

number = int(input("Bir sayı girin: "))

if number > 1:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"{number} bir asal sayıdır.")
else:
    print(f"{number} bir asal sayı değildir.")
  
#soru7_cevap

limit = int(input("Fibonacci dizisi için bir üst sınır girin: "))

fibonacci_sequence = []

a, b = 0, 1

while a <= limit:
    fibonacci_sequence.append(a)
    a, b = b, a + b

print("Fibonacci dizisi:", fibonacci_sequence)
#soru8_cevap

kelime = input("Bir kelime girin: ")

ters_kelime = kelime[::-1]

print(ters_kelime)

#soru9_cevap

kelime = input("Bir kelime girin: ")

ters_kelime = ""

for harf in kelime:
    ters_kelime = harf + ters_kelime

if kelime == ters_kelime:
    print("Bu bir palindrom.")
else:
    print("Bu bir palindrom değil.")
  
#soru10_cevap

kilo = float(input("Kilonuzu girin (kg): "))
boy = float(input("Boyunuzu girin (metre): "))

bmi = kilo / (boy * boy)

if bmi < 25:
    print("Zayıf")
elif 25 <= bmi < 30:
    print("Normal")
elif 30 <= bmi < 40:
    print("Kilolu")
else:
    print("Fazla kilolu")
  
#soru11_cevap

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
sayi3 = float(input("Üçüncü sayıyı girin: "))

en_buyuk = sayi1  # Başlangıçta en büyük sayıyı sayi1 olarak kabul ediyoruz

if sayi2 > en_buyuk:
    en_buyuk = sayi2

if sayi3 > en_buyuk:
    en_buyuk = sayi3

print("En büyük sayı:", en_buyuk)

#soru12_cevap

for i in range(4):
    print("Ders", i + 1)
    
    vize = float(input("Vize notunu girin: "))
    final = float(input("Final notunu girin: "))
    
    ortalama = vize * 0.4 + final * 0.6
    
    if ortalama < 50:
        print("FAILED")
    else:
        print("SUCCESSFUL")

    print()
