from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import pickle

app = Flask(__name__)
CORS(app)

RULES_PATH = "/app/shared_volume/rules.pickle"
with open(RULES_PATH, 'rb') as f:
    rules = pickle.load(f)

def get_date():
    return datetime.datetime.now().isoformat()

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json(force=True)
    liked_songs = data['songs']
    recommendationsRules = [list(rule[1]) for rule in rules if set(liked_songs).intersection(rule[0])]
    recommendations = list(set([song for sublist in recommendationsRules for song in sublist]))

    response = {
        "songs": recommendations,
        "version": "1.0",
        "model_date": get_date()
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=52022)