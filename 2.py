import random

columnCount = int(input("Kaç kolon oynamak istersiniz?: "))
excludeInput = input("Hariç tutulacak sayıları giriniz (virgülle ayırarak): ")
includeInput = input("Her kolonda olmasını istediğiniz şanslı sayıyı giriniz (yoksa boş bırakın): ")

excludedNumbers = []

if excludeInput != "":
    splitNumbers = excludeInput.split(",")
    for numberText in splitNumbers:
        excludedNumbers.append(int(numberText.strip()))

luckyNumber = 0

if includeInput != "":
    luckyNumber = int(includeInput)

coupon = []

for i in range(columnCount):
    column = []

    if luckyNumber != 0:
        column.append(luckyNumber)

    for j in range(100):
        if len(column) == 6:
            break

        randomNumber = random.randint(1, 90)

        if randomNumber not in column and randomNumber not in excludedNumbers:
            column.append(randomNumber)

    coupon.append(column)

print("\nOluşturulan Kupon:")
print(coupon)

print("\nKolonların Alt Alta Görünümü:")
for i in range(len(coupon)):
    print(f"{i + 1}. Kolon: {coupon[i]}")
