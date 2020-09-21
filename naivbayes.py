import csv
from math import log,exp
from pprint import pprint
from operator import itemgetter


# import data 
with open('TrainsetTugas1ML.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dataTrain = [dict(row) for row in reader]

with open('TestsetTugas1ML.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dataTest = [dict(row) for row in reader]
   
#memisahkan data berdasarkan income kecil / besar 
incomeBesar =list(filter(lambda x: x['income'] == '>50K',dataTrain))
incomeKecil =list(filter(lambda x: x['income'] == '<=50K',dataTrain))


#buat bantu liat atribut doang
atribut = {attr: set(d[attr] for d in dataTrain) for attr in dataTrain[0] if attr not in {"id", 'income'}}

# frekuensi per atribut
adultBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['age'] == 'adult' ,dataTrain)))
adultKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['age'] == 'adult' ,dataTrain)))
youngBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['age'] == 'young' ,dataTrain)))
youngKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['age'] == 'young' ,dataTrain)))
oldBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['age'] == 'old' ,dataTrain)))
oldKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['age'] == 'old' ,dataTrain)))

someBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['education'] == 'Some-college' ,dataTrain)))
someKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['education'] == 'Some-college' ,dataTrain)))
bachBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['education'] == 'Bachelors' ,dataTrain)))
bachKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['education'] == 'Bachelors' ,dataTrain)))
hsBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['education'] == 'HS-grad' ,dataTrain)))
hsKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['education'] == 'HS-grad' ,dataTrain)))

normBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['hours-per-week'] == 'normal' ,dataTrain)))
normKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['hours-per-week'] == 'normal' ,dataTrain)))
manyBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['hours-per-week'] == 'many' ,dataTrain)))
manyKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['hours-per-week'] == 'many' ,dataTrain)))
lowBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['hours-per-week'] == 'low' ,dataTrain)))
lowKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['hours-per-week'] == 'low' ,dataTrain)))

divBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['marital-status'] == 'Divorced' ,dataTrain)))
divKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['marital-status'] == 'Divorced' ,dataTrain)))
marBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['marital-status'] == 'Married-civ-spouse' ,dataTrain)))
marKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['marital-status'] == 'Married-civ-spouse' ,dataTrain)))
nevBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['marital-status'] == 'Never-married' ,dataTrain)))
nevKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['marital-status'] == 'Never-married' ,dataTrain)))

craftBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['occupation'] == 'Craft-repair' ,dataTrain)))
craftKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['occupation'] == 'Craft-repair' ,dataTrain)))
execBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['occupation'] == 'Exec-managerial' ,dataTrain)))
execKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['occupation'] == 'Exec-managerial' ,dataTrain)))
profBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['occupation'] == 'Prof-specialty' ,dataTrain)))
profKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['occupation'] == 'Prof-specialty' ,dataTrain)))

husBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['relationship'] == 'Husband' ,dataTrain)))
husKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['relationship'] == 'Husband' ,dataTrain)))
notBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['relationship'] == 'Not-in-family' ,dataTrain)))
notKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['relationship'] == 'Not-in-family' ,dataTrain)))
ownBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['relationship'] == 'Own-child' ,dataTrain)))
ownKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['relationship'] == 'Own-child' ,dataTrain)))

locBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['workclass'] == 'Local-gov' ,dataTrain)))
locKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['workclass'] == 'Local-gov' ,dataTrain)))
privBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['workclass'] == 'Private' ,dataTrain)))
privKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['workclass'] == 'Private' ,dataTrain)))
selfBesar = len(list(filter(lambda x: x['income'] == '>50K' and x['workclass'] == 'Self-emp-not-inc' ,dataTrain)))
selfKecil = len(list(filter(lambda x: x['income'] == '<=50K' and x['workclass'] == 'Self-emp-not-inc' ,dataTrain)))

#menghitung jumlah data dengan income kecil & besar
jumBesar = len(incomeBesar)
jumKecil = len(incomeKecil)

#probabilitas income besar & kecil (umum)
probBesar = jumBesar/len(dataTrain)
probKecil = jumKecil/len(dataTrain)


