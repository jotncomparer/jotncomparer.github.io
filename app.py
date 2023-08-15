from flask import Flask, render_template, jsonify
import json
import subprocess
import os

app = Flask(__name__, static_folder='static')

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
    return render_template("index.html")

@app.route('/get_exotic_data/<player>', methods=['GET'])
def get_exotic_data(player):
    # Run formatExotic.py with the specified player
    subprocess.run(['python', 'formatExotic.py', player], shell=True)
   
    # Return the formatted data
    data = get_formatted_data(player)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Player data not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
