import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from code_generator import get_code

CONNECTION_STRING=os.getenv('CONNECTION_STRING')
mongo_client = MongoClient(CONNECTION_STRING)
collection = mongo_client.taskboard.tasks

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def convert_keys_to_camel_case(data):
    if isinstance(data, dict):
        return {to_camel_case(k): convert_keys_to_camel_case(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_keys_to_camel_case(i) for i in data]
    else:
        return data

def db_entry_to_task(db_entry, to_camel=False):
    result = {
        'name': db_entry.get( 'name', None ),
        'id': db_entry.get( 'id', None ),
        'start_date': db_entry.get( 'start_date', None ),
        'end_date': db_entry.get( 'end_date', None ),
        'status': db_entry.get( 'status', None ),
        'subtasks': []
    }

    if to_camel:
        result = convert_keys_to_camel_case(result)

    return result

# Initialize Flask
app = Flask(__name__)
# api = Api(app)

@app.route('/', methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/cstr', methods=['GET'])
def cstr():
    return CONNECTION_STRING

@app.route('/tasks/get', methods=['GET'])
def get_tasks():
    return [db_entry_to_task(x, True) for x in collection.find({})]

@app.route('/tasks/get/<id>', methods=['GET'])
def get_task(id):
    return db_entry_to_task(collection.find({'id': id}), True)

@app.route('/tasks/complete/<id>', methods=['POST'])
def complete_task(id):
    updated_document = collection.find_one_and_update(
        {'id': id}, 
        { '$set': { 'status': 'C' }}, 
        return_document = True
    )
    return db_entry_to_task(updated_document, True)

@app.route('/tasks/add', methods=['POST'])
def add_task():
    data = request.get_json()  # Parse JSON data from request body
    data['id'] = get_code()
    data['status'] = 'N'

    # Insert the task into the database
    result = collection.insert_one(data)

    # Retrieve the inserted document
    inserted_document = collection.find_one({'_id': result.inserted_id})

    # Remove the _id field from the document
    if inserted_document:
        inserted_document.pop('_id', None)

    return jsonify(inserted_document), 201

@app.route('/tasks/reset/all', methods=['POST'])
def reset_all_tasks():
    update_result = collection.update_many({}, { '$set': { 'status': 'N' }})
    return 'OK', 200

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()