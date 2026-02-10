from src.database import database_connection
from datetime import datetime

def generate_report():
    print("Génération du rapport de synthèse...")
    with database_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        
        # 1. Statistiques générales [cite: 142]
        cursor.execute("SELECT COUNT(*) as nb_p FROM players")
        nb_players = cursor.fetchone()['nb_p']
        
        cursor.execute("SELECT COUNT(*) as nb_s, COUNT(DISTINCT game) as nb_g FROM scores")
        score_stats = cursor.fetchone()
        
        # 2. Top 5 des meilleurs scores [cite: 143, 148]
        cursor.execute("""
            SELECT p.username, s.game, s.score 
            FROM scores s 
            JOIN players p ON s.player_id = p.player_id 
            ORDER BY s.score DESC LIMIT 5
        """)
        top_5 = cursor.fetchall()

        # 3. Score moyen par jeu [cite: 144, 148]
        cursor.execute("SELECT game, AVG(score) as avg_s FROM scores GROUP BY game")
        avg_scores = cursor.fetchall()

        # 4. Répartition par pays [cite: 145, 148]
        cursor.execute("SELECT country, COUNT(*) as count FROM players GROUP BY country")
        countries = cursor.fetchall()

        # 5. Sessions par plateforme [cite: 146, 148]
        cursor.execute("SELECT platform, COUNT(*) as count FROM scores GROUP BY platform")
        platforms = cursor.fetchall()

    with open('output/rapport.txt', 'w', encoding='utf-8') as f:
        f.write("=======\nGAMETRACKER\n====\n")
        f.write(f"Rapport de synthese généré le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Nombre de joueurs: {nb_players}\n")
        f.write(f"Nombre de scores: {score_stats['nb_s']}\n")
        f.write(f"Nombre de jeux: {score_stats['nb_g']}\n\n")
        
        f.write("Top 5 des meilleurs scores :\n")
        for i, row in enumerate(top_5, 1):
            f.write(f"{i}. {row['username']} | {row['game']} | {row['score']}\n")
        
        f.write("\nScore moyen par jeu :\n")
        for row in avg_scores:
            f.write(f"{row['game']}: {row['avg_s']:.1f}\n")
            
        f.write("\nJoueurs par pays :\n")
        for row in countries:
            f.write(f"{row['country']}: {row['count']}\n")

        f.write("\nSessions par plateforme :\n")
        for row in platforms:
            f.write(f"{row['platform']}: {row['count']}\n")
    print("Rapport généré dans output/rapport.txt")