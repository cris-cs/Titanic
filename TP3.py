from Titanic01 import survided, age, sexe, name

nbPassagers = len(name)


def analyseTitanic(totalPassagers,sexePassager):

    nbSurvivants = 0
    nbPassagersCritere = 0

    for i in range(nbPassagers):
        if survided[i] == 1:
            nbSurvivants += 1
        if survided[i] == 1 and sexe[i] == sexePassager:
            nbPassagersCritere += 1

    tauxDeSurvie = (nbPassagersCritere/nbSurvivants)*100

    return tauxDeSurvie

tauxDeSurvie_male = analyseTitanic(nbPassagers,"male")
tauxDeSurvie_female = analyseTitanic(nbPassagers,"female")

print(f"Le taux de survie des hommes est {tauxDeSurvie_male:.2f} %")
print(f"Le taux de survie des femmes est {tauxDeSurvie_female:.2f} %")


