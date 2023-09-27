import json

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, Views = {self.views}, Likes = {self.likes})"


vid_put_args = reqparse.RequestParser()
vid_put_args.add_argument("name", type=str, help="Name of the video")
vid_put_args.add_argument("views", type=int, help="Views of the video")
vid_put_args.add_argument("likes", type=int, help="Likes of the video")

update_args = reqparse.RequestParser()
update_args.add_argument("name", type=str, help="Name of the video")
update_args.add_argument("views", type=int, help="Views of the video")
update_args.add_argument("likes", type=int, help="Likes of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        print(result)
        # result = VideoModel.query.get(id=video_id)
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        # print(request.form)
        # db.create_all()

        args = vid_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        # videos[video_id] = args
        return video, 201
        # return {video_id: args}
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()

        if not result:
            abort(404, message='Video doesnt exists, cannot update')

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.add(result)
        db.session.commit()

        return result

    def delete(self,video_id):

        # del videos[video_id]
        valuee = "Video deleted"
        return valuee, 204



class VideoAll(Resource):
    @marshal_with(resource_fields)
    def get(self):
        print(VideoModel.query.get(1))
        result = VideoModel.query.all()
        print(result)

        return result

api.add_resource(Video, '/video/<int:video_id>')
api.add_resource(VideoAll, '/video/all')

if __name__ == '__main__':
    app.run(host="localhost",port=5001, debug=True)