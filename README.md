# applicationPygame
application pygame groupe Roxane, Danick, Xavier


Pour ce dernier projet vous devrez créé un petit jeu vidéos: FastClick

Dans FastClick il vous est demandé de cliquer rapidement sur un rectangle bleu ou sur un rectangle rouge.

Suivant votre performance, un score est calcule et vous pourrez faire un Highscore !

Il y aura 4 écrans :

Sur le 1er écran nous aurons un menu
Le menu comprends les boutons :

Nouvelle Partie
Highscore
Quitter
Le click sur Nouvelle Partie commence une nouvelle partie.
Le click sur Highscore affiche les Highscore
Le click sur Quitter ferme le programme.


Exemple de menu

Sur l'écran Highscore seront afficher les plus grands scores
Les 10 meilleurs scores sont affichés.
Les scores sont stockés dans un fichier : au redémarrage du jeu, les anciens highscores peuvent être affichés
Si l'on appuie sur la touche Escape, nous revenons au menu principal (ecran1).


Exemple d'écran d'Highscore.

L'écran de jeu
L'écran de jeu est affiche lorsque que l'on clique sur nouvelle partie.

Une partie dure 20 secondes.

L'écran de jeu affiche 2 rectangles un rouge et un bleu et une balle rebondissante.
L'écran de jeu se rafraichit a hauteur de 60 images par seconde.
L'écran de jeu fait 800*600 pixels
Les rectangles bleu et rouge sont places aléatoirement dans l'écran.
Les rectangles bleu et rouges font 20*20pixels.
La balle rebondissante de déplace de 2 pixels par cycle.
La balle rebondissante fait 40*40 pixels.
Le score de la session en cours est place en haut a droite de l'écran.
Au click gauche sur un rectangle bleu :

Le score est augmente de 10
Le rectangle n'est plus affiché
Un nouveau rectangle bleu est place aléatoirement a l'écran
Au click droit sur un rectangle bleu :

Le score est réduit de 5
Le rectangle n'est plus affiché
Un nouveau rectangle bleu est place aléatoirement a l'écran
Au click gauche sur un rectangle rouge:

Le score est réduit de 5
Le rectangle n'est plus affiché
Un nouveau rectangle rouge est place aléatoirement a l'écran
Au click droit sur un rectangle rouge:

Le score est augmente de 10
Le rectangle n'est plus affiché
Un nouveau rectangle rouge est place aléatoirement a l'écran
Au click (gauche ou droit) sur la balle rebondissante:

Le score est réduit de 10.
La balle rebondissante continue de se déplacer.
Nous avons donc a tout moment un rectangle bleu, un rectangle rouge et une balle rebondissante affiche sur l'écran.

  

  

Fin de partie

Si a la fin d'une partie le score du joueur lui permet d'entrer dans les Highscore alors l'utilisateur est invite a saisir son nom.

Sinon, l'utilisateur est redirige vers l'écran principal, le score de sa dernière session est affiche en haut a droite.

   

   

Écran de saisie de Highscore
Dans cet écran l'utilisateur sera invite a saisir son nom. 

Une fois le texte saisi et la touche entrée appuyée l'utilisateur sera redirige vers l'écran Highscore ou son nom+ score serons affiches.

 

 Exemples de captures de jeu :






 

Barème
Menu principal : 1pt
Écran de jeu : 5pts :
Placement des rectangles 1pt
Click sur rectangle et placement aléatoire 1pt
Affichage de la balle rebondissante au dessus des rectangles. 1pt
Calcul du score : 2pts
Saisie de Highscore : 1pt
Affichage de l'écran Highscore : 2pts (avec persistance dans un fichier).
Mise en place de style pour l'application 1pt, par exemple : 
Couleurs de menu (couleurs choisies)
'Effets' graphiques
Bordure du menu
Détection de mouse-hover et changement de style