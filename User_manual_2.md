# Manuel d'utilisation du programme

* [Procédures d'installation](#procédures-d'installation)
* [Utilisation](#utilisation)
  * [Générateur examens de niveau 2](#Générateur-d'examens-de-niveau-2)
    * **(1) Choisir la topologie**
    * **(2) VLAN**
    * **(3) PCs, Switchs and Servers**
      * **A** : Configuration des Switchs Couche 2 (S1-S2-S3)
      * **B** : Configuration des Clients (Clients - PC)
      * **C** : Configuration des Serveurs (SRV1, SRV2)
    * **(4) Layer 3 Switch**
      * **A** : Configuration des Interfaces
      * **B** : Mise en place du routage
    * **(5) Routers**
      * **A** : Configuration principal de R1
      * **B** : Mise en place de NAT (R2)
      * **C** : Configuration principal de l'ISP
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

<img src="img\maquette2.png" />

### Générateur d'examens de niveau 2

#### 1. Choisir la topologie
> PS : Une seule topologie est actuellement disponible.	

<img src="img\img10.png" width="450" height="370" />

<img src="img\img11.png" width="450" height="370" />

* Une fois la topologie sélectionnée, celle-ci se voit encadré en rouge et un bouton apparaît.
* Cliquer sur le bouton pour continuer.

<div style="page-break-after: always;"></div>

####  2. "(2) VLAN"

<img src="img\img12.png" width="620" height="502" />

* **(1) : C'est le schéma du réseau.**

* > :warning:***Pour les points de 2 à 8, c'est la configuration d'un VLAN. Les VLANs se configurent 1 à la fois.***

* **(2) : Champs permettant d'indiquer le numéro du VLAN et le nom du VLAN**

* **(3) : Le réseau et son CIDR.**

  * > ***Il s'agit bien ici d'un réseau/sous-réseau et non d'une adresse IP.***

* **(4) : L'adresse IP de la passerelle du VLAN.**

* **(5) : L'adresse IP du serveur DHCP.**

  * Si les clients/utilisateurs de ce VLAN obtiennent leur adresse IP de manière automatique via un serveur DHCP, alors mettre ici l'adresse IP du serveur DHCP.
  * Laisser le champ VIDE si ne voulez PAS de serveur DHCP pour ce VLAN.

* **(6) : VLAN Natif.**

  * Permet d'indiquer que le VLAN est natif.

  * > :warning:***Il ne peut y avoir qu'UN SEUL VLAN natif !***
    >
    > (Le bouton disparaît une fois qu'un VLAN natif est ajouté)

* **(7) : "Add".**

  * En cliquant sur ce bouton, celui-ci va ajouter les données du VLAN courant dans la table.
  * Une fois cliqué sur ce bouton, vous pouvez ajouter d'autres VLANs (ou passer à la suite - "Save Changes")

* **(8) : "Clear".**

  * Permet de nettoyer la table (utile si l'on fait des bêtises).

* **(9) : Table récapitulatif.**

  * Cette table permet de visualiser ce qui va être enregistré par le programme.

* **(10) : "Save Changes"**

  * Une fois que vous avez mis toutes les informations désirées, cliquer sur ce bouton pour passer à la suite.
  * Ce bouton va sauvegardé les données et faire apparaître le prochain bouton.

* **(11) : "Home"**

  * Permet de retourner à la page d'accueil du programme.
  * >:warning: ***Attention, si c'est pour relancer le générateur d'examen, il est vivement conseillé de redémarrer le programme.***

<div style="page-break-after: always;"></div>

####  3. "(3) PCs, Switchs and Servers"

##### A : Configuration des Switchs Couche 2 (S1-S2-S3)

<img src="img\img13.png" width="609" height="499" />

> Avant de sauvegardé les configurations des switchs, Pcs et serveurs (donc cliquer sur Save Changes), il faut absolument avoir configuré chaque appareil (donc passé dans chaque "onglet").
>
> Pour l'instant, nous sommes dans l'onglet "**S1**". La logique reste la même pour S2 et S3. ***Des explications suivront pour les onglets "Clients" et "Servers".***

- **(1) : C'est le schéma du réseau.**

- **(2) : Champ permet d'indiquer le nom de l'appareil.**

- **(3) : Permet d'indiquer l'interface qu'on est en train de configuré (relatif au schéma (1)).**

  - > Exemple : S1 : (a) F0/1 => S1 vers PC1 (interface a) utilisera l'interface FastEthernet0/1 (F0/1)
  
- **(4) : Menu déroulant avec les interfaces disponibles pour l'appareil en question.**

- **(5) : Menu déroulant permet de préciser le type d'accès.**

  - Soit "`Access`" et donc un champ avec le numéro de VLAN apparaîtra.
  - Soit "`Trunk`" (généralement pour des appareils tel que Switch Couche 3 ou Routeurs)

- **(6) : Permet de préciser le numéro de VLAN dont on souhaite donner accès.**

  - > PS : Uniquement visible si vous donnez un accès - (5) == "Access"
  

<div style="page-break-after: always;"></div>

- **(7) : Description**

  - Permet de mettre une description pour savoir de quoi il s'agit.


- **(8) : "Is Part of a Vlan ?"**

  - Si le switch fait parti d'un VLAN (par exemple, VLAN 99), permet de choisir le VLAN approprié.

  - Si le switch ne fait PAS parti d'un VLAN, laisser le champ sur "No".

  - > Si le switch fait parti d'un VLAN, vous allez voir un autre champ apparaître demandant l'adresse IP du Switch.

- **Suite ?**

  - Cliquer sur l'onglet "S2" pour configurer **S2** (de la même manière que S1).
  - Cliquer sur l'onglet "S3" pour configurer **S3** (de la même manière que S1).
  - Une fois S1, S2 et S3 configuré, cliquer sur l'onglet "**Clients - PC**".

<div style="page-break-after: always;"></div>

##### B : Configuration des Clients (Clients - PC)

<img src="img\img14.png" width="609" height="499" />

> Avant de sauvegardé les configurations des switchs, Pcs et serveurs (donc cliquer sur Save Changes), il faut absolument avoir configuré chaque appareil (donc passé dans chaque "onglet").
>
> Pour l'instant, nous sommes dans l'onglet "**Clients - PC**". Des explications suivront pour les onglets "Servers".

- **(1) : C'est le schéma du réseau.**
- **(2) : Cette "boite" permet de configurer un client (PC1 dans notre cas).**
- **(3) : DHCP ?**
  - Si vous cochez cette case (3-Bis), alors tous les autres disparaissent.
  - Permet de dire au programme que ce PC sera configuré de manière automatique.
- **(4) et (5) : Adresse IP du PC et CIDR correspondant.**
- **(6) : L'adresse IP de la passerelle.**
- **(7) : L'adresse IP du serveur DNS.**
  - Permet de dire au client (PC) où se trouve le serveur DNS (et donc où renvoyer ces requêtes DNS).
  - Laissez ce champ vide si le PC ne possède pas de serveur DNS.
- **(8) : Permet de configuré le nom de l'appareil.**

- **Suite ?**
  - Une fois les clients (PCs) configurés, cliquer sur l'onglet "**Servers - SRV1**".

<div style="page-break-after: always;"></div>

##### C : Configuration des Serveurs (SRV1, SRV2)

<img src="img\img15.png" width="609" height="499" />

- **(1) : C'est le schéma du réseau.**

- **(2) : Cette "boite" correspond à la configuration général du serveur.**

  - `Hostname `= Nom de l'appareil, `IP `= Adresse IP du serveur, `Gateway `= Adresse IP de la passerelle.

- **(3) : L'adresse IP du serveur DNS.**

  - Permet de dire au serveur où se trouve le serveur DNS (et donc où renvoyer ces requêtes DNS).

  - Laissez ce champ vide si le serveur ne possède pas de serveur DNS.

  - > Dans notre cas, c'est l'adresse IP du serveur vu qu'il est lui-même serveur DNS.

- **(4) : Cette "boite" correspond à la configuration du serveur DNS.**

  - > :warning:Le programme supporte **uniquement** les ressource record de **type A** (Adresse IP) et **CNAME** (Alias).

- **(5) : Nom du ressource record.**

  - Peut être un nom de domaine ou un alias.

  - > Exemple 1 : www.labo.local qui pointera vers une IP (type A)
    >
    > Exemple 2 : www qui pointera vers www.labo.local (type CNAME)

- **(6) : Type du ressource record.**

  - Soit "A" (Adresse IP) ou "CNAME" (alias).


<div style="page-break-after: always;"></div>

- **(7) : La valeur du ressource record.**

  - > Dans l'exemple 1 : "www.labo.local (Nom du RR) A (Type du RR) 192.168.20.11 (Valeur du RR)"
    >
    > Dans l'exemple 2 : "www (Nom du RR) CNAME (Type du RR) www.labo.local (Valeur du RR)"

- **En cliquant sur le bouton "`Add`", vous ajouter un ressource record dans la table. Vous pouvez en ajouter autant que vous voulez. En cliquant sur le bouton "`Clear`", vous nettoyer la table.**

- **(8) : Table contenant les ressources record - c'est un aperçu de ce que le programme prendra en compte.**

- **(9) : Cette "boite" correspond à la configuration du serveur DHCP.**

- **(10) : Nom du "pool" d'adresses DHCP.**

- **(11) : Start IP et CIDR.**

  - `Strat IP` correspond à la première adresse IP disponible pour les clients de ce pool d'adresses IP.

  - > Exemple : Dans mon cas, vu que la passerelle est 192.168.30.1, alors le pool commencera à l'adresse 192.168.30.**2**.

- **(12) : adresse IP de la passerelle pour ce pool.**

- **En cliquant sur le bouton "`Add`", vous ajouter ce pool dans la table. Vous pouvez en ajouter autant que vous voulez. En cliquant sur le bouton "`Clear`", vous nettoyer la table.**

- **(13) : Table contenant les "pool" d'adresse IP - c'est un aperçu de ce que le programme prendra en compte.**

- **Suite ?**

  - Faire de même pour l'onglet suivant "**Servers - SRV2**".

  - Une fois le dernier configuré, vous pouvez (enfin) cliquer sur le bouton "`Save Changes`" pour passer à la suite.

  - > PS : Après avoir appuyer sur "`Save Changes`", un bouton apparaît, cliquer dessus.

<div style="page-break-after: always;"></div>

####  4. "(4) Layer 3 Switch"

##### A : Configuration des Interfaces

<img src="img\img16.png" width="607" height="492" />

> Cette page contient 2 "onglets" : "Interface" et "Routing". Le principe d'onglets reste le même ici, il faut configurer chaque onglets avant de pouvoir cliquer sur le bouton "`Save Changes`".

Etant donné que cette page est très similaire à celle des switchs de couche 2, il y aura moins d'explications.

* **(1) : L'onglet actuel (Interface)**
* **(2) : Le schéma du réseau (focaliser sur SWL3)**
* **(3) : Configuration d'une interface (en l'occurrence, l'interface (b))**
  * Interface, adresse IP, CIDR et description de l'interface.
* **(4) : Une fois terminé, cliquer sur l'onglet "`Routing`" (4).**

<div style="page-break-after: always;"></div>

##### B : Mise en place du routage

<img src="img\img17.png" width="607" height="492" />

> ***Juste à titre informatif, cette capture n'est exact car "OSPF" et "RIP(v2)" sont cochées. En réalité, vous pouvez en coché une ou l'autre. J'ai mis les deux afin de vous expliquer les deux cas de figure avec juste une image.***

* **(1) : L'onglet actuel (Routing)**

* **(2) : Type de routage OSPF - cochez là si vous souhaitez utiliser du routage OSPF au lieu du RIP.**

  * Si vous cochez cette case, alors la "boite" bleu (correspondant à RIP) disparaîtra.

* **(3) Type de routage RIP - cochez là si vous souhaitez utiliser du routage RIP au lieu du OSPF.**

  * Si vous cochez cette case, alors la "boite" verte (correspondant à OSPF) disparaîtra.
  * Pour ajouter un réseau, il suffit de mettre son adresse IP dans le champ "`Network`" et de cliquer sur "`Add`".

* **(4) : L'ID du processus utilisé par OSPF.**

  * > PS : Après avoir ajouter un réseau/sous-réseau, celui-ci ne pourra plus être changé.

* **(5) : La bande-passante de référence - correspond au "`auto-cost reference bandwidth`"**

  * > PS : Après avoir ajouter un réseau/sous-réseau, celle-ci ne pourra plus être changée.


<div style="page-break-after: always;"></div>

* **(6) : L'ajout d'un réseau/sous-réseau.**

  * Vous devez remplir l'adresse IP du réseau/sous-réseau, son CIDR correspondant et préciser dans quelle zone se trouve t-il (area combien ?).
  * N'oubliez pas d'appuyer sur le bouton "`Add`" afin d'ajouter votre réseau/sous-réseau dans la table.

* **(7) : Les interfaces passive - interfaces dont on ne veut pas envoyer des informations concernant le routage.**

  * Il suffit de sélectionner dans le menu déroulant l'interface que l'on souhaite de ne pas envoyer d'informations concernant le routage.

  * Et ensuite d'appuyer sur "`Add`".

  * > En cas d'erreur ou autre, vous pouvez toujours appuyer sur le bouton "`Clear`" qui s'occupera de nettoyer la table (13).

* **(8) : Le routage statique => route par défaut et route statique.**

* **(9) : Le réseau cible ainsi que le masque de sous-réseau du réseau cible.**

* **(10) : Menu déroulant contenant l'interface de sortie de l'appareil et les adresses IP possible du "next-hop".**

* > Comme d'habitude, il faut appuyer sur le bouton "`Add`" pour ajouter une route.

* **(11) : Table contenant les données de routage (OSPF / RIP).**

* **(12) : Table contenant les données concernant les routes statiques ou par défaut.**

* **(13) : Table avec les interfaces passives.**

* **(14) : Une fois terminé, cliquer sur ce bouton afin de passer à la suite.**

* **Appuyer sur le bouton qui vient d'apparaître ("Routers").**

<div style="page-break-after: always;"></div>

#### 5. "(5) Routers"

##### A : Configuration principal de R1

<img src="img\img18.png" width="607" height="492" />

> Cette page contient 6 "onglets". Le principe d'onglets reste le même ici, il faut configurer chaque onglets avant de pouvoir cliquer sur le bouton "`Save Changes`".
>
> Vu que l'onglet "R1 - Main Configuration" et "R2 - Main Configuration" sont identique (sauf que dans un cas c'est R1 et dans l'autre R2), il y aura des explications pour R1 mais PAS pour R2.
>
> Vu que l'onglet "R1 - Routing" et "R2 - Routing" sont identique à celui du switch layer 3 [(voir ici)](#b-:-Mise-en-place-du-routage), alors il n'y aura PAS d'explications.
>
> ***Donc je vais expliquer les onglets "R1 - Main Configuration", "R2 - NAT", et "ISP".***

* **(1) : L'onglet actuel ("R1 - Main Configuration")**
* **(2) : Le schéma du réseau (focalisé sur R1)**
* **(3) : Permet d'activer SSH sur le routeur (R1)**
  * Par défaut, cette case n'est PAS cochée. En la cochant, cela fera apparaître les autres "menus".
* **(4) : Le nom du domaine - correspond à "`ip domain-name ...`"**
* **(5) : Le nom d'utilisateur et le mot de passe utilisé pour se connecter en SSH au routeur.**

<div style="page-break-after: always;"></div>

* **(6) : Permet d'ajouter une règle (ACL SSH) permettant d'autoriser un hôte ou un réseau.**

  * Pour autoriser un hôte (donc une adresse IP), il suffit de mettre le CIDR sur "/32".

  * > En appuyant sur "`Add`", cela va ajouter l'ACL dans la table.
    >
    > PS : :warning:L'ACL aura toujours le numéro **1** (donc 1 seule ACL) mais celle-ci peut contenir plusieurs règles.

* **(8) : Un penses-bête SSH - rappelant ce qui a été dis ci-dessus.**

* **Suite ?**

  * Passer à l'onglet suivant ("R1 - Routing") et complétez de la même manière que pour le routage du switch layer 3.
  * Ensuite passer à l'onglet ("R2 - Main Configuration") et faites la même chose qu'ici.
  * Vous pouvez après cela passer à l'onglet ("R2 - Routing") et complétez de la même manière que pour le routage du switch layer 3 et R1.
  * ***Une fois cela fait, vous pouvez passer à l'onglet ("R2 - NAT") où les explications reprennent.***

<div style="page-break-after: always;"></div>

##### B : Mise en place de NAT (R2)

<img src="img\img19.png" width="607" height="492" />

* **(1) : L'onglet actuel ("R2 - NAT")**

* **(2) : Le schéma du réseau.**

* **(3) : "Boite" qui contient de quoi mettre en place des listes d'accès NAT.**

  * Pour ajouter une règle qui vise une seule adresse IP, il faut mettre un CIDR équivalent à "/32".

  * >En appuyant sur "`Add`", cela va ajouter l'ACL dans la table.
    >
    >PS : :warning:L'ACL aura toujours le numéro **2** (donc 1 seule ACL) mais celle-ci peut contenir plusieurs règles.

* **(4) : "Boite" contenant de quoi faire de la redirection de ports.**

  * J'ai mis en texte au dessus des différents champs ce qu'il faut mettre dedans, afin de faciliter l'encodage dans le programme.

* **(5) : Le protocole du service (/port) à rediriger.**

  * Soit `TCP` ou `UDP`

  * Lorsque vous changer le protocole, vous allez voir que le menu déroulant avec les ports (7) s'adaptera également.

  * > Exemple 1 : Si vous choisissez UDP, alors le menu (7) vous proposera par exemple de rediriger le port 53 (DNS) qui est basé sur UDP.
    >
    > Exemple 2 : Si vous choisissez TCP, alors le menu (7) vous proposera par exemple de rediriger le port 22 (SSH) qui est basé sur TCP.

<div style="page-break-after: always;"></div>

* **(6) : L'Adresse IP interne - correspond à la "vrai" adresse IP du serveur.**
* **(7) : Le service / ports à rediriger.**
  * Le contenu de ce menu déroulant est basé sur le protocole choisis (TCP ou UDP).
  * Celui-ci adaptera en fonction du protocole choisi.
* **(8) : L'adresse IP redirigée - correspond à l'adresse IP accessible depuis l'extérieur**.
  * Généralement, l'adresse IP de l'interface de sortie côté ISP du routeur.
* **(9) : Le port redirigé**
* **En appuyant sur la bouton "`Add`" cela va ajouter la règle de redirection dans la table.**
* **(10) : Table avec les règles d'accès NAT.**
* **(11) : Table avec les règles de redirection NAT.**
* **Suite ?**
  * **Passer au dernier onglet "ISP" (12).**

<div style="page-break-after: always;"></div>

##### C : Configuration principal de l'ISP

<img src="img\img20.png" width="607" height="492" />

La configuration de l'ISP est fortement identique à celles de R1, R2 (onglet interfaces).

* **(1) : L'onglet courant ("ISP")**
* **(2) : Le schéma du réseau (focalisé sur l'ISP)**
* **(3) : Une fois tous les onglets de cette page configurés, appuyer sur ce bouton ("`Save Changes`")**

<img src="img\img21.png" width="607" height="492" />

* Et enfin, cliquez sur le bouton qui vient d'apparaître "`(6) Generate my exam !`"

* Ce bouton va générer les 2 fichiers de sorties suivants :

  * "`solution_v2.txt`" et "`packet-tracer_v2.yaml`"

  * > PS : Ces 2 fichiers seront générer directement sur le bureau.

<div style="page-break-after: always;"></div>

### Calculatrice réseau

<img src="img\img6.png" width="601" height="494" />

* **(1) : En fonction du CIDR, va générer en (2) :**

  * Le masque de sous-réseau
  * Le masque de sous réseau inversé
  * Le nombre d'adresses IP disponibles (et utilisables)

* **(3) : Mettre le réseau et le CIDR correspondant (va permettre des calculs de VLSM)**

* **(4) : Mettre le nombre d'hôtes souhaité et à chaque fois cliquer sur "Add" pour ajouter un nombre d'hôte dans la table.**

  * > Par exemple, j'ai mis 50 puis "Add", 100 puis "Add" et enfin 3 et "Add" afin d'avoir 50-100-3 dans la table.
    >
    > PS : L'ordre n'a pas d'importance, le programme s'occupe de remettre dans l'ordre les nombres et de mener à bien les calculs de VLSM.

* **(5) : La table des hôtes - permet d'avoir un visuel sur ce que le programme va prendre en compte.**

* **(6) : En appuyant sur ce bouton, cela va démarrer le calcul de VLSM et injecter la solution dans la table (7).**

  * > Fonction caché : En appuyant une 2ème fois sur le bouton, va nettoyer la table.

* **(7) : La table VLSM contenant la solution du calcul de VLSM.**