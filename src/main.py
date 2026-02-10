from src.extract import extract
from src.transform import transform_players, transform_scores
from src.load import load_players, load_scores
from src.database import database_connection
from src.report import generate_report

def main():
    # 1. Extraction [cite: 110-111, 208]
    print("--- Phase d'Extraction ---")
    df_players_raw = extract("data/raw/Players.csv")
    df_scores_raw = extract("data/raw/Scores.csv")

    # 2. Transformation [cite: 112-125, 208]
    print("\n--- Phase de Transformation ---")
    df_players_clean = transform_players(df_players_raw)
    
    # Récupération des IDs valides pour filtrer les scores orphelins [cite: 124, 211]
    valid_ids = df_players_clean['player_id'].tolist()
    df_scores_clean = transform_scores(df_scores_raw, valid_ids)

    # 3. Chargement [cite: 126-127, 208]
    # On charge les joueurs AVANT les scores pour respecter la clé étrangère [cite: 210]
    print("\n--- Phase de Chargement ---")
    with database_connection() as conn:
        load_players(df_players_clean, conn)
        load_scores(df_scores_clean, conn)
        print("Données chargées en base avec succès.")
    
    # 4. Rapport [cite: 137-146, 201]
    print("\n--- Phase de Reporting ---")
    generate_report()

if __name__ == "__main__":
    main()

    