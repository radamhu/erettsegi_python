epitmenyek = []
with open('./utca.txt', 'r', encoding='utf-8') as file:
    adok = file.readline().strip().split()
    adosavok = {'A': int(adok[0]), 'B': int(adok[1]), 'C': int(adok[2])}
    for sor in file:
        adatok = sor.strip().split()
        epitmeny = {'adoszam': adatok[0],
                    'utca': adatok[1],
                    'hazszam': adatok[2],
                    'adosav': adatok[3],
                    'terulet': int(adatok[4])}
        epitmenyek.append(epitmeny)
# print(adosavok)
# print(epitmenyek)

#2. feladat
print(f'2. feladat. A mintában {len(epitmenyek)} telek szerepel.')

# 3. feladat
adoszam = input('3. feladat. Egy tulajdonos adószáma: ')
talalat = False
for epitmeny in epitmenyek:
    if adoszam == epitmeny['adoszam']:
        print(epitmeny['utca'], epitmeny['hazszam'])
        talalat = True
if not talalat:
    print('Nem szerepel az adatállományban.')

# 4. feladat
def ado(ado_savonkent, adosav, alapterulet):
    ado = alapterulet * ado_savonkent[adosav]
    if ado < 10000:
        return 0
    else:
        return ado

# 5. feladat
ado_osszesites = {'A': [0, 0], 'B': [0, 0], 'C': [0, 0]}
for epitmeny in epitmenyek:
    ado_osszesites[epitmeny['adosav']][0] += 1
    ado_osszeg = ado(adosavok, epitmeny['adosav'], epitmeny['terulet'])
    ado_osszesites[epitmeny['adosav']][1] += ado_osszeg
# print(ado_osszesites)
print(f'A sávba {ado_osszesites["A"][0]} telek esik, az adó {ado_osszesites["A"][1]} Ft')
print(f'B sávba {ado_osszesites["B"][0]} telek esik, az adó {ado_osszesites["B"][1]} Ft')
print(f'C sávba {ado_osszesites["C"][0]} telek esik, az adó {ado_osszesites["C"][1]} Ft')