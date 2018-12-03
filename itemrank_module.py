import numpy as np # Shift+F1 pour ouvrir la doc

#A = np.matrix / alpha = float / v = np.array / m = bool / return np.matrix
def itemRank(A, alpha, v, m):
    #TODO verifier valeur en param sont corrects
    print("Verification des variables paramètre")

    x = np.array()
    if m:
        print("Resolution par recurrence")
        #TODO Score par recurrence

    else :
        print("resolution par inversion matricielle")
        #TODO Score par inversion matricielle

    return x #vecteur des scores d'importance des noeuds

#--------------------TESTING---------------------------------------
a = np.array([[1,2,3],[4,5,6]], np.int32)
print("Print test array\n",a)
b = np.matrix([[1,2,3],[7,8,9]], np.int32)
print("Print test Matrix\n",b)

print("Print Matrix transpose\n",b.T)

print("Print multiplicative inverse of invertible matrix", b.I)