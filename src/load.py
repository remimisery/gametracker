import numpy as np
import mysql.connector

def load_players(df, conn):
    cursor = conn.cursor()
    # On convertit les NaN/NaT de pandas en None pour MySQL [cite: 129]
    df_clean = df.replace({np.nan: None})
    
    for _, row in df_clean.iterrows():
        # Utilisation de ON DUPLICATE KEY UPDATE pour éviter les erreurs de doublons 
        sql = """
            INSERT INTO players (player_id, username, email, registration_date, country, level)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                username=VALUES(username), 
                email=VALUES(email), 
                level=VALUES(level)
        """
        cursor.execute(sql, tuple(row))
    print(f"Chargement terminé : {len(df_clean)} joueurs traités.")

def load_scores(df, conn):
    cursor = conn.cursor()
    df_clean = df.replace({np.nan: None})
    
    for _, row in df_clean.iterrows():
        sql = """
            INSERT INTO scores (score_id, player_id, game, score, duration_minutes, played_at, platform)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                score=VALUES(score), 
                duration_minutes=VALUES(duration_minutes)
        """
        cursor.execute(sql, tuple(row))
    print(f"Chargement terminé : {len(df_clean)} scores traités.")