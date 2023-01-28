szakaszok = ['F5.3', 'NF1', 'F3.2', 'NF0.6', 'NF0', 'F2.1', 'NF2']

print('\n2. feladat')
km = 0
for szakasz in szakaszok:
    if szakasz[0] == 'F':
        km += float(szakasz[1:])
        #print(szakasz[1:])
    else:
        km += float(szakasz[2:])
        #print(szakasz[2:])
print(f'A verseny távja {km} km volt!')

print('\n3. feladat')
if szakaszok[-1][0] == 'F':
    print('Futva ért célba!')
else:
    print('Gyalogolva ért célba!')

print('\n4. feladat')
megallt = 0
for szakasz in szakaszok:
    if szakasz == 'NF0':
        megallt += 1
print(f'A verseny soran {megallt} alkalommal állt meg.')

print('\n5. feladat')
megszakitottak = 0
for index in range(len(szakaszok) -1):
    if szakaszok[index][0] == 'F' and szakaszok[index+1][0:2] == 'NF':
        megszakitottak += 1
print(f'A futását {megszakitottak} alkalommal szakitotta meg.')

print('\n6. feladat')
volt_olyan = False
for index in range(len(szakaszok) -1):
    if szakaszok[index][0:1] == 'NF' and float(szakaszok[index][2:]) != 0 and szakaszok[index+1] == 'NF0':
        volt_olyan = true
        break
if volt_olyan:
    print(f'Volt olyan alkalom, hogy gyaloglás közben megállt!')
else:
    print(f'Nem volt olyan alkalom, hogy gyaloglás közben megállt!')