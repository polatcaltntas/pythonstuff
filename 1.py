print("Boy gir")
height=int(input())
print("Kilo gir")
weight=int(input())

bki = weight / (height * height)

if 25 < bki < 30:
    print("Aşırı kilolu")
    weightchange = ((bki * (height * height)) - (25 * (height * height)))
    print("vermeniz gereken kilo",weightchange)
elif 18.5 < bki < 25:
    print("sağlıklı kilolu")
elif bki < 18.5:
    print("aşırı zayıf")
    weightchange = (25 * height * height) -  (bki * height * height) 
    print("almanız gereken kilo",weightchange)
else:
    print("obez")
    weightchange = (bki * height * height) - (25 * height * height)
    print("vermeniz gereken kilo",weightchange)

