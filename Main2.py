from Titanic02 import dictTitanic

nom = 'Flynn, Mr. James'

print(dictTitanic[nom]['Pclass'])

nom2 = 'Todoroff, Mr. Lalio'
if dictTitanic[nom2]['SibSp'] > 0:
    print('he was not alone')
else:
    print('he was alone')
