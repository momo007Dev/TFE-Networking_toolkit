# TFE-Networking_toolkit

* **Coach TFE** : **_Madame Masson_**
* **Etudiant** : **_Morgan Valentin_**

---

### Manuel d'utilisation

* [Version Markdown sur github](https://github.com/momo007Dev/TFE-Networking_toolkit/blob/main/User_manual_v1.md)
* [Version PDF](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/User_manual_v1.pdf)

---

### Release

* Version ***1.0*** : [release_windows_v1.0.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v1.0.zip)
* Version ***1.2*** : [release_windows_v1.2.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v1.2.zip) - Dernière version !
> ***PS : Cette première version peut générer des examens de 1ère et inclus également un simplificateur de calcul de sous-réseau et VLSM. Disponible uniquement pour Windows***

---

### Vérification de l'intégrité du fichier :

Nom du fichier | hash sha1 associé
---------|----------
 release_windows_v1.0.zip | 2f7677315ed1412290d8318b9d17e308f580d369
 release_windows_v1.2.zip | 3b8b4821e52105fd6737129626b17d7b59a05e40

**Comment générer un hash sha1 sous windows ?**

1. Télécharger le fichier sur votre machine.
2. Ouvrir l'explorateur de fichier windows et aller dans le dossier où se situe le fichier téléchargé (généralement "Téléchargement")
3. Maintenir la touche "Maj" ("shift" en anglais) + faire un click droit avec la souris et sélectionner "Ouvrir powershell ici"
4. Taper la commande "***```certutil -hashfile nom_du_fichier```***"
5. Vérifier si le hash correspond à celui mis dans le tableau ci-dessus. 

> ***PS : Si le hash est différent (donc les données ont été altérées = possible virus), ne l'ouvrez surtout pas.***
---

## Table des matières

- [Description du projet](#description-du-projet)
- [Objectif du projet](#objectif-du-projet)
- [Division en modules](#division-en-modules)
  * [Premier module](#premier-module)
  * [Second module](#second-module)
  * [Troisiéme module](#troisième-module)
  * [Fonctionnalités bonus](#fonctionnalités-bonus)
- [Aspect technique](#aspect-technique)
- [Organisation et trello](#organisation-et-trello)
- [Mocup](#mocup)
- [Démo](#démo)
  * [Démo de la partie subneting utilities](#démo-de-la-partie-subneting-utilities)
- [Souces utilisées](#sources-utilisées)
---

## Description du projet

Application (à but éducative) permettant de faciliter la mise en place d'un réseau ou la génération d'examen via une GUI facile à prendre en main.
Cette application sera divisé en 3 modules :
1. Configuration de divers appareils via un générateur de commandes à "_copier-coller_" dans ceux-ci.
2. Générateur d'examen compatible avec (Cisco) **`Packet Tracer`**.
3. Un simplificateur de calculs **`VLSM`** et pour le calcul de sous-réseau.


**_⚠ Ce programme est conçu pour être à des fins éducatives._**

---

## Objectif du projet

L'objectif de ce projet, est de faire gagner du temps aux professeurs dans la mise en place d'un réseau, que ce soit pour la génération d'examen qui peut prendre jusqu'à 1h30 pour certains examens, mais aussi pour simplement générer les commandes pour d'autres topologies réseau qui n'ont pas été crée via ce logiciel.

---

## Division en modules

### Premier module

Le premier module consiste en la mise en place d'un générateur de commandes reprenant divers protocoles réseau et permettant la mise en place de : 
- `Switch Layer 2` (Cisco)
- `Switch Layer 3` (Cisco)
- `Router` (Cisco)
- `Serveur DNS` (bind par exemple)
- `Serveur DHCP` (isc-dhcp-server par exemple)

---

### Second module

Le deuxième module consiste à mettre en place un générateur d'examen (blanc ou pas).
Idéalement, celui-ci génèrera une topologie (schéma réseau), ainsi que toutes les commandes nécessaires permettant de résoudre l'examen généré. Il faudra ensuite l'encoder dans **`Packet Tracer`** si le professeur souhaite utiliser ce programme comme examen pour les étudiants.

L'idée serait de proposé un "template" (une base) comprenant un schéma du réseau avec déjà des liaisons faites (Exemple : Un Pc relié à un switch et un switch relié à un routeur,...).

Ensuite l'utilisateur pourra rajouté les fonctionnalités qu'il désire comme du routage dynamique tel que **`RIP`** (au lieu du routage statique), un système de **`VLAN`**, mise en place de **`NAT`**,...

BONUS : Intégrer une sorte d'aide pour insérer dans Packet Tracer. 
  * Afficher les commandes dans l'ordre des cases à cocher dans Packet Tracer.
  * Afficher dans quel sous-menu mettre la commande.

---

### Troisième module

Ce dernier module est similaire à une calculatrice : il permettra de faciliter les calculs de **`VLSM`** et de calculs de sous-réseau.

Pour les calculs de sous-réseau : 
- Permet de trouver le **`wildcard`** (masque de sous-réseau inversé)
- Permet de savoir le nombre d'adresses **`IP`** utilisable.

---

### Fonctionnalités bonus

> Correspond au bouton "Configuration Editor" dans le mocup en fin de page.

Cette fonctionnalité consiste en une sorte d'IDE pour les configurations faites par le programme. 

Entre autre, permet de :
* **Visualiser les configurations** faites par le programme.
* Visualiser en **couleur** afin d'y voir plus claire.
* Pouvoir **choisir le type de fichier** (Switch Layer 2 / 3, Routeur, fichier de zone DNS, config DHCP,...)

---

## Aspect technique


Plateforme | Langage (programmation) | Librairie ?
---------|----------|---------
 **Application de bureau** | **`Python`** | **`PyQt`** => Librairie permettant de mettre en place des GUI plus belle.

> ***Ce programme disponible et utilisable sous Windows via un exécutable***

---

## Organisation et trello

<img src="img/trello.png" />

* [Lien vers trello](https://trello.com/b/ywBg35gv/tfe)

---

## Mocup

<img src="img/mocup.png" width="450" height="370" />

---

## Démo

### Démo de la partie subneting utilities

![](img/demo_subnet.gif)

---

## Sources utilisées

* [Générer un hash sha1/md5 sous windows](https://www.lifewire.com/validate-md5-checksum-file-4037391)
* [Documentation des composants graphiques de la librairie "PyQT5"](https://doc.qt.io/qt-5/)
* [Site pour avoir des logos/icônes](https://www.flaticon.com/)
* [QT Designer - Outil pour faire le design de l'application](https://build-system.fman.io/qt-designer-download)
* [Pycharm - IDE Python pour coder](https://www.jetbrains.com/pycharm/)
* [Cheat-sheet pour les calculs de sous-réseau](https://nsrc.org/workshops/2009/summer/presentations/day3/subnetting.pdf)