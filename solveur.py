"""
    DUPIN Léa - Aéro 2 classe F2
    Ma 223 - Tp 1 : Méthode de Gauss pour la résolution de systèmes linéaires.
    Programme de résolution d'un système linéaire avec le solveur python.
    Institut Polytechnique des Sciences Avancées - IPSA Paris
"""

# ---------------- Import des modules nécessaires
import numpy as np
import math
import matplotlib.pyplot as plt
from time import process_time


# ---------------- Calculs de précision
def precision(A, X, B):
    # On récupère la taille de B (nombre de colonnes)
    n = len(B)
    # On la redimensionne
    B = np.reshape(B, (1, n))
    # on récupère les éléments de X et B dans une matrice 1-D
    X = np.ravel(X)
    B = np.ravel(B)
    # On calcule l'erreur
    a = np.dot(A, X) - B
    # On renvoie la norme ||A X - B||
    return(np.linalg.norm(a))


# ---------------- Graphiques
def graph():
    # Mise en page pour mettre les 3 graphiques
    plt.gcf().subplots_adjust(wspace = 0.5, hspace = 0.5)
    plt.subplot(3, 1, 1)

    # Demande de la taille de la matrice maximale à calculer
    taille = int(input("Taille max de la matrice souhaitée ? \n"))

    # ------ Temps de calcul
    print("\n------------Solveur python------------")
    time_list_solveur = []

    for i in range(0, taille + 1):
        A = np.random.rand(i, i)
        B = np.random.rand(i, 1)
        np.linalg.solve(A, B)
        t = process_time()
        time_list_solveur.append(t)

    # Calculs de temps & création de la liste les contenant tous
    T_list_solveur = [] 
    for i in range(len(time_list_solveur)):
        if i == len(time_list_solveur)-1:
            T = time_list_solveur[-1] - time_list_solveur[0]
        elif i == len(time_list_solveur):
            None
        else:
            T = time_list_solveur[i + 1] - time_list_solveur[i]
        T_list_solveur.append(T)

    # Affichage des temps en console
    if taille > 100:
        for i in range(0, len(T_list_solveur) -1, 100):
            print("Le temps de calcul pour une matrice de taille ", i, "est de :", T_list_solveur[i], "secondes.")

    print("Le temps de calcul pour une matrice de taille ", taille, "est de :", T_list_solveur[-2], "secondes.")

    print("\nLe temps de calcul total est de", T_list_solveur[-1], "secondes")
    minutes = int(T_list_solveur[-1]//60)
    secondes = int(T_list_solveur[-1] % 60)
    if minutes == 1:
        print("Soit environ", minutes, "minute et", secondes, "secondes.")
    elif minutes > 1:
        print("Soit environ", minutes, "minutes et", secondes, "secondes.")  

    # On supprime le temps total afin de pouvoir afficher les temps de calcul
    del(T_list_solveur[- 1])

    abscisse = []
    for i in range(0, taille):
        abscisse.append(i)  

    #  -- Création de la courbe
    plt.plot(abscisse, T_list_solveur, color = 'tab:orange', label = 'Solveur python')

    # -- Affichage de la courbe
    # Graphique 1 : Temps / taille
    plt.title("Temps de calcul en fonction de la taille de la matrice")
    plt.ylabel('Temps de calcul en secondes')
    plt.xlabel('Taille de la matrice')
    plt.grid(True)
    plt.legend(loc = 'best')
    # Graphique 2 : Temps en échelle logarithmique / taille
    plt.subplot(3, 1, 2)
    plt.plot(abscisse, T_list_solveur, color = 'tab:orange', label = 'Solveur python')
    plt.title("Temps de calcul en fonction de la taille de la matrice \n Echelle logarithmique ")
    plt.ylabel('Temps de calcul en secondes (log)')
    plt.xlabel('Taille de la matrice')
    plt.yscale('log')
    plt.grid(True)
    plt.legend(loc = 'best')

    # ------ Erreur en fonction de la taille
    plt.subplot(3, 1, 3)
    print("\n------------Solveur python------------")
    size = []
    erreur = []
    for i in range(0, taille + 1):
        A = np.random.rand(i, i)
        B = np.random.rand(i, 1)
        X = np.linalg.solve(A, B)
        result = precision(A, X, B)
        size.append(i)
        erreur.append(result)
    # Graphique 3 : Erreur / taille
    #  -- Création des courbes : LU
    plt.plot(size, erreur, color = 'tab:orange', label = 'Solveur python')
    # -- Affichage des courbes
    plt.xlabel('Taille de la matrice')
    plt.ylabel('Erreur ||A X - B||')
    plt.title('Erreur en fonction de la taille de la matrice')
    plt.grid(True)
    plt.legend(loc = 'best')
    plt.show()

graph()