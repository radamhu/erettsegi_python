print('1. feladat')
mondat = input('Add meg a mondatot! ')

print('\n2. feladat')
kiszurendo = ' ,.;?!'
betuk = []
for karakter in mondat:
    if karakter  not in kiszurendo:
        betuk.append(karakter)
# lista értelmezés NEW method
#betuk = [karakter for karakter in mondat if karakter not in kiszurendo]
print(f'A mondatban előforduló betűk száma: {len(betuk)}')

print('\n3. feladat')
szavak = mondat[:-1].lower().split()
print(f'A szavak száma: {len(szavak)}.')

print('\n4. feladat')
maganhangzok = 'aeiou'
mghz_db = 0
for karakter in mondat:
    if karakter in maganhangzok:
        mghz_db += 1
print(f'A mondatban előforduló magánhangzók száma: {mghz_db}.')

print('\n5. feladat')
leghosszabb = ''
max_hossz = 0
for szo in szavak:
    if max_hossz < len(szo):
        max_hossz = len(szo)
        leghosszabb = szo
print(f'A leghosszabb szó a(z) {leghosszabb}, ami {max_hossz} betűből áll.')
# leghosszabb = max(szavak, key=len)
# print(f'A leghoszabbb szó a(z) {leghosszabb} {len(leghosszabb)} betűből áll.')

print('\n6. feladat')
keresett = input('Add meg a keresett szót! ')
if keresett.lower() in szavak:
    print('A keresett szó előfordul a mondatban.')
else:
    print('A keresett szó nem fordul elő a mondatban.')
    
    