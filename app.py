from flask import Flask, jsonify, request
import json, random, sqlite3 as sql
import joke_db


API = Flask(__name__)

joke_db.create_table()

with open('./joke.json') as f:
    jokes = json.load(f)
    # print(jokes)

for joke in range(len(jokes)):
    id = jokes[joke]['id']
    type = jokes[joke]['type']
    setup = jokes[joke]['setup']
    punchline = jokes[joke]['punchline']
    # print(id, type, setup, punchline)
    joke_db.add_joke(id, type, setup, punchline)

# joke_db.add_joke(jokes['id'], jokes['type'], jokes['setup'], jokes['punchline'])

@API.route('/api/v1/jokes', methods=['GET'])
def get_all_jokes():
    jokes = joke_db.get_all_jokes()
    return jsonify(jokes)
    
    # return jsonify(jokes)

@API.route('/api/v1/jokes/random', methods=['GET'])
def get_random_joke():
    joke = joke_db.get_random_joke()
    return jsonify(joke)
    # return jsonify(random.choice(jokes))

# @API.route('/api/v1/jokes/id', methods=['GET'])
# def get_jokes_by_rating():
#     id = request.args.get('id')
#     joke_id = joke_db.get_joke_by_id(id)
#     if 
#     # for joke in jokes:
#     #     if joke['id'] == int(id):
#     #         return jsonify(joke)
#     # return jsonify({'message': 'No joke found'})
    

@API.route('/api/v1/jokes/newjokes', methods=['POST'])
def add_new_joke():
    new_joke = request.get_json()
    joke_db.add_joke(new_joke['id'], new_joke['type'], new_joke['setup'], new_joke['punchline'])
    all_joke = joke_db.get_all_jokes()
    return jsonify(all_joke)
    # jokes.append(new_joke)
    # return jsonify(new_joke)

@API.route('/api/v1/jokes/delete', methods=['DELETE'])
def delete_joke():
    id = request.args.get('id')
    joke_db.delete_joke(id)
    return jsonify({'message': 'Joke deleted'})
    # for joke in jokes:
    #     if joke['id'] == int(id):
    #         jokes.remove(joke)
    #         return jsonify({'message': 'Joke deleted'})
    # return jsonify({'message': 'No joke found'})

@API.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    return jsonify(message), 404

@API.errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url,
    }
    return jsonify(message), 400

@API.errorhandler(405)
def method_not_allowed(error=None):
    message = {
        'status': 405,
        'message': 'Method Not Allowed: ' + request.url,
    }
    return jsonify(message), 405

@API.errorhandler(500)
def internal_error(error=None):
    message = {
        'status': 500,
        'message': 'Internal Server Error: ' + request.url,
    }
    return jsonify(message), 500

if __name__ == '__main__':
    API.run(debug=True)
