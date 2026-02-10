import pandas as pd
import numpy as np

def transform_players(df):
    # 1. Doublons [cite: 114]
    df = df.drop_duplicates(subset=['player_id'])
    # 2. Espaces parasites [cite: 115]
    df['username'] = df['username'].str.strip()
    # 3. Dates incohérentes [cite: 116]
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')
    # 4. Emails invalides [cite: 117]
    df.loc[~df['email'].str.contains('@', na=False), 'email'] = None
    return df

def transform_scores(df, valid_player_ids):
    # 1. Doublons [cite: 119]
    df = df.drop_duplicates(subset=['score_id'])
    # 2. Conversion types [cite: 120]
    df['played_at'] = pd.to_datetime(df['played_at'], errors='coerce')
    # 3. Scores négatifs ou nuls [cite: 121]
    df = df[df['score'] > 0]
    # 4. Références orphelines [cite: 122]
    # On ne garde que les scores dont le joueur existe dans la table Players nettoyée
    df = df[df['player_id'].isin(valid_player_ids)]
    return df
