#!/usr/bin/env python3

l = [
  "Gorusuke",
  "DavidFabian",
  "ItziarZG",
  "edy WOLF",
  "MarcosGaPe",
  "Jose Jimenez",
  "Borja ",
  "Jhonathan Izquierdo Higuita",
  "MiLfeR322",
  "Sebastián Espínola",
  "Matias Luna",
  "Imanol Decima",
  "MarcoCasula",
  "MaríaBohórquez",
  "Renan",
  "IvanL'olivier",
  "Shonero",
  "Luichidev",
  "Faviola Narvaez",
  "Christopher Fuentes",
  "Kuro",
  "Juan Pablo Addeo",
  "Sergio Martínez",
  "Fran Enriquez González",
  "Diana",
  "tictools",
  "ConchaAsensio",
  "Emilio_Arreaza",
  "novamix",
  "Tomas Duclos",
  "Elaya",
  "Ignacio Palominos",
  "David C.",
  "Gerardo Felipe Conrado",
  "ElXuri",
  "David Borja Martinez",
  "JaviFelices",
  "CarlesSànchez",
  "Gorusuke",
  "DavidFabian",
  "ItziarZG",
  "edy WOLF",
  "MarcosGaPe",
  "Jose Jimenez",
  "Borja ",
  "Jhonathan Izquierdo Higuita",
  "MiLfeR322",
  "Sebastián Espínola",
  "Matias Luna",
  "Imanol Decima",
  "MarcoCasula",
  "MaríaBohórquez",
  "Renan",
  "IvanL'olivier",
  "Shonero",
  "Luichidev",
  "Faviola Narvaez",
  "Christopher Fuentes",
  "Kuro",
  "Juan Pablo Addeo",
  "Sergio Martínez",
  "Fran Enriquez González",
  "Diana",
  "tictools",
  "ConchaAsensio",
  "Emilio_Arreaza",
  "novamix",
  "Tomas Duclos",
  "Elaya",
  "Ignacio Palominos",
  "David C.",
  "Gerardo Felipe Conrado",
  "ElXuri",
  "David Borja Martinez",
  "JaviFelices",
  "CarlesSànchez",
  "Gorusuke",
  "DavidFabian",
  "ItziarZG",
  "edy WOLF",
  "MarcosGaPe",
  "Jose Jimenez",
  "Borja ",
  "Jhonathan Izquierdo Higuita",
  "MiLfeR322",
  "Sebastián Espínola",
  "Matias Luna",
  "Imanol Decima",
  "MarcoCasula",
  "MaríaBohórquez",
  "Renan",
  "IvanL'olivier",
  "Shonero",
  "Luichidev",
  "Faviola Narvaez",
  "Christopher Fuentes",
  "Kuro",
  "Juan Pablo Addeo",
  "Sergio Martínez",
  "Fran Enriquez González",
  "Diana",
  "tictools",
  "ConchaAsensio",
  "Emilio_Arreaza",
  "novamix",
  "Tomas Duclos",
  "Elaya",
  "Ignacio Palominos",
  "David C.",
  "Gerardo Felipe Conrado",
  "ElXuri",
  "David Borja Martinez",
  "JaviFelices",
  "CarlesSànchez"
]


#l = ['Gorusuke', None, 'ItziarZG', None, 'MarcosGaPe', None, 'Borja ', None, 'MiLfeR322', None, 'Matias Luna', None, 'MarcoCasula', None, 'Renan', None, 'Shonero', None, 'Faviola Narvaez', None, 'Kuro', None, 'Sergio Martínez', None, 'Diana', None, 'ConchaAsensio', None, 'novamix', None, 'Elaya', None, 'David C.', None, 'ElXuri', None, 'JaviFelices', None, 'Gorusuke', None, 'ItziarZG', None, 'MarcosGaPe', None, 'Borja ', None, 'MiLfeR322', None, 'Matias Luna', None, 'MarcoCasula', None, 'Renan', None, 'Shonero', None, 'Faviola Narvaez', None, 'Kuro', None, 'Sergio Martínez', None, 'Diana', None, 'ConchaAsensio', None, 'novamix', None, 'Elaya', None, 'David C.', None, 'ElXuri', None, 'JaviFelices', None, 'Gorusuke', None, 'ItziarZG', None, 'MarcosGaPe', None, 'Borja ', None, 'MiLfeR322', None, 'Matias Luna', None, 'MarcoCasula', None, 'Renan', None, 'Shonero', None, 'Faviola Narvaez', None, 'Kuro', None, 'Sergio Martínez', None, 'Diana', None, 'ConchaAsensio', None, 'novamix', None, 'Elaya', None, 'David C.', None, 'ElXuri', None, 'JaviFelices', None]

def get_next_index(start):
    for i, a in enumerate(l):
        if i > start and a:
            return i
    
    for i, a in enumerate(l):
        if a:
            return i


def tira():
    n = -1
    for i, a in enumerate(l):
        if i==n:
            print('skip', i, a)
            continue#skip
        if a is None:
            print('skip', i, a)
            continue
        n = get_next_index(i)
        print(i, a, n)
        l[n] = None


def count():
    return len([a for a in l if a])


while count() > 1:
    tira()
    for i, a in enumerate(l):
        print(i, a)


#tira()