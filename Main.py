from Titanic01 import sexe
from Titanic01 import survided
from Titanic01 import age
from Titanic01 import name
import re

sum = 0
passagers = len(sexe)
hombres = sexe.count('male')
mujeres = sexe.count('female')
vive = survided.count(1)
# muere = survided.count(0)
PorcVive = vive/passagers *100

for item in age:
    sum += item

moyen = sum/passagers

print(f'total {passagers}')
print(f'hombres {hombres}')
print(f'mujeres {mujeres}')
print(f'Porcentaje de supervivencia {PorcVive:.1f}%')
print(f'Edad media: {moyen:.1f} años')

nombre = str(input('Nombre a buscar'))
name2 = str(name)

if nombre in name2:
    print('Presente')
else:
    print('no presente')

i = name.index('Panula, Mr. Ernesti Arvid')
name[i] = 'Tanula, Mr. Ernesto Arvad'
print(name[i])
print(name)