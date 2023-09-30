from flask import Flask, jsonify
from FlaskPracticeAPI.src.auth import auth
from FlaskPracticeAPI.src.bookmarks import bookmarks
from FlaskPracticeAPI.src.database import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'
app.config["JWT_SECRET_KEY"] = "JWT_SECRET_KEY"


@app.get('/cre_db')
def cre_db():
    db.create_all()
    return "db created"


@app.get('/')
def home():
    return jsonify({
        'data': 'Welcome to the Home page'
    })


db.app = app
db.init_app(app)
JWTManager(app)
app.register_blueprint(auth)
app.register_blueprint(bookmarks)

if __name__ == "__main__":
    app.run(debug=True)
