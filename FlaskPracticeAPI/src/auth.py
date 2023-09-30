from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from FlaskPracticeAPI.src.constants.http_status_codes import (HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                                                              HTTP_201_CREATED)
import validators
from FlaskPracticeAPI.src.database import User, db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post("/register")
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if len(password) < 6:
        return jsonify({
            "error": "password is too short"
        }), HTTP_400_BAD_REQUEST
    if len(username) < 3:
        return jsonify({
            "error": "username is too short"
        }), HTTP_400_BAD_REQUEST
    if not username.isalnum() or " " in username:
        return jsonify({
            "error": "username should be alphabetical and no spaces"
        }), HTTP_400_BAD_REQUEST
    if not validators.email(email):
        return jsonify({
            "error": "Email is not valid"
        }), HTTP_400_BAD_REQUEST

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({
            "error": "username is already taken"
        }), HTTP_409_CONFLICT
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({
            "error": "email is already taken"
        }), HTTP_409_CONFLICT

    pwd_hash = generate_password_hash(password)

    user = User(username=username, email=email, password=pwd_hash)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        "message": "User created",
        "User": {
            "username": username,
            "email": email
        }
    }), HTTP_201_CREATED


@auth.post('/login')
def login():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()

    if user:
        is_pwd_correct = check_password_hash(user.password, password)

        if is_pwd_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            return jsonify({
                "User": {
                    "refresh": refresh,
                    "access": access,
                    "username": user.username,
                    "email": user.email
                }
            }), 200

    return jsonify({
        "error": "Wrong credentials"
    }), 401


@auth.get("/me")
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    return jsonify({
        "data": "Hello world!!!",
        "User": {
            "username": user.username,
            "email": user.email
        }
    })


@auth.post('/token/refresh')
@jwt_required(refresh=True)
def refresh_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({
        "access": access
    })
