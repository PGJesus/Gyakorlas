import random

numbers = []
for number in range(50):
    numbers.append(random.randint(-60, 100))
print("Generált számok:", numbers)

product = 1
for num in numbers:
    product *= num
print("A számok szorzata: ", product)

last_index_div_5_7 = None
for i in range(len(numbers)):
    if numbers[i] % 5 ==0 or numbers[i] % 7 == 0:
        last_index_div_5_7 = i
print("Az utolsó 5-el/7-el oszttható szám: ", last_index_div_5_7)

last_index_div_3_7 = None
for i in range(len(numbers)):
    if numbers[i] % 3 ==0 and numbers[i] % 7 == 0:
        last_index_div_3_7 = i
        break
print("Az utolsó 3-el/7-el oszttható szám: ", last_index_div_3_7)