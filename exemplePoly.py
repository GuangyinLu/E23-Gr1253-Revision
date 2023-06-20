"""
Une petie révision ::
"""

# Qu'est ce que une classe / Objet ?
# Une classe contient des attributs (data) et des méthodes (comportement / traitement)
# Une classe Est un concept abstrait qui permet de créer des objets concrets
# La classe se trouve dans le fichiers et les objets se trouvent dans la mémoire

# Le constructeur permet de créer des objets

# 4 pliers de l'OO : encapsulation / abstraction / héritage / polymorphisme
# Héritage: c'est créer des classes enfants à partir de classes parents: + ajoute d'attributs/méthodes
# Pour un seytème d'information:

#class ::

class Personne:
    def __init__(self, p_nom, p_prenom, p_age):
        self.nom = p_nom
        self.prenom = p_prenom
        self.age = p_age

    def presenteToi(self):
        print('Je suis ', self.prenom, 'et j ai', self.age)

# Un Etudiant(+ID, Groupe, AnneGraduation) est une Personne(nom,prenom,age)
# Un Employé(+NumEmployee, Service, Bureau) == c'est une Personne
# Un Enseignant(+Département est un Employé

# class Etudiant hérite de Personne::
class Etudiant(Personne):
    # constructeur en utilisant un objet de type Personne(parent)
    def __init__(self, p_personne, p_NumEdutiant, p_Groupe, p_AnneeGraduation):
        super().__init__(p_personne.nom, p_personne.prenom, p_personne.age)
        self.NumEtudiant = p_NumEtudiant
        self.Groupe = p_Groupe
        self.AnneGraduation = p_AnneeGraduation

    def presenteToi(self):
        print('Je suis ', self.prenom, 'et je suis dans le gr:', self.Groupe)

"""
  # constructeur V2 en utilisant un objet de type Personne (parent)
    def __init__(self, p_nom, p_prenom, p_age, p_NumEtudiant, p_Groupe, p_AnneeGraduation):
        super().__init__(p_nom, p_prenom, p_age)
        self.NumEtudiant = p_NumEtudiant
        self.Groupe = p_Groupe
        self.AnneeGraduation =p_AnneeGraduation
"""

class Voiture:
    def __init__(self, v_marque, v_modele, v_couleur):
        self.__marque = v_marque
        self.__modele = v_modele
        self.__couleur = v_couleur
        self.__proprietaire = Personne('Aucun','Aucun',0)

    def attribuer(self, person):
        self.__proprietaire = person

    def affichier(self):
        print('La voiture:', self.__marque, self.__modele, self.__couleur,
              ', est à ', self.__proprietaire.prenom)

# Création des objets: Instantiation

liste = []
liste.append(Personne('babari', 'raouf', 31))
liste.append(Personne('bachir', 'Fikry', 25))
liste.append(Personne('Nabil', 'Agsous', 40))

E1 = Etudiant(liste[1], 1234567, 1253, 2024)
E2 = Etudiant(Personne('Nabil', 'Agsous', 40), 1234567, 1253, 2024)
liste.append(E1)
liste.append(E2)

# constructeur V2 : E3 = Etudiant('Nabil', 'Agsous', 40, 1234567, 1253, 2024)

# Les objets de la même classe se comportemt souvent de la même manière ...

# Les objets de la même classe se comportemt souvent de la même manière ...
for x in liste:
    x.presenteToi()


#Exercice Créer une liste de 4 Voiture
# Trouver un moyen pour informer quelle personne conduit quelle voiture ???

# Création des 4 Voiture
liste_v = []
liste_v.append(Voiture('Subaru','Outback','noir'))
liste_v.append(Voiture('Toyota','Rav4','rouge'))
liste_v.append(Voiture('Nissan','Rougue','jaune'))
liste_v.append(Voiture('Honda','Civic','vert'))

liste_v[0].attribuer(liste[0])
liste_v[1].attribuer(liste[1])
liste_v[2].attribuer(liste[2])
liste_v[3].attribuer(liste[1])

for x in liste_v:
    x.affichier()
