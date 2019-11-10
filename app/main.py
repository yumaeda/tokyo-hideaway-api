import sys

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    version = '{}.{}'.format(sys.version_info.major, sys.version_info.minor)
    return '<h1>Kojinten [Python {}]</h1>'.format(version)

@app.route('/stores/', methods=['GET'])
def get_stores():
    return jsonify(
        {
            'stores': [
                {
                    'name': '土鍋ごはんと和酒の店 おてだま',
                    'area': '神田',
                    'url': 'https://tabelog.com/tokyo/A1310/A131002/13193128/',
                    'tags': 'sake|rice'
                },

                {
                    'name': 'Wine Bar 葉隠',
                    'area': '池袋',
                    'url': 'https://tabelog.com/tokyo/A1305/A130501/13126401/',
                    'tags': 'wine'
                },

                {
                    'name': '源MOTO',
                    'area': '池袋',
                    'url': 'https://tabelog.com/tokyo/A1305/A130501/13122386/',
                    'tags': 'wine|kushiage'
                },
                {
                    'name': '魚真',
                    'area': '池袋',
                    'url': 'https://tabelog.com/tokyo/A1305/A130501/13039080/',
                    'tags': 'sake|sushi'
                },
                {
                    'name': '稲水器 あまてらす',
                    'area': '池袋',
                    'url': 'https://tabelog.com/tokyo/A1305/A130501/13211375/',
                    'tags': 'sake'
                }
            ]
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

