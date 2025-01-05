from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

RULES_PATH = "/app/shared_volume/rules.pickle"
with open(RULES_PATH, 'rb') as f:
    rules = pickle.load(f)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    print("DEBUG: Request received")
    data = request.get_json(force=True)
    print("DEBUG: Request data: ", data)
    liked_songs = data['songs']
    recommendationsRules = [list(rule[1]) for rule in rules if set(liked_songs).intersection(rule[0])]
    recommendations = list(set([song for sublist in recommendationsRules for song in sublist]))

    response = {
        "songs": recommendations,
        "version": "1.0",
        "model_date": "2025-01-05"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=52022)