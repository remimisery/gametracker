#!/bin/bash
attempt=0
# On utilise --skip-ssl ici
until mysqladmin ping -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" --skip-ssl --silent; do
    attempt=$((attempt+1))
    if [ $attempt -gt 30 ]; then
        echo "Erreur : Base de données injoignable après 60 secondes."
        exit 1
    fi
    echo "Attente de MySQL... ($attempt/30)"
    sleep 2
done

echo "MySQL est prêt !"

