from flask import Flask as _Flask
from flask import jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date
import json


app = _Flask(__name__)
api = Api(app)
ma = Marshmallow(app)

# 配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://xue:123456@localhost:3306/test'

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class JSONEncoder(_JSONEncoder):
    def default(self, o):

        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, o)


class Flask(_Flask):
    json_encoder = JSONEncoder


class Test(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    def keys(self):
        return ['id', 'name']

    def __getitem__(self, item):
        return getattr(self, item)


class HelloWorld(Resource):
    def get(self):
        test_data = Test.query.all()
        data_json = json.loads(json.dumps(test_data, cls=JSONEncoder))
        # c_json = json.loads(data_json)
        return data_json


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)



