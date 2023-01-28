print('1. feladat')
fajlnev = 'konnyu.txt' # input('Adja meg a bemeneti fájl nevét!')
# átalakítjuk a bekérés pillanatában index értékké
sor = 1 #int(input('Adja meg egy sor számát! ')) - 1
oszlop = 1 #int(input('Adja meg egy oszlop számát! ')) - 1

# 2. feladat
tablazat = []
lepesek = []
with open(fajlnev, 'r') as fajl:
    for adatsor in fajl:
        adatsor = adatsor.strip().split()
        # mivel string tipusu az adatsor egy uj listában átalakítom int-é, ehhez lista értelmezést használok
        ertekek = [int(adat) for adat in adatsor]
        # most választanám szét hogy ebben a listában (konnyu.txt) 9 elem vagy 3
        if len(ertekek) == 9:
            tablazat.append(ertekek)
        else:
            lepesek.append(ertekek)
# print(f'{tablazat=}')
# print(f'{lepesek=}')

# 3. feladat