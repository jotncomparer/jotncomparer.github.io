from flask import Flask, request, render_template, jsonify, url_for, current_app as app
import json
import subprocess

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET'])
def index():
    # Run the formatExotic.py script
    subprocess.run(['python', 'formatExotic.py'], shell=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)