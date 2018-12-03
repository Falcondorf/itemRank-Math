import numpy as np # Shift+F1 pour ouvrir la doc
import csv
from copy import copy

#A = np.matrix / alpha = float / v = np.array / m = bool / return np.matrix
def itemRank(A, alpha, v, m):
    #TODO verifier valeur en param sont corrects
    print("Verification des variables paramètre")
    if (alpha > 0 or alpha < 1):
        raise ValueError("alpha doit être entre 0 et 1!!")


    if m:
        print("Resolution par recurrence")
        #TODO Score par recurrence
        cpt = 0
        x = copy(v)
        while(1): #Tant que non convergence
            #Calculer au temps cpt la valeur du vecteur x
            x= []
    else :
        print("resolution par inversion matricielle")
        #TODO Score par inversion matricielle
        x = []

    return x #vecteur des scores d'importance des noeuds

#Read a specific CSV file (fn file name in parameter) from the project and transform into np.array
def read_csv_toarray(fn):
    arr = []
    with open(fn) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            arr.append(row)

    return arr


#--------------------TESTING---------------------------------------
a = np.array([[1,2,3],[4,5,6]], np.int32) #int32 pas necessaire... Juste indicatif
print("Print test array\n",a)
print("Print element at [1,1]",a[1,1])
print("Print element at [1,0]", a[1,0])
b = np.matrix([[1,2,3],[7,8,9]])
print("Print test Matrix\n",b)

print("Print Matrix transpose\n",b.T)

print("Print multiplicative inverse of invertible matrix", b.I)

print(read_csv_toarray("./Personnalisation_Student12.csv"))