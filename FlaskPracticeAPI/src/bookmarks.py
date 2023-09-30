from flask import Blueprint, jsonify, request
import string
import random
from FlaskPracticeAPI.src.database import db, Bookmark
import validators
from flask_jwt_extended import jwt_required, get_jwt_identity

bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")


def generate_short_url():
    character = string.digits + string.ascii_letters
    picked_chars = ''.join(random.choices(character, k=3))

    link = Bookmark.query.filter_by(short_url=picked_chars).first()

    if link:
        generate_short_url()
    else:
        return picked_chars


@bookmarks.route('/', methods=['GET', 'POST'])
@jwt_required()
def bookmark_route():
    user_id = get_jwt_identity()
    if request.method == 'POST':

        body = request.json['body']
        url = request.json['url']

        if not validators.url(url):
            return jsonify({
                "error": "Please enter valid url"
            }), 400
        if Bookmark.query.filter_by(url=url).first():
            return jsonify({
                "error": "You have entered existing url, Please enter new url"
            }), 409

        srt_url = generate_short_url()
        bookmark = Bookmark(body=body, url=url, user_id=user_id, short_url=srt_url)

        db.session.add(bookmark)
        db.session.commit()

        return jsonify({
            "data": {
                "id": bookmark.id,
                "body": bookmark.body,
                "url": bookmark.url,
                "short_url": bookmark.short_url,
                "Visits": bookmark.visits,
                "created_at": bookmark.created_at,
                "updated_at": bookmark.updated_at
            }
        }), 201

    else:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)
        bookmark_data = Bookmark.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page)

        data = []

        for bookmark in bookmark_data:
            data.append({
                "id": bookmark.id,
                "body": bookmark.body,
                "url": bookmark.url,
                "short_url": bookmark.short_url,
                "Visits": bookmark.visits,
                "created_at": bookmark.created_at,
                "updated_at": bookmark.updated_at,
            })
        meta = {
            "page": bookmark_data.page,
            "pages": bookmark_data.pages,
            "total": bookmark_data.total,
            "prev_page": bookmark_data.prev_num,
            "next_page": bookmark_data.next_num,
            "has_prev": bookmark_data.has_prev,
            "has_next": bookmark_data.has_next
        }

        return jsonify({
            "data": data,
            "meta": meta
        }), 200
