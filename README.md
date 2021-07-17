# (TFE) Networking Toolkit : Boite à outil permettant de générer facilement des examens pour Packet Tracer.

* **Coach TFE** : **_Madame Masson_**
* **Etudiant** : **_Morgan Valentin_**

---

### Manuel d'utilisation

* [Archive contenant les 2 manuels en format PDF](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/Manuels.zip)

---

### Release

* Version complète, avec tous les bugs connus corrigés.
	* Version ***3.0*** : [release_windows_v3.0.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v3.0.zip)

> ***Nouveauté*** : Cette version permet désormais de générer un examen de 1ère ou de 2ème. Plus besoin de choisir la version du programme par rapport au besoin.

---

### Vérification de l'intégrité du fichier :

Nom du fichier | hash sha1 associé
---------|----------
 release_windows_v3.0.zip | 68f0bb9bbc590e50e6b19d9e18a55f060288e130

**Comment générer un hash sha1 sous windows ?**

1. Télécharger le fichier sur votre machine.
2. Ouvrir l'explorateur de fichier windows et aller dans le dossier où se situe le fichier téléchargé (généralement "Téléchargement")
3. Maintenir la touche "Maj" ("shift" en anglais) + faire un click droit avec la souris et sélectionner "Ouvrir powershell ici"
4. Taper la commande "***```certutil -hashfile nom_du_fichier```***"
5. Vérifier si le hash correspond à celui mis dans le tableau ci-dessus. 

> ***PS : Si le hash est différent (donc les données ont été altérées = possible virus), ne l'ouvrez surtout pas.***
---

### Bugs connues et anciennes versions

[Liens vers bugs.md](https://github.com/momo007Dev/TFE-Networking_toolkit/blob/main/bugs.md)

---

## Table des matières

- [Description du projet](#description-du-projet)
- [Objectif du projet](#objectif-du-projet)
- [Prochainement](#prochainement)
- [Aspect technique](#aspect-technique)
- [Mocup](#mocup)
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

## Prochainement

* Générateur de commande pour un appareil type (Routeur, Switch-L2/ L3)
* Générateur de configuration de services linux (DNS et DHCP)
  * Permettra de facilement configurer pour le DNS **`Bind9`** et pour le DHCP **` isc-dhcp-server`**.
* Une sorte d'IDE, qui permettra de visualiser les différents fichier générer par le programme afin de pouvoir les personnaliser.
  * Permettra de visualiser en couleur, d'éditer les fichiers, les sauvegardé et si possible, de proposer un système d'auto-complétion.
* Possiblement un jour.... Une sorte de d'analyseur de fichier de config.
  * On place un fichier de config dans le programme, et celui-ci doit être capable de dire, tout les fonctions / protocoles utilisées dans un 1er temps. Et dans un 2ème temps, générer un fichier permettant de facilement encoder dans Packet Tracer (pour les cas d'examens).

---

## Aspect technique


Plateforme | Langage (programmation) | Librairie ?
---------|----------|---------
 **Application de bureau** | **`Python`** | **`PyQt`** => Librairie permettant de mettre en place des GUI plus belle.

> ***Ce programme est disponible et utilisable sous Windows via un exécutable***.

---

## Mocup

<img src="img/mocup.png" width="450" height="370" />

---

## Sources utilisées

* [Générer un hash sha1/md5 sous windows](https://www.lifewire.com/validate-md5-checksum-file-4037391)
* [Documentation des composants graphiques de la librairie "PyQT5"](https://doc.qt.io/qt-5/)
* [Site pour avoir des logos/icônes](https://www.flaticon.com/)
* [QT Designer - Outil pour faire le design de l'application](https://build-system.fman.io/qt-designer-download)
* [Pycharm - IDE Python pour coder](https://www.jetbrains.com/pycharm/)
* [Cheat-sheet pour les calculs de sous-réseau](https://nsrc.org/workshops/2009/summer/presentations/day3/subnetting.pdf)
* [Typora - IDE pour Markdown](https://typora.io/#windows)