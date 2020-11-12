# TFE-Networking_toolkit

* **Coach TFE** : **_Madame Masson_**
* **Etudiant** : **_Morgan Valentin_**

---

## Table des matières

- [Description du projet](#description-du-projet)
- [Objectif du projet](#objectif-du-projet)
- [Contraintes](#contraintes)
    + [Aspect technique](#aspect-technique)
- [Fonctionnalite](#fonctionnalite)
- [Installation](#installation)

---

## Description du projet

Application (à but éducative) permettant de faciliter la mise en place d'un réseau via une GUI qui va générer les commandes à copier-coller dans des appareils tel que :

* Routeur Cisco (cisco)
* Switch Layer 2 (cisco)
* Switch Layer 3 (cisco)
* Serveur DNS (bind par exemple)
* Serveur DHCP (isc-dhcp-server par exemple)

**_⚠ Ce programme est conçu pour être à des fins éducatives._**

**L'idée est par exemple** : 

1. D'aider les professeurs à corriger les configurations des étudiants lors d'un examen en générant la configuration correcte via ce logiciel.
2. Donner aux étudiants l'application mobile qui elle fournit de la documentation sur les protocoles / services vu aux cours + le calcul de masque de sous-réseau via un CIDR (exemple : /24 = 255.255.255.0)
3. Permet de vite mettre en place un petit réseau avec GNS3 (ou packet tracer) pour tester ou montrer certains concepts réseau.

---

## Objectif du projet

Idéalement le programme :

* Permettra de générer des configurations pour les appareils Cisco (Routeur, Switch Layer 2 / Layer 3).
* Permettra de générer des configurations pour divers services linux nécessaire dans un réseau tel que DNS et DHCP.
* Possèdera des outils fecilitant le calcul de VLSM de sous-réseau
* Possèdera des outils facilitant le calcul de "wildcard" (masque de sours-réseau inversé), masque de sous-réseau, nombres d'adresse IP utilasables,...
* Permettra de visualiser des configs générer pour celui-ci en couleur et également modifié celles-ci. 

---

## Contraintes

Ce projet est divisé en 2 parties :

1. Une partie "**`Desktop`**" où il y aura la plupart des fonctionnalités.
    * Application desktop disponible sur Linux (ubuntu/debian du moins) et windows.
2. Une partie **`Mobile`** où il y aura une partie limité des fonctionnalités.
    * Application mobile disponible sur Android.

L'idée, c'est que l'application desktop soit utilisé pour mettre en place un réseau et que l'application mobile soit là juste pour aider sur quelques détails comme calculé le masque de sous-réseau inversé d'une IP qui a pour CIDR /11 par exemple.

#### Aspect technique


Type | Langage | Détails ?
---------|----------|---------
 **Desktop** | **`Python`** | **`PyQt`** => Librairie permettant de mettre en place des GUI plus belle.
 **Mobile** | **`Java`** + **`Xml`** | Développé pour utilisateurs **`Android`**.

---

## Fonctionnalite

 Features | Windows & Linux | Android
 |---|---|---
 Calculateur de masque de sous-réseau, Masque de sous-réseau inversé et nombre d'IP utilisable | Bientot ! | Bientot !
 Générateur de config pour un Switch Layer 2 (Cisco) | Bientot ! | ❌
 Générateur de config pour un Switch Layer 3 (Cisco) | Bientot ! | ❌
 Générateur de config pour un Routeur (Cisco) | Bientot ! | ❌
 Générateur de config pour un Serveur DNS (Linux) | Bientot ! | ❌
 Générateur de config pour un Serveur DHCP (Linux) | Bientot ! | ❌
 Simplificateur de calcul de VLSM | Bientot ! | Bientot !

> ⚠ L'application android à le **minimum** de functionnalités !

---

## Installation

**=> Prochainement !**