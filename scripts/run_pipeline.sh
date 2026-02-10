Remove-Item -Recurse -Force .git#!/bin/bash
set -e

echo "1. Attente de la base de données..."
./scripts/wait-for-db.sh

echo "2. Initialisation du schéma SQL..."
mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" --skip-ssl < scripts/init-db.sql

echo "3. Exécution du pipeline ETL Python..."
# On lance le module src.main depuis la racine /app
python -m src.main

echo "Pipeline terminé avec succès !"