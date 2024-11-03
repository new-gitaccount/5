son = int(input("Bir son kiriting: "))
summa = 0

for i in range(1, son + 1):
    summa += i

print(summa)
matn = input("Matn kiriting: ")
bosh_harf = ""
kichik_harf = ""

for harf in matn:
    if harf.isupper():
        bosh_harf += harf
    elif harf.islower():
        kichik_harf += harf

print(f'"{bosh_harf}", "{kichik_harf}"')

matn = input("Matn kiriting: ")
bosh_harf = ""
kichik_harf = ""

for harf in matn:
    if harf.isupper():
        bosh_harf += harf
    elif harf.islower():
        kichik_harf += harf

print(f'"{bosh_harf} => {len(bosh_harf)}ta", "{kichik_harf} => {len(kichik_harf)}ta"')

matn = input("Matn kiriting: ")
bosh_harf = ""
kichik_harf = ""
raqamlar = ""

for harf in matn:
    if harf.isupper():
        bosh_harf += harf
    elif harf.islower():
        kichik_harf += harf
    elif harf.isdigit():
        raqamlar += harf

print(f'"{bosh_harf} => {len(bosh_harf)}ta", "{kichik_harf} => {len(kichik_harf)}ta", "{raqamlar} => {len(raqamlar)}ta"')
