# itemRank Math description
Implémentation de l'algorithme itemRank avec la librairie numpy pour le cours de Maths discrète de l'UCL 2ème BAC

## Principe
L’ItemRank se base sur le principe de marche aléatoire avec téléportation. Il consiste à démarrer
la marche aléatoire sur un produit choisi au hasard parmi ceux consommés par l’utilisateur,
puis d’entammer une marche aléatoire sur le graphe entre produits. A chaque moment
t , le marcheur a une probabilité \lpha de continuer la marche aléatoire et une probabilité (1-alpha)
d’être retéléporté au hasard sur l’un des produits déjà consommés par l’utilisateur. Les produits
recommandés seront ceux associés aux noeuds qui sont visités le plus souvent par le
marcheur.
Le calcul de xu, le vecteur de score d’importance des produits pour un utilisateur u s’obtient
en partant de P, la matrice de probabilité de transition du graphe des produits, et vu, le vecteur
de personnalisation de l’utilisateur, défini comme [vu]i = 1/n
si l’utilisateur a consommé le produit i et 0 sinon. Le terme n représente le nombre de produits différents achetés par cet
utilisateur.

## Calcul du vecteur de score
Plusieurs méthodes existent afin de calculer le vecteur de score. La méthode qu’il vous est
demandé d’utiliser dans le cadre de ce rapport est le calcul par récurrence. Son principe est
le suivant :

Initialiser: xu(0) = vu

Répéter: xu(t+1) = alpha . P(matrice transposée) . xu(t) + (1-alpha) . vu

jusqu'à convergence du vecteur xu.

## Mission
Ecrivez une méthode calculant les scores par récurrence comme expliqué ci-dessus, puis
utilisez-la pour calculer le score de chaque produit pour l’utilisateur en cours de traitement.
Dans le cadre de ce projet, considérez une forte probabilité de retéléportation vers les produits
consommés (85%).

Le score pour t -> infini peut être obtenu directement en utilisant une inversion matricielle
comme suit :
xu(infini) = (1-alpha).(I-alpha . P(matrice transposée))^-1 . vu
où I est la matrice identité de même dimension que P.

Calculez xu(infini) en Python puis vérifiez empiriquement (en imprimant les deux valeurs à
l’écran et en les comparant) la convergence du vecteur de score vers cette valeur à l’aide de
votre méthode de récurrence.
