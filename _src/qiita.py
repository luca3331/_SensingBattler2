from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/post_article', methods=['POST'])
def post_article():
    # access_token = request.json['access_token']
    access_token = '2d4533a0c58b1662b8e76c586fead2cfb0b3d082'
    title = 'from qiita.py'
    body = 'From python'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'title': title,
        'body': body,
        'private': False,
        'tags': [
            {'name': 'Python'},
            {'name': 'API'},
            {'name': 'ChatGPT'}
        ]
    }
    response = requests.post('https://qiita.com/api/v2/items', headers=headers, json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    # app.run(debug=True)
    post_article()
