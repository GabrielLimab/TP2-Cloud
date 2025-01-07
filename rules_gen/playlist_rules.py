import pandas as pd
import os
from fpgrowth_py import fpgrowth
import pickle

dataset_path = os.getenv('DB_PATH')
if not dataset_path:
    raise ValueError("A variável de ambiente DB_PATH não foi definida.")

if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Arquivo do banco de dados não encontrado: {dataset_path}")

playlists = pd.read_csv(dataset_path)

playlists = playlists.groupby('pid')['track_name'].apply(list).tolist()

minSupRatio = 0.05  
minConf = 0.05 
frequent_itemsets_fp, rules_fp = fpgrowth(playlists, minSupRatio=minSupRatio, minConf=minConf)

pickle_path = "/app/shared_volume/rules.pickle"
with open(pickle_path, 'wb') as f:
    pickle.dump(rules_fp, f)

print("New rules generated!")