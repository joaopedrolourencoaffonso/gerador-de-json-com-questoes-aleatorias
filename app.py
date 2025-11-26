from flask import Flask, render_template, jsonify
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
