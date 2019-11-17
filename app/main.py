import boto3
import base64
import json
import sys

from flask import Flask, jsonify
app = Flask(__name__)

# CONSTANTS
SECRET_NAME = "RDSSecret3683CA93-LpqX2CRjubS6"
REGION_NAME = "ap-northeast-1"

@app.route('/')
def index():
    version  = '{}.{}'.format(sys.version_info.major, sys.version_info.minor)
    html     = '<h1>Kojinten [Python {}]</h1>'.format(version)
    """
    session    = boto3.session.Session()
    secret_mgr = session.client(
        service_name='secretsmanager',
        region_name=REGION_NAME
    )

    try:
        response = secret_mgr.get_secret_value(SecretId=SECRET_NAME)
        if 'SecretString' in response:
            secret  = json.loads(response['SecretString'])
            html    += (
                '<ul>'
                '<li>DB Host: {}</li>'.format(secret['host'])
                '<li>DB User: {}</li>'.format(secret['username']))
                '<li>DB Pwd: {}</li>'.format(secret['password']))
                '<li>DB Port: {}</li>'.format(secret['port'])
                '</ul>'
            )
        else:
            html += base64.b64decode(response['SecretBinary'])
    except:
        return '<h1>Could not retrieve RDS credentials.</h1>'
    """

    return html

@app.route('/stores/', methods=['GET'])
def get_stores():
    return jsonify(
        {
            'stores': []
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

