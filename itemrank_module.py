import numpy as np # Shift+F1 pour ouvrir la doc
import csv
from copy import copy

#Calcule la matrice diagonale contenant les degres des noeuds de la matrice A
def calculate_D(A):
    D = np.zeros(A.shape) #Cree une matrice de meme forme remplie de 0
    #TODO remplir la diagonale avec le degres des noeuds
    for i in range(0,A.shape[0]):
        for j in range(0, A.shape[1]):
            if (A[i,j] != 0):
                D[i,i] = D[i,i] + 1

    return D

#Lecture d'un ficheir CSV (fn en paramètre) du projet et le transforme en np.array
def read_csv_toarray(fn):
    arr = []
    with open(fn) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            for col in row:
                arr.append(int(col))    #N'ajoute jamais qu'une seule ligne (Attention si le fichier CSV est incorrect)

    return arr


#A = np.matrix / alpha = float / v = np.array / m = bool / return np.matrix
def itemRank(A, alpha, v, m):
    print("Verification des variables paramètre")
    if (alpha > 0 or alpha < 1):
        raise ValueError("alpha doit être entre 0 et 1!!")

    if (A.shape[0] != A.shape[1]):
        raise ValueError("La matrice doit être carree!!")

    if m:
        print("Resolution par recurrence")
        #TODO Score par recurrence
        D = calculate_D(A) #Calculer matrice diagonale contenant les degres des noeuds
        P = D.I * A #Matrice de probabilite de transition
        I = np.identity(P.shape[0]) #Matrice d'identite de P
        convergent = (1-alpha) * (I - alpha * P.T).I * v
        x = copy.deepcopy(v)
        while(0): #Tant que non convergence
            x = alpha * P.T * x  + (1-alpha) * v
    else :
        print("resolution par inversion matricielle")
        #TODO Score par inversion matricielle
        x = []

    return x #vecteur des scores d'importance des noeuds


#--------------------TESTING---------------------------------------
a = np.array([[1,2,3],[4,5,6],[8,8,8]], np.int32) #int32 pas necessaire... Juste indicatif
print("Print test array\n",a)
print("Print element at [1,1]",a[1,1])
print("Print element at [1,0]", a[1,0])

b = np.matrix([[1,2,4],[7,8,3],[3,3,2]])
print("Print test Matrix\n",b)
print("Matrix shape=", b.shape)
print("Square matrix? -> row:", b.shape[0],"col:", b.shape[1], "\n Is same?", b.shape[0] == b.shape[1])
c = np.matrix([[1,3,5],[0,1,0],[3,10,1]])
print("Another matrix c:\n", c)
print("matrix a x matrix b:\n",a*b)
c[1,1] = 0
print("C after changing [1,1] to 0\n", c)

print("Calculate D:\n",calculate_D(b))

print("Print Matrix transpose\n",b.T)

print("Print multiplicative inverse of invertible matrix\n", b.I)

print("Matrix identity size 5\n", np.identity(5))

print("Read CSV file 12\n",read_csv_toarray("./Personnalisation_Student12.csv"))