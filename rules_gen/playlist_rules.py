import pandas as pd
import os
from fpgrowth_py import fpgrowth
import pickle

# Obtém o caminho do banco de dados da variável de ambiente
dataset_path = os.getenv('DB_PATH')
if not dataset_path:
    raise ValueError("A variável de ambiente DB_PATH não foi definida.")

# Carrega o banco de dados
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Arquivo do banco de dados não encontrado: {dataset_path}")
# Load dataset
playlists = pd.read_csv(dataset_path)

# spotifyPlaylists1 = pd.read_csv('../datasets/2023_spotify_ds1.csv')
# # spotifyPlaylists2 = pd.read_csv('2023_spotify_ds2.csv')

# # spotifyPlaylists = pd.concat([spotifyPlaylists1, spotifyPlaylists2])

# Preprocess: Convert playlists into a list of lists
playlists = playlists   .groupby('pid')['track_name'].apply(list).tolist()

# Run FP-Growth
minSupRatio = 0.05  # 5% de suporte mínimo
minConf = 0.05      # 5% de confiança mínima
frequent_itemsets_fp, rules_fp = fpgrowth(playlists, minSupRatio=minSupRatio, minConf=minConf)
print(rules_fp)

# Save rules to a pickle file
pickle_path = "/app/shared_volume/rules.pickle"
with open(pickle_path, 'wb') as f:
    pickle.dump(rules_fp, f)

print("Rules generated and saved successfully!")