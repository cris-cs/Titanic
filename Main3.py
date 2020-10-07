from Titanic01 import sexe, survided, name

nbPassagers = len(sexe)


def analyseTitanic(totalPassagers, sexePassager):
    nbSurvivants = 0
    nbPassagersCritere = 0
    for passager in range(nbPassagers):
        if survided[passager] == 1:
            nbSurvivants += 1
            if sexe[passager] == sexePassager:
                nbPassagersCritere += 1

    taux = nbPassagersCritere / nbSurvivants * 100
    return taux


#print(analyseTitanic(nbPassagers))
#tauxSurvie = analyseTitanic(nbPassagers) / nbPassagers * 100
#print(f'{tauxSurvie:.1f}%')

print(analyseTitanic(nbPassagers, 'male'))
print(analyseTitanic(nbPassagers, 'female'))