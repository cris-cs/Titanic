from Titanic01 import sexe, survided, name, age

nbPassagers = len(sexe)


def analyseTitanic(totalPassagers, sexePassager):
    nbSurvivants = 0
    nbPassagersCritere = 0
    for passager in range(nbPassagers):
        if survided[passager] == 1:
            nbSurvivants += 1
            if sexe[passager] == sexePassager:
                nbPassagersCritere += 1


def analyseTitanic2(totalPassagers, agemin, agemax):
    nbSurvivants = 0
    nbPassagersCritere = 0
    for passager in range(nbPassagers):
        if survided[passager] == 1:
            nbSurvivants += 1
            if agemax >= age[passager] >= agemin:
                nbPassagersCritere += 1

    taux = nbPassagersCritere / nbSurvivants * 100
    return taux


# print(analyseTitanic(nbPassagers))
# tauxSurvie = analyseTitanic(nbPassagers) / nbPassagers * 100
# print(f'{tauxSurvie:.1f}%')

print(analyseTitanic(nbPassagers, 'male'))
print(analyseTitanic(nbPassagers, 'female'))

print('0-19')
print(analyseTitanic2(nbPassagers, 0, 19))
print('20-39')
print(analyseTitanic2(nbPassagers, 20, 39))
print('40-59')
print(analyseTitanic2(nbPassagers, 40, 59))
print('60->')
print(analyseTitanic2(nbPassagers, 60, 100000))