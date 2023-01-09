# a 'range()' fg előállírja az egész számokat a paraméterben megadott két szám között; zárt - nyílt intervallumban
# pl.: range(6, 10) -> [6, 7, 8, 9]

# ha csak egy paramétert adok neki, akkor az az intervallum végét fogja jelenteni, és az intervallum eleje 0 (nulla) lesz:
# pl.: range(5) -> [0, 1, 2, 3, 4]

# tehát ha szeretnénk csinálni egy ciklust, ami pontosan 5x fut le, akkor az így fog kinézni:
# for x in range(5): [kód, amit 5x isméptlünk]

for n in range(10):
    print(f'{n}: Juhász Zoltán')