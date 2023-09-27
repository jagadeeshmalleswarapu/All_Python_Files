from flask import Flask, jsonify

app = Flask(__name__)



@app.get('/')
def home():
    return jsonify({
        'data': 'Welcome to the Home page'
    })

if __name__ == "__main__":
    app.run(debug=True)