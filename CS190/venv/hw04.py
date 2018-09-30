bottles = 99

while bottles > 1:
    if bottles > 2:
        print(bottles, "bottles of beer on the wall,", bottles, "bottles of beer. Take one down, pass it around", bottles - 1, "bottles of beer on the wall")
    if bottles == 2:
        print(bottles, "bottles of beer on the wall,", bottles, "bottles of beer. Take one down, pass it around", bottles - 1, "bottle of beer on the wall.")

    bottles -= 1

while bottles <= 1:
    if bottles == 1:
        print(bottles, "bottle of beer on the wall,", bottles, "bottle of beer. Take one down pass it around 0 bottles of beer on the wall.")
    if bottles == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. Get some help.")
    bottles -=1