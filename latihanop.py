#Operator
#Operator Aretmatika
a = 5
b = 3
a = 2
a = 6
b = 4
c = 9
penjumlahan = a + b + c
sisabagi = a % b
perkalian = a * b * c
pembagian = c / b
pengurangan = a - b
print(f"hasil penjumlahan {a} + {b} + {c} = {penjumlahan}")
print(f"sisa bagi {a} mod {b} = {sisabagi}")
print(f"hasil kali {a} * {b} * {c} = {perkalian}")
print(f"hasil bagi {c} / {b} = {pembagian}")
print(f"hasil pengurangan {a} - {b} = {pengurangan}")

#Operator Assignment
a += 2 
b *= 5
c %= 2
print("hasil dari a += 2:", a)
print("hasil dari b *= 5:", b)
print("hasil dari c %= 2:", c)

#Operator Perbandingan
x = 4
y = 7
print(x == y)
print(x != y)
print(x < y)
print(x >= y)

#Operator Logika
m = 3
print(m < 2 and m < 5)
print(m > 4 or m < 7)
print(not(m < 5 and m > 2))