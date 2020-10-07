from Titanic02 import dictTitanic

print("-------------------------------------------")
print("Brisons définitivement la glace !")
print("-------------------------------------------")

# classe Flynn, Mr James

nom = "Flynn, Mr. James"

names = dictTitanic[nom]['Pclass']

print(f"Classe de Mr. Flynn : {names} classe")

########################################################

# proches a bord

print("-------------------------------------------")

nom = "Todoroff, Mr. Lalio"

proches = dictTitanic[nom]['SibSp']

if proches > 0:
    print(f"Mr. Todoroff a {proches} à bord")
else:
    print("Mr. Todoroff voyage seul")

########################################################

# miss a bord?

print("-------------------------------------------")

nom = "Nicola-Yarred, Miss. Jamila"

if nom in dictTitanic:
    print("Oui, Miss Nicola-Yarred était à bord")
else:
    print("Non, Miss Nicola-Yarred n'était pas à bord")

#######################################################

# corriger erreur classe

print("-------------------------------------------")

nom = "Mamee, Mr. Hanna"

dictTitanic[nom]['Pclass'] = 1

classe = dictTitanic[nom]['Pclass']

print(f"Mr. Mamee voyage en {classe}ère classe")




