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
            return {'body': obj.body, 'author': obj.author, 'id': obj.id}
        else:
            return super().default(self, obj)
        
app.json = CustomJSONProvider(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


# объединил методы GET и POST, правильней было бы их сделать
# по отдельности, но интересно было попробовать так

@app.route('/twit', methods=['GET', 'POST'])
def twit_functions():
    if request.method == 'GET':
        return jsonify({'twits': twits})
    elif request.method == 'POST':
        twit_json = request.get_json()
        twit = Twit(twit_json['body'], twit_json['author'], twit_json['id'])
        twits.append(twit)
        return jsonify({'status': 'success'})


# изменяем твит по номеру твита в списке (id)
    
@app.route('/twit', methods=['PUT'])
def edit_twit():
    twit_json = request.get_json()
    author = twit_json.get('author')
    body = twit_json.get('body')
    id = twit_json.get("id")
    twits[id] = twit_json
    return jsonify({'author': author, 'body': body, 'id': id, 'edit': 'success'})


# удаляем твит по номеру твита в списке (id)

@app.route('/twit', methods=['DELETE'])
def delete_twit():
    twit_json = request.get_json()
    id = twit_json.get("id")
    del twits[id]
    return jsonify({'delete': 'complete'})


if __name__ == '__main__':
    app.run(debug=True)








# ниже пробы и черновики



# result = next(d['Age'] for d in example['list'] if d.get('Surname') == 'surname5')
# result = example["list"][4]["Age"]


# @app.route('/twit', methods=['POST'])
# def create_twit():
#     '''{"body": "Hello World", "author": "@alex", "id": 1}
#     '''
#     twit_json = request.get_json()
#     twit = Twit(twit_json['body'], twit_json['author'])
#     twits.append(twit)
#     return jsonify({'status': 'success'})

# @app.route('/twit', methods=['GET'])
# def read_twits():
#     return jsonify({'twits': twits})


# @app.route('/users/<int:user_id>', methods=['PUT'])
# def pythongeeks_update_user(user_id):
#    # Retrieve data from the request
#    name = request.form['name']
#    email = request.form['email']
#    # Update user in the database
#    user = User.query.get(user_id)
#    user.name = name
#    user.email = email
#    db.session.commit()
#    # Return success message
#    return 'User updated successfully'

# @app.route("/guide/<id>", methods=["PUT"])
# def guide_update(id):
#     guide = Guide.query.get(id)
#     title = request.json['title']
#     content = request.json['content']

#     guide.title = title
#     guide.content = content

#     db.session.commit()
#     return guide_schema.jsonify(guide)




# , use_reloader=False
