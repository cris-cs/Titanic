from Titanic01 import survided, name, sexe, age

print("-------------------------------------------")
print("TOUT LE MONDE A BORD !")
print("-------------------------------------------")

# nombre passagers

nombre_passagers = 0
for element in name:
    nombre_passagers += 1

print(f"Le nombre de passagers : {nombre_passagers} " + "passagers")

#######################################

# nombre de femmes et d'hommes

femmes = 0
hommes = 0
for element in sexe:
    if element == "female":
        femmes += 1
    else:
        hommes += 1

print(f"Le nombre de femmes : {femmes} " + "femmes")
print(f"Le nombre de hommes : {hommes} " + "hommes")

######################################

# pourcentage de survit des passagers

survecus = 0
morts = 0

for element in survided:
    if element == 0:
        morts += 1
    else:
        survecus += 1

pourcentage_survecus = (survecus*100)/(survecus+morts)

print(f"Le pourcentage de survit des passagers : {pourcentage_survecus:.2f} " + "%")

#####################################

#age moyen

age_total = 0

for element in age:
    age_total = age_total + element

age_moyen = age_total/nombre_passagers
print(f"L'age moyen sur le bateau : {age_moyen:.0f} " + "ans")

####################################

print("-------------------------------------------")

#trouver une personne

nom_a_trouver = input("Était présente? : ")

flag = 0

for element in name:
    if nom_a_trouver in element:
        flag = 1

if flag == 1:
    print("Oui")
else:
    print("Non")

########################################

#erreur nom

for element in range(0, len(name)):
    if name[element] == "Panula, Mr. Ernesti Arvid":
        name[element] = "Tanula, Mr. Ernesto Arvad"
print(name)








