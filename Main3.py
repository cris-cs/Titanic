from Titanic01 import sexe, survided, name

nbPassagers = len(sexe)


def analyseTitanic(totalPassagers):
    nbSurvivants = 0
    for passager in range(nbPassagers):
        if survided[passager] == 1:
            nbSurvivants += 1
    return nbSurvivants


print(analyseTitanic(nbPassagers))
tauxSurvie = analyseTitanic(nbPassagers) / nbPassagers * 100
print(f'{tauxSurvie:.2f}%')
