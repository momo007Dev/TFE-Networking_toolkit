## Ancienne releases


* **Générateur d'examen de niveau 1 :**
  * Version ***1.8*** :  [release_windows_v1.8.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v1.8.zip)

> ***PS : Ces premières versions peuvent générer des examens de 1ère et incluent également un simplificateur de calcul de sous-réseau et VLSM. Disponible uniquement pour Windows***
>
> **:warning:Les versions commençant par "`1.x`" contiennent uniquement les examens de niveau 1 !**
>
> **:warning:Les versions commençant par "`2.x`" contiendront toutes les fonctionnalités.**

* **Générateur d'examen de niveau 2 :**
  * Version ***2.2*** : [release_windows_v2.2.zip](https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/release/release_windows_v2.2.zip)

---

### Hash des releases

Nom du fichier | hash sha1 associé
---------|----------
 release_windows_v1.8.zip | d2b696c948c644c09b5533e2d39a187fb809b706 
 release_windows_v2.2.zip | f5253e79eb7bcb441f11436620168f8856224c92 

---

## Listes des problèmes connues et corrections

| Version | Où se situe le problème                                      | Description du problème                                      | Solution                                                     |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **1.2** | Page "`(3) Connectivity`"                                    | Les valeurs par défauts des descriptions des interfaces sont toujours les mêmes. | ~~***Sera corrigé dans la prochaine version***.~~ ***Corrigé ! (v1.4)*** |
| **1.2** | Fichier de sortie : "`packet-tracer.yaml`"                   | Au niveau de la route statique, il manque "-0-1" à la fin pour que **Packet Tracer** la prenne en compte. | ~~***Sera corrigé dans la prochaine version***.~~ ***Corrigé ! (v1.4)*** |
| **1.2** | Page "`(4) Addons`"                                          | Après avoir sauvegarder les données de la page 3, le bouton "`(5) Generate my exam !`"est déjà visible. | ~~Il faudra d'abord passer par la page "`(4) Addons`" et sauvegarder avant de pouvoir générer l'examen. ***Sera corrigé dans la prochaine version***.~~ ***Corrigé ! (v1.4)*** |
| **1.4** | Fichier de sortie : "`packet-tracer.yaml`"                   | Manque les descriptions des interfaces des switchs.          | ~~***Sera corrigé prochainement.***~~ ***Corrigé ! (v1.6)*** |
| **1.4** | Page "`About`"                                               | Le numéro de version n'est pas à jour (toujours sur **1.2**). | ~~Un bouton permettant de télécharger directement le manuel d'utilisation sera ajouté également. ***Sera corrigé prochainement.***~~ ***Corrigé ! (v1.6)*** |
| **1.6** | **Nouvelle Fonctionnalité.**                                 | Le client aimerait pouvoir ajouter plusieurs routes statiques (pour l'instant, le programme ne prends qu'une seule route). | ***~~Cette fonctionnalité sera ajouté prochainement.~~ Corrigé ! (v1.8)*** |
| **2.0** | (***Examen de niveau 2***) Page "`(3) Pcs, Switchs and Servers`", onglet Servers. | Il manque un champ "DNS" au niveau des pool DHCP. Dans le pool, il devrait être possible d'indiquer le serveur DNS que les clients prendront en compte. | ~~Il faudra ajouté un champ DNS au niveau des 2 serveurs + ajouter le résultat dans les 2 fichiers de sorties (solution et Packet Tracer). ***Sera corrigé prochainement.~~ ***Corrigé ! (v2.2)*** |
| **2.0** | (***Examen de niveau 2***) Fichier de sortie : "`packet-tracer.yaml`" | Les différentes zones OSPF ne sont pas prises en compte (champs "`Area`") dans le fichier de sortie Packet Tracer. | ***~~Sera corrigé prochainement.~~ Corrigé ! (v2.2)***       |
| **2.0** | (***Examen de niveau 2***) Fichier de sortie : "`packet-tracer.yaml`" | Presque la totalité des descriptions des interfaces ne sont PAS pris en compte dans le fichier de sortie Packet Tracer. | ***~~Sera corrigé prochainement.~~ Corrigé ! (v2.2)***       |
| **2.0** | (***Examen de niveau 2***) Fichier de sortie : "`packet-tracer.yaml`" | Les routes statiques ne respectent pas le format de Packet Tracer. | ***~~Sera corrigé prochainement.~~ Corrigé ! (v2.2)***       |
| **2.2** | (***Examen de niveau 2***) SRV1 et SRV2.                     | Les RR DNS de SRV2 sont pris en compte par SRV1. Ils devraient être uniquement pris en compte par SRV2. Correction également de certaines fautes d'orthographes. | ***~~Sera corrigé prochainement.~~ Corrigé ! (v2.4)***       |

---

## Nouveauté de la dernière version (3.0)

* Correction de plusieurs fautes d'orthographes provoquant des confusions sur les serveurs SRV1 et SRV2.
* Les "Ressource Records" de SRV2 ne se mettent désormais plus dans la table de SRV1.
* Ajout des commandes "`no shut`" (permettant de "réveiller" une interface) au niveau de R1, R2 et de l'ISP.
* Suppression de certains commentaires auto-généré au niveau de OSPF causant certain soucis de copier-coller.
* Mise en place d'une archive zip contenant les 2 manuels d'utilisation au lieu de devoir les télécharger indépendamment.