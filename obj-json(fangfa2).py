from flask import Flask as _Flask
from flask import jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date
from itsdangerous import json as _json_
from sqlalchemy import func

app = _Flask(__name__)
api = Api(app)
ma = Marshmallow(app)

# 配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://xue:123456@localhost:3306/ipc'

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
        return _json_.JSONEncoder.default(self, o)


class Flask(_Flask):
    json_encoder = JSONEncoder


class Microwave(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    station_id = db.Column(db.String(20), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    datatype = db.Column(db.String(2), nullable=False)
    temp = db.Column(db.Float)
    rh = db.Column(db.Float)
    pres = db.Column(db.Float)
    tir = db.Column(db.Float)
    rain = db.Column(db.SMALLINT)
    vint = db.Column(db.Float)
    lqint = db.Column(db.Float)
    cloudbase = db.Column(db.Float)
    m0 = db.Column(db.Float)
    m10 = db.Column(db.Float)
    m25 = db.Column(db.Float)
    m50 = db.Column(db.Float)
    m75 = db.Column(db.Float)
    m100 = db.Column(db.Float)
    m130 = db.Column(db.Float)
    m160 = db.Column(db.Float)
    m190 = db.Column(db.Float)
    m220 = db.Column(db.Float)
    m250 = db.Column(db.Float)
    m280 = db.Column(db.Float)
    m310 = db.Column(db.Float)
    m340 = db.Column(db.Float)
    m370 = db.Column(db.Float)
    m400 = db.Column(db.Float)
    m430 = db.Column(db.Float)
    m460 = db.Column(db.Float)
    m490 = db.Column(db.Float)
    m520 = db.Column(db.Float)
    m560 = db.Column(db.Float)
    m600 = db.Column(db.Float)
    m640 = db.Column(db.Float)
    m680 = db.Column(db.Float)
    m720 = db.Column(db.Float)
    m760 = db.Column(db.Float)
    m800 = db.Column(db.Float)
    m840 = db.Column(db.Float)
    m880 = db.Column(db.Float)
    m920 = db.Column(db.Float)
    m960 = db.Column(db.Float)
    m1000 = db.Column(db.Float)
    m1040 = db.Column(db.Float)
    m1080 = db.Column(db.Float)
    m1120 = db.Column(db.Float)
    m1160 = db.Column(db.Float)
    m1200 = db.Column(db.Float)
    m1260 = db.Column(db.Float)
    m1320 = db.Column(db.Float)
    m1380 = db.Column(db.Float)
    m1440 = db.Column(db.Float)
    m1500 = db.Column(db.Float)
    m1560 = db.Column(db.Float)
    m1620 = db.Column(db.Float)
    m1680 = db.Column(db.Float)
    m1740 = db.Column(db.Float)
    m1800 = db.Column(db.Float)
    m1890 = db.Column(db.Float)
    m1980 = db.Column(db.Float)
    m2170 = db.Column(db.Float)
    m2260 = db.Column(db.Float)
    m2350 = db.Column(db.Float)
    m2430 = db.Column(db.Float)
    m2500 = db.Column(db.Float)
    m2600 = db.Column(db.Float)
    m2700 = db.Column(db.Float)
    m2800 = db.Column(db.Float)
    m2900 = db.Column(db.Float)
    m3000 = db.Column(db.Float)
    m3100 = db.Column(db.Float)
    m3200 = db.Column(db.Float)
    m3300 = db.Column(db.Float)
    m3400 = db.Column(db.Float)
    m3500 = db.Column(db.Float)
    m3650 = db.Column(db.Float)
    m3800 = db.Column(db.Float)
    m3950 = db.Column(db.Float)
    m4100 = db.Column(db.Float)
    m4250 = db.Column(db.Float)
    m4400 = db.Column(db.Float)
    m4550 = db.Column(db.Float)
    m4600 = db.Column(db.Float)
    m4800 = db.Column(db.Float)
    m5000 = db.Column(db.Float)
    m5200 = db.Column(db.Float)
    m5400 = db.Column(db.Float)
    m5600 = db.Column(db.Float)
    m5800 = db.Column(db.Float)
    m6000 = db.Column(db.Float)
    m6300 = db.Column(db.Float)
    m6600 = db.Column(db.Float)
    m6900 = db.Column(db.Float)
    m7200 = db.Column(db.Float)
    m7500 = db.Column(db.Float)
    m7800 = db.Column(db.Float)
    m8100 = db.Column(db.Float)
    m8400 = db.Column(db.Float)
    m8700 = db.Column(db.Float)
    m9000 = db.Column(db.Float)
    m9300 = db.Column(db.Float)
    m9600 = db.Column(db.Float)
    m9800 = db.Column(db.Float)
    m10000 = db.Column(db.Float)

    def keys(self):
        return ['datetime', 'temp']

    def __getitem__(self, item):
        return getattr(self, item)


class HelloWorld(Resource):
    def get(self):
        b = Microwave.query.get_or_404(1)
        # return jsonify(microwave_schema(b))
        b_json = _json_.dumps(b, cls=JSONEncoder)
        print(type(b_json))         # str
        c_json = _json_.loads(b_json)
        print(type(c_json))         # dict
        return c_json


class GetTemperature(Resource):

    def __init__(self):
        self.data = []
        self.temp = []
        self.all_data = {}

    def get_data(self):
        one_data = Microwave.query.filter(Microwave.station_id == '54511', Microwave.datatype == '11').all()
        self.data = one_data
        for i in range(0, len(one_data)):
            self.temp.append(one_data[i].temp)

    def get(self):
        self.get_data()
        self.all_data['data'] = self.data
        self.all_data['max_temperature'] = max(self.temp)
        self.all_data['min_temperature'] = min(self.temp)

        d_str = _json_.dumps(self.all_data, cls=JSONEncoder)
        d_dict = _json_.loads(d_str)
        return d_dict


api.add_resource(HelloWorld, '/')

api.add_resource(GetTemperature, '/data')

if __name__ == '__main__':
    app.run(debug=True)



