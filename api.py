from flask import current_app, abort
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import Blueprint
from flask_restful import Api
from resources import profiles


api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

api.add_resource(profiles.ProfileListResource, '/profiles')
api.add_resource(profiles.ProfileResource, '/profiles/<string:id>')
