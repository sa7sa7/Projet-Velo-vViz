
# Review from [ChordViz](https://github.com/jmarwane/ChordViz/blob/master/README.md)
Le projet ChordViz Permet la Visualisation de l'enchaînement d'accords d'un certain nombre de chansons:
sélection par artiste, chanson...
Possibilité de retrouver une chanson en sélectionnant une progression harmonique.

## Est-ce que le problème est clairement décrit ?

La derniére image chordProgression.png  nous donne une bonne vision sur le résultat attendu par ce projet.

Le projet paraît pertinent.

Point d'amélioration pour le fichier *Data.md* : à compléter : il faut décrire la base de données dedans. ainsi que la source des
données !


## Est-ce que les choix de visualisation sont adaptés ?

L'equipe a parti depuis la visualisation à partir d'un graphe ce qui parait complexe à une visualisation bien adapté à ce type de 
probléme.
Le scénario abordé par l'équipe et l'idée de design est intéressante.

La présence de plusieurs filtres permet de bien raffiner la visualisation.(minimiser les lignes)

Cependant on ne comprend pas bien, en regardant les fiches, l'interactivité de l'utilisateur avec le graphique :
* Le choix d'artist 
* Le choix de genre 

## Est-ce que le projet est réalisable ?

* Ce projet semble tout à fait réalisable et la méthode pour récupérer les données est claire.
* pensez au temps de traitement (si on a plusieurs courbes à dessiner .. ) 
* Pensez à l'encombrement aussi

## Remarques

</table>
Commentaires sur  les fonctionnalités:

- Déterminer une durée des transitions pour l'apparition / dispartition des lignes.
y'a t-il une entrée pour le paramétré ? si oui elle est ou dans la feuille de design !

- Déterminer le nombre de chansons dans la base de données.
je comprends pas pourquoui le nombre de chonson est un paramétre

- Déterminer la plus petite opacité que peut avoir une ligne et La largeur des lignes. (claire)

- Renvoier le string correspondant à l'accord n°bar du morceau n°song. (claire)

- Nombre maximal de mesures (si il est plus grand que le nombre de mesures de la plus grande chanson, c'est du gâchis parce que ça mettra des mesures vides à la fin, si il est plus petit les derniers accords ne seront pas affichés). (claire)

- Déterminer la largeur d'un des rectangles contenant un nom d'accord, les distances horizontale, la verticale entre deux rectangles contenant un accord et la Largeur et la hauteur du svg. (claire)

- Déterminer une liste qui contient les entiers de 1 à MAX_BAR_ID, et une autre liste contenant les noms des accords les plus communs, "?" correspond aux autres accords. (claire)

- Déterminer les dimensions de la zone d'affichage sur le svg, la hauteur d'un des rectangles contenant un accord, et la taille de la police de caractères. (claire)

- La gestion du scrolling.(ça veut dire quoi? à clarifier ...)

- Déterminer des groupes d'éléments, bars[i] contient les rectangles contenant les noms des accords de la mesure i. Ainsi que les éléments sur lesquels on ne peut pas cliquer. (claire)

- Définition d'unn objet d3 permettant de générer les courbes. (claire)

- La création des groupes d'éléments dans lesquels on va stocker les courbes de chaque chanson. (claire)

- Parcourir les chansons et créer pour chaque chanson l'ensemble de ses courbes. (claire)

- Implémentation d'une fonction qui gère la mise à jour des courbes quand on sélectionne / déselectionne un accord. (claire)
</table>
<h3>le projet demande plus de clarification (simplifier les idées au début pour faire comprendre le lecteur)</h3>
