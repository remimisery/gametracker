import pandas as pd
import os

def extract(filepath):
    if not os.path.exists(filepath):
        print(f"Erreur : Le fichier {filepath} est introuvable.")
        return None
    df = pd.read_csv(filepath)
    print(f"Extraction réussie : {len(df)} lignes lues depuis {filepath}")
    return df