#dictionary untuk menampung probabilitas tiap atribut
ageDict = {'adult': {'>50k':adultBesar/jumBesar,'<=50k':adultKecil/jumKecil},
            'young' : {'>50k':youngBesar/jumBesar,'<=50k':youngKecil/jumKecil},
            'old' : {'>50k':oldBesar/jumBesar,'<=50k':oldKecil/jumKecil}}

eduDict = {'Some-college' : {'>50k':someBesar/jumBesar,'<=50k':someKecil/jumKecil},
            'Bachelors' : {'>50k':bachBesar/jumBesar,'<=50k':bachKecil/jumKecil},
            'HS-grad' : {'>50k':hsBesar/jumBesar,'<=50k':hsKecil/jumKecil}}
hoursDict = {'normal' : {'>50k':normBesar/jumBesar,'<=50k':normKecil/jumKecil},
            'many' : {'>50k':manyBesar/jumBesar,'<=50k':manyKecil/jumKecil},
            'low' : {'>50k':lowBesar/jumBesar,'<=50k':lowKecil/jumKecil}}
maritalDict = {'Divorced' : {'>50k':divBesar/jumBesar,'<=50k':divKecil/jumKecil},
            'Married-civ-spouse' : {'>50k':marBesar/jumBesar,'<=50k':marKecil/jumKecil},
            'Never-married' : {'>50k':nevBesar/jumBesar,'<=50k':nevKecil/jumKecil}}
occupDict = {'Craft-repair' : {'>50k':craftBesar/jumBesar,'<=50k':craftKecil/jumKecil},
            'Exec-managerial' : {'>50k':execBesar/jumBesar,'<=50k':execKecil/jumKecil},
            'Prof-specialty' : {'>50k':profBesar/jumBesar,'<=50k':profKecil/jumKecil}}
relationDict = {'Husband' : {'>50k':husBesar/jumBesar,'<=50k':husKecil/jumKecil},
            'Not-in-family' : {'>50k':notBesar/jumBesar,'<=50k':notKecil/jumKecil},
            'Own-child' : {'>50k':ownBesar/jumBesar,'<=50k':ownKecil/jumKecil}}
workDict = {'Local-gov' : {'>50k':locBesar/jumBesar,'<=50k':locKecil/jumKecil},
            'Private' : {'>50k':privBesar/jumBesar,'<=50k':privKecil/jumKecil},
            'Self-emp-not-inc' : {'>50k':selfBesar/jumBesar,'<=50k':selfKecil/jumKecil}}

    
#menghitung probabilitas total (besar&kecil) untuk menentukan kelas dataTest
for row in dataTest:
    #probtotalKecil = log(ageDict[row['age']]['<=50k']) + log(eduDict[row['education']]['<=50k'])+ log(hoursDict[row['hours-per-week']]['<=50k']) + log(maritalDict[row['marital-status']]['<=50k']) + log(occupDict[row['occupation']]['<=50k']) + log(relationDict[row['relationship']]['<=50k']) + log(workDict[row['workclass']]['<=50k']) + log(probKecil)
    probtotalKecil = ageDict[row['age']]['<=50k'] * eduDict[row['education']]['<=50k']*hoursDict[row['hours-per-week']]['<=50k'] * maritalDict[row['marital-status']]['<=50k'] * occupDict[row['occupation']]['<=50k'] * relationDict[row['relationship']]['<=50k'] * workDict[row['workclass']]['<=50k'] * probKecil
    probtotalBesar = ageDict[row['age']]['>50k'] * eduDict[row['education']]['>50k']*hoursDict[row['hours-per-week']]['>50k'] * maritalDict[row['marital-status']]['>50k'] * occupDict[row['occupation']]['>50k'] * relationDict[row['relationship']]['>50k'] * workDict[row['workclass']]['>50k'] * probBesar
    if probtotalKecil > probtotalBesar :
        row['income'] = '<=50K'
    else :
        row['income'] = '>50K'


with open('tebakantugas1.csv',mode = 'w') as csvfile:
    for x in dataTest:
        csvfile.write(x['income']+'\n')
    