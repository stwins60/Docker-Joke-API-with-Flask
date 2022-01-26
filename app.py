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


if __name__ == '__main__':
    API.run(debug=True)
