import sys
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from models.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config().db_connection_string
db = SQLAlchemy(app)

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id   = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    url  = db.Column(db.String(512), nullable=False)
    tags = db.Column(db.Text, default='', nullable=False)

    def __init__(self, name, url, tags):
        """
        Constructor
        """
        self.name = name
        self.url  = url
        self.tags = tags

    @property
    def serialize(self):
        """
        Return object data in serializeable format.
        """
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'tags': self.tags
        }

    def __repr__(self):
        return '<Restaurant %r>' % self.name

@app.route('/')
def index():
    version  = '{}.{}'.format(sys.version_info.major, sys.version_info.minor)
    return '<h1>Kojinten [Python {}]</h1>'.format(version)

@app.route('/restaurants/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify({
        'data': [ restaurant.serialize for restaurant in restaurants ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
