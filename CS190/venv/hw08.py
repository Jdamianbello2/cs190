



def diff(g):
    if g > 2.375:
        g = 2.375
    if g < 0:
        g = 0
    return g
def a(comp, attempts):
    x = ((comp / attempts) - 0.3) * 5
    y = diff(x)
    return y
def b(yds, attempts):
    y = ((yds / attempts) - 3) * 0.25
    z = diff(y)
    return z
def c(touch,attempts):
    z = (touch / attempts) * 20
    x = diff(z)
    return x
def d(inter, attempts):
    w = 2.375 - ((inter / attempts) * 25)
    s = diff(w)
    return s

def rating(a1,b1,c1,d1):
    return ((a1 + b1 + c1 + d1)/6) * 100
quart = input("Enter a quarterback's name and following stats: ")
attempts = int(input("Attempts: "))
comp = int(input("Completions: "))
touch = int(input("Touchdowns: "))
inter = int(input("Interceptions: "))
yds = int(input("Yards: "))

a1 = a(comp, attempts)
b1 = b(yds, attempts)
c1 = c(touch, attempts)
d1 = d(inter, attempts)

print(rating(a1, b1, c1, d1))