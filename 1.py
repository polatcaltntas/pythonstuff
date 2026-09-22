print("Boy gir")
height=int(input())
if height > 3:
    height = height / 100
print("Kilo gir")
weight=int(input())

bki = weight / (height * height)

if 25 < bki < 30:
    print("Aşırı kilolu")
    weightchange = weight - (25 * (height * height))
    print("vermeniz gereken kilo",weightchange)
elif 18.5 < bki < 25:
    print("sağlıklı kilolu")
elif bki < 18.5:
    print("aşırı zayıf")
    weightchange = weight -  (18.5 * height * height) 
    print("almanız gereken kilo",weightchange)
else:
    print("obez")
    weightchange = weight - (25 * height * height)
    print("vermeniz gereken kilo",weightchange)