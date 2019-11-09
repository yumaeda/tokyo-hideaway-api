import sys

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    version = '{}.{}'.format(sys.version_info.major, sys.version_info.minor)
    return '<h1>Kojinten [Python {}]</h1>'.format(version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

