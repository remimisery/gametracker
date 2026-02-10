# GameTracker - Pipeline ETL Automatisé

## Description
GameTracker est une solution complète de traitement de données pour une startup analysant les performances de joueurs de jeux vidéo. Ce projet implémente un pipeline ETL (Extract, Transform, Load) qui nettoie des données brutes issues de fichiers CSV, les intègre dans une base de données MySQL et génère un rapport de synthèse analytique.



## Prérequis Techniques
* Docker et Docker Compose installés.
* Client Git pour le versionnement.
* Les fichiers de données `Players.csv` et `Scores.csv` placés dans le dossier `data/raw/`.

## Structure du Projet
Le projet est organisé de manière modulaire :
* `data/raw/` : Dossier contenant les données sources brutes.
* `scripts/` : Contient les scripts d'automatisation Bash et l'initialisation SQL.
* `src/` : Code source Python (Logique d'extraction, transformation, chargement et reporting).
* `output/` : Dossier où sont générés les rapports finaux.

## Problèmes de Qualité Traités
Le pipeline détecte et corrige automatiquement les 7 problèmes de qualité suivants :
1. **Doublons** : Suppression des joueurs et scores répétés.
2. **Emails invalides** : Suppression des adresses ne contenant pas le caractère "@".
3. **Dates incohérentes** : Harmonisation des différents formats de date vers un standard SQL.
4. **Espaces parasites** : Nettoyage des espaces en début et fin de pseudonymes.
5. **Scores aberrants** : Suppression des scores négatifs ou nuls.
6. **Valeurs manquantes** : Gestion des champs vides dans les emails ou les scores.
7. **Références orphelines** : Filtrage des scores liés à des joueurs inexistants dans la base.

## Instructions de Lancement
Pour déployer l'infrastructure et exécuter le pipeline complet, utilisez les commandes suivantes :

1. **Lancer l'environnement** :
   ```bash
   docker compose up -d --build