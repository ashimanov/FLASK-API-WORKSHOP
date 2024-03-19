from flask import Flask, jsonify, request
from flask.json.provider import DefaultJSONProvider

from model.twit import Twit


twits = []

app = Flask(__name__)

class CustomJSONProvider(DefaultJSONProvider):
    # def __init__(self, app):
    #     super().__init__(app)

    def default(self, obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(self, obj)
        
app.json = CustomJSONProvider(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})

@app.route('/twit', methods=['POST'])
def create_twit():
    '''{"body": "Hello World", "author": "@alex"}
    '''
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})

@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})




if __name__ == '__main__':
    app.run(debug=True)

# , use_reloader=False
