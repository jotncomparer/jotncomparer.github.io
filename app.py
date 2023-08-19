from flask import Flask, render_template, jsonify
import json
import subprocess
import os

app = Flask(__name__, static_folder='static')

def update_all_players_data():
    players = ["Cameron", "Connor", "Douglas", "Hunter", "Jack", "Kade", "Mark", "Thomas"]
    
    for player in players:
        subprocess.run(['python3', 'formatExotic.py', player], shell=True)

def get_formatted_data(player):
    json_path = f'static/data/formattedPlayerExoticData/formatted{player.capitalize()}Exotics.json'
    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    else:
        return None

@app.route('/', methods=['GET'])
def index():
    update_all_players_data()
    return render_template("index.html")

@app.route('/get_exotic_data/<player>', methods=['GET'])
def get_exotic_data(player):
    data = get_formatted_data(player)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Player data not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
