# Manuel d'utilisation du programme

* [Procédures d'installation](#procédures-d'installation)
* [Utilisation](#utilisation)
  * [Générateur examens de niveau 1](#Générateur-d'examens-de-niveau-1)
    * **(1) Choisir la topologie**
    * **(2) Main Configuration**
    * **(3) Connectivity**
    * **(4) Addons**
  * [Calculatrice réseau](#calculatrice-réseau)

## Procédures d'installation

1. Aller sur le repos GitHub du projet : [github](https://github.com/momo007Dev/TFE-Networking_toolkit)

2. Téléchargez la dernière version disponible.

3. (**Optionnel**) Vérifier l'intégralité du fichier [Voir section du github](https://github.com/momo007Dev/TFE-Networking_toolkit#v%C3%A9rification-de-lint%C3%A9grit%C3%A9-du-fichier-)

4. Extraire les fichiers :

	* > Vous devriez avoir 1 dossier `"img"` contenant les images du programme et le programme sous format exécutable (`".exe"`).

5. Double cliquer sur l'exécutable pour démarrer le programme.

> PS : Cette exécutable contient toutes les librairies python ainsi que les différents modules utilisées.

<div style="page-break-after: always;"></div>

## Utilisation

<img src="img\maquette.png" />

### Générateur d'examens de niveau 1

#### 1. Choisir la topologie
> PS : Une seule topologie est actuellement disponible.	

<img src="img\img1.png" width="450" height="370" />

<img src="img\img2.png" width="450" height="370" />

* Une fois la topologie sélectionnée, celle-ci se voit encadrée en rouge et un bouton apparaît.
* Cliquez sur le bouton pour continuer.

<div style="page-break-after: always;"></div>

####  2. "(2) Main Configuration"

<img src="img\img3.png" width="620" height="502" />

* **(1) : C'est le schéma du réseau.**

* **(2) : Les données générales du réseau**

  * LAN => C'est le réseau de base qui sera ensuite "coupé" en d'autres sous-réseau (via VLSM)
  * WAN => C'est le réseau entre `R1` et `ISP`
  * DNS Domain => Permettra par la suite de mettre en place un accès distant chiffré (SSH)

* **(3) : Le système de VLSM**

  * Pour chaque sous-réseau, il faut indiquer le nom du sous réseau et le nombre d'hôtes souhaités.

  * Se configure 1 par 1. Il faut donc mettre par exemple "LAN A" et "50" puis ensuite cliquer sur "Add" pour l'ajouter au tableau.

  * > PS : Il n'est pas possible d'avoir 2 réseau avec le même nom !
    >
    > PPS : Si jamais vous avez fait une bêtise, cliquer sur le bouton "`Clear`" qui effacera tout le contenu de la table.

* **(4) : La table VLSM**

  * Cette table à pour but de montrer ce qui est encodé dans le programme.
  * Mais tant que vous n'avez pas cliquer sur "`Save Changes`", vous pouvez toujours revenir en arrière.

<div style="page-break-after: always;"></div>

* **(5) : "Save Changes"**

  * Une fois que vous avez mis toutes les informations désirées, cliquez sur ce bouton pour passer à la suite.
  * Ce bouton va sauvegarder les données et faire apparaître le prochain bouton.

* **(6) : "Home"**

  * Permet de retourner à la page d'accueil du programme.
  * Utilité ?
    
    * Permet d'aller dans la section "`Subnetting Utilities`" pour effectuer un calcul de sous réseau pour ensuite revenir dans l'onglet "`Exam Generator`"
  * >:warning: Attention, si c'est pour relancer le générateur d'examen, il est fortement recommandé de redémarrer le programme.

<div style="page-break-after: always;"></div>

####  3. "(3) Connectivity"

<img src="img\img4.png" width="609" height="499" />

- **(1) : Représente les champs pour mettre le nom d'hôtes des différentes machines (Hostname).**

- **(2) : Menu déroulant permettant d'indiquer dans quel réseau/sous-réseau l'appareil en question se trouve.**

  - Ce menu est constitué des sous-réseau sauvegardé de la page précédente ainsi que le réseau "WAN" (entre ISP et R1)

- **(3) : Menu déroulant comprenant la règle au niveau de l'adressage IP.**

  - "`1st IP Available`" => Indique qu'il faut donner la **1ère adresse IP disponible** à cette appareil (PC1 par exemple).
  - "`2nd IP Available`" => Indique qu'il faut donner la **2ème adresse IP disponible**.
  - "`Last-1 IP Available`" => Indique qu'il faut donner **l'avant-dernière adresse IP disponible**.
  - "`Last IP Available`" => Indique qu'il faut donner la **dernière adresse IP disponible**.

- **(4) : Schéma réseau avec des lettres utilisées pour représenter les interfaces disponibles.**

- **(5) : Menu déroulant avec les interfaces disponibles pour l'appareil en question.**

- **(6) : Permet de préciser quelle interface vous êtes en train de configurer.**

  - > Exemple 1 : R1 : (a) G0/0 => R1 vers S1 (interface a) utilisera l'interface GigabitEthernet0/0 (G0/0)
    >
    > Exemple 2 : R1 : (d) E0/0/0 => R1 vers PC3 (interface d) utilisera l'interface Ethernet0/0/0 (E/0/0/0)
  
<div style="page-break-after: always;"></div>

- **(7) : Description**

  - Permet de mettre une description pour savoir de quoi il s'agit.

- **(8) : "Save Changes"**

  - Une fois que vous avez tout configuré comme vous le souhaitez, appuyer sur ce bouton afin de sauvegarder les données et de passé à la suite.

  - > PS :  :warning: 2 boutons vont s'affichés par la suite : "(4) Addons" et "(5) Generate my exam !".

<div style="page-break-after: always;"></div>

####  4. "(4) Addons"

<img src="img\img5.png" width="607" height="492" />

* **(0) : Il faut bien cliquer sur le bouton "(4) Addons" qui signifie "suppléments".**

  * Contient le nécessaire de sécurité de base, SSH et la possibilité d'ajouter **des** route statique ou par défaut.

* **(1) : Le mot de passe secret.**

* **(2) : Le mot de passe pour accéder à la ligne console et distante.**

* **(3) : Coché si vous voulez chiffrer les mots de passes (fortement conseillé).**

* **(4) : Coché si vous voulez utiliser SSH.**

* **(5) : Champs où il faut y indiquer le nom d'utilisateur et le mot de passe à utiliser lors des connexions via SSH.**

  * > Uniquement visible si la case "`SSH ?`"est cochée.

* **(6) : La bannière affichée lors d'une connexion à l'appareil.**

* **(7) : Le même menu sauf qu'il concerne les switchs.**

  * > :warning: Il n'est malheureusement PAS possible de configurer la sécurité des switchs individuellement.

  * Utilité ?

    * Par exemple autoriser SSH sur R1 mais pas sur les switchs, avoir des mots de passes différents.

<div style="page-break-after: always;"></div>

* **(8) : (Routage Statique) Champ permettant d'y mettre le réseau ainsi que son CIDR dont l'on souhaite accéder.**

* **(9) : Menu déroulant contenant toutes les interfaces de R1 ainsi qu'une option "Other"**

  * L'option "Other", permet de "transformer" le menu déroulant en champ de saisie (permettant ainsi d'y entrer l'adresse IP du "next hop").
  * En cliquant sur "Add" ou "Clear", ce menu se "retransforme" en menu déroulant.

* **(10) : Les boutons "Add" et "Clear" permettant d'ajouter une route dans le tableau, ou bien nettoyer la table.**

* **(11) : Tableau reprenant les informations des routes statiques qui seront encodé par le programme**

* **(12) : Comme d'habitude, appuyer sur ce bouton pour enregistrer les modifications.**

* **(13) : Appuyer sur ce bouton pour générer les 2 fichiers de sorties.**

  * "`solution.txt`" et "`packet-tracer.yaml`"

  * > PS : Ces 2 fichiers seront générer directement sur le bureau.
  
* Pour les routes statiques, lorsque vous sélectionnez l'option "Other", le menu se transforme en champ de saisie. Pas inquiétude, lors d'un clique sur le bouton "Add" ou "Clear", ce menu se "retransforme" en menu déroulant.

<img src="img\img5_1.png" width="400" height="200" />

<div style="page-break-after: always;"></div>

### Calculatrice réseau

<img src="img\img6.png" width="601" height="494" />

* **(1) : En fonction du CIDR, va générer en (2) :**

  * Le masque de sous-réseau
  * Le masque de sous-réseau inversé
  * Le nombre d'adresses IP disponibles (et utilisables)

* **(3) : Mettre le réseau et le CIDR correspondant (va permettre d'effectuer des calculs de VLSM)**

* **(4) : Mettre le nombre d'hôtes souhaité et à chaque fois cliquer sur "Add" pour ajouter un nombre d'hôte dans la table.**

  * > Par exemple, j'ai mis 50 puis "Add", 100 puis "Add" et enfin 3 et "Add" afin d'avoir 50-100-3 dans la table.
    >
    > PS : L'ordre n'a pas d'importance, le programme s'occupe de remettre dans l'ordre les nombres et de mener à bien les calculs de VLSM.

* **(5) : La table des hôtes - permet d'avoir un visuel sur ce que le programme va prendre en compte.**

* **(6) : En appuyant sur ce bouton, cela va démarrer le calcul de VLSM et injecter la solution dans la table (7).**

  * > Fonction caché : En appuyant une 2ème fois sur le bouton, va nettoyer la table.

* **(7) : La table VLSM contenant la solution du calcul de VLSM.**