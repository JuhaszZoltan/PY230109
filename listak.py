szam = 10
#         0       1       2        3
nevek = ['Ádám', 'Béla', 'Cecil', 'Dénes']
# dolgok = ['Juhász', 'Zoltán', 34, True, '1990-07-11']

print(f'lista 2-es indexű eleme: {nevek[2]}')

hossz = len(nevek)
print(f'lista elemeinek száma: {hossz}')

# új elem hozzáadása:
uj_nev = input('ír be egy nevet: ')
nevek.append(uj_nev)

print('a lista elemei hozzáadás után:')
print(nevek)
print(f'a lista hossza hozzáadás után: {len(nevek)}')

# lista elemeinek bejárása ciklussal:
for nev in nevek:
    print(nev)

# lista INDEXEINEK bejárása:
for index in range(0, len(nevek)):
    print(f'a lista {index}-as/es indexű eleme: {nevek[index]}')