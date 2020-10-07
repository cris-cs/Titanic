from Titanic02 import dictTitanic

nom = 'Flynn, Mr. James'

print(dictTitanic[nom]['Pclass'])

nom2 = 'Todoroff, Mr. Lalio'

if dictTitanic[nom2]['SibSp'] > 0:
    print('he was not alone')
else:
    print('he was alone')

nom3 = 'Nicola-Yarred, Miss. Jamila'

if nom3 in dictTitanic:
    print('She was here')
else:
    print('she was not here')

nom4 = 'Mamee, Mr. Hanna'

dictTitanic[nom4]['Pclass'] = 1

print(dictTitanic[nom4])
