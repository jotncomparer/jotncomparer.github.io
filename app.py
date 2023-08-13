from flask import Flask, request, render_template, jsonify, url_for, current_app as app

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)