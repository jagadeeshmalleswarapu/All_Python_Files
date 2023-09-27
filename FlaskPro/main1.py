from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

names = {
    "Jagadeesh": {
        "name": "Jagadeesh",
        "Age": 24,
        "Gender": "male"
    },
    "Venkat": {
        "name": "Venkat Kumar",
        "Age": 26,
        "Gender": "male"
    }
}
class HelloWorld(Resource):
    def get(self,name):
        return names[name]
    # def post(self):
    #     return {"name":"Jagadeesh"}

api.add_resource(HelloWorld,'/helloWorld/<string:name>')
# api.add_resource(HelloWorld,'/helloWorld/<string:name>/<int:test>')

if __name__=='__main__':
    app.run(debug=True)
