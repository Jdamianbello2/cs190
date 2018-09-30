factors = []

b = False
while b == False:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        b = True

for factor in range(1, num+1):
    if num % factor == 0:
        factors.append(factor)
print(factors)