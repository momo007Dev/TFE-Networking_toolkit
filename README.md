# TFE-Networking_toolkit

* **Coach TFE** : **_Madame Masson_**
* **Etudiant** : **_Morgan Valentin_**

---

### Manuel d'utilisation

* **Générateur d'examen de niveau 1** :
  * [Version Markdown sur github](https://github.com/momo007Dev/TFE-Networking_toolkit/blob/main/User_manual_v1_2.md)
  * [Version PDF](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/User_manual_v1_2.pdf)
* **Générateur d'examen de niveau 2 :**
  * [Version Markdown sur github](https://github.com/momo007Dev/TFE-Networking_toolkit/blob/main/User_manual_v2_0.md)
  * [Version PDF](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/User_manual_v2_0.pdf)

---

### Release

* **Générateur d'examen de niveau 1 **:
  * Version ***1.0*** : [release_windows_v1.0.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v1.0.zip)
  * Version ***1.2*** : [release_windows_v1.2.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v1.2.zip)
  * Version ***1.4*** : [release_windows_v1.4.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v1.4.zip)
  * Version ***1.6*** :  [release_windows_v1.6.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v1.6.zip) - ***Dernière version !***
> ***PS : Ces premières versions peuvent générer des examens de 1ère et incluent également un simplificateur de calcul de sous-réseau et VLSM. Disponible uniquement pour Windows***
>
> **:warning:Les versions commençant par "`1.x`" contiennent uniquement les examens de niveau 1 !**
>
> **:warning:Les versions commençant par "`2.x`" contiendront toutes les fonctionnalités.**

* **Générateur d'examen de niveau 2** :
  * Version ***2.0*** : [release_windows_v2.0.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v2.0.zip)

#### Problèmes Connues

| Version | Où se situe le problème                    | Description du problème                                      | Solution                                                     |
| ------- | ------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **1.2** | Page "`(3) Connectivity`"                  | Les valeurs par défauts des descriptions des interfaces sont toujours les mêmes. | ~~***Sera corrigé dans la prochaine version***.~~ ***Corrigé ! (v1.4)*** |
| **1.2** | Fichier de sortie : "`packet-tracer.yaml`" | Au niveau de la route statique, il manque "-0-1" à la fin pour que **Packet Tracer** la prenne en compte. | ~~***Sera corrigé dans la prochaine version***.~~ ***Corrigé ! (v1.4)*** |
| **1.2** | Page "`(4) Addons`"                        | Après avoir sauvegarder les données de la page 3, le bouton "`(5) Generate my exam !`"est déjà visible. | ~~Il faudra d'abord passer par la page "`(4) Addons`" et sauvegarder avant de pouvoir générer l'examen. ***Sera corrigé dans la prochaine version***.~~ ***Corrigé ! (v1.4)*** |
| **1.4** | Fichier de sortie : "`packet-tracer.yaml`" | Manque les descriptions des interfaces des switchs.          | ~~***Sera corrigé prochainement.***~~ ***Corrigé ! (v1.6)*** |
| **1.4** | Page "`About`"                             | Le numéro de version n'est pas à jour (toujours sur **1.2**). | ~~Un bouton permettant de télécharger directement le manuel d'utilisation sera ajouté également. ***Sera corrigé prochainement.***~~ ***Corrigé ! (v1.6)*** |

---

### Vérification de l'intégrité du fichier :

Nom du fichier | hash sha1 associé
---------|----------
 release_windows_v1.0.zip | 2f7677315ed1412290d8318b9d17e308f580d369
 release_windows_v1.2.zip | 3b8b4821e52105fd6737129626b17d7b59a05e40
 release_windows_v1.4.zip | 8c0a6e78f2746a66930f85804e6217500d8fd533 
 release_windows_v1.6.zip | b627149beb60631cb93b5a2aa7dc63bf48a6badd 
 release_windows_v2.0.zip | 0774c2af9874d10ab4dbe8aeca835166786aaf35 

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
- [Feedback Clients](#feedback-clients)
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
* [Typora - IDE pour Markdown](https://typora.io/#windows)

---

## Feedback clients

#### Examen de niveau 1

* **Testé par : Madame Masson.**

> J'ai testé. Voici ce que j'en pense:
>
> - très facile et intuitif
> - mode d'emploi très bien fait et très utile (attention à l'orthographe)
> - MAIS... J'ai pu entrer de grosses bêtises . Il n'y a pas de vérification du nombre d'hôtes en fonction du /xx demandé
>
> Est-ce prévu? Faisable? Inutile car on s'adresse à des profs?

#### Examen de niveau 2

TODO