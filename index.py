 # -*- coding: utf-8 -*-


from flask import Flask, request,jsonify

from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app

api = Api(app)

class Firstpage(Resource):
    def get(self):
        return 'This is my first page'

class Secondpage(Resource):
    def get(self):
        return 'This is my second page'

class Thirdpage(Resource):
    def get(self):
        return 'This is my third page'

api.add_resource(Firstpage, '/firstpage')

api.add_resource(Secondpage, '/Secondpage')

api.add_resource(Thirdpage, '/thirdpage')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"),debug = True) 