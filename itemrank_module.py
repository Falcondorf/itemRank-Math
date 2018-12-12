import numpy as np # Shift+F1 pour ouvrir la doc
import csv
from copy import copy

#A = np.matrix / alpha = float / v = np.array / m = bool / return np.matrix
def itemRank(A, alpha, v, m):
    print("Verification des variables paramètre")
    if (alpha > 0 or alpha < 1):
        raise ValueError("alpha doit être entre 0 et 1!!")

    if m:
        print("Resolution par recurrence")
        #TODO Score par recurrence
        P = np.matrix() #Matrice de prrobabilite de transition
        I = np.identity(P[0].size) #Identity matrix with matrix A size
        convergent = (1-alpha) * (I - alpha * P.T)**(-1) * v
        x = copy.deepcopy(v)
        while(1): #Tant que non convergence
            x = alpha * P.T * x  + (1-alpha) * v
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
            for col in row:
                arr.append(int(col))

    return arr


#--------------------TESTING---------------------------------------
a = np.array([[1,2,3],[4,5,6]], np.int32) #int32 pas necessaire... Juste indicatif
print("Print test array\n",a)
print("Print element at [1,1]",a[1,1])
print("Print element at [1,0]", a[1,0])

b = np.matrix([[1,2,3],[7,8,9]])
print("Print test Matrix\n",b)
print("Matrix length=", b[0].size)

print("Print Matrix transpose\n",b.T)

print("Print multiplicative inverse of invertible matrix\n", b.I)

print("Matrix identity size 5\n", np.identity(5))

print("Read CSV file 12\n",read_csv_toarray("./Personnalisation_Student12.csv"))