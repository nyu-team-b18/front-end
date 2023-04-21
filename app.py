from flask import Flask, request, session, redirect, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return jsonify({"text":"hello"})


@app.route('/verifyRegistration', methods=["GET", "POST"])
def verifyRegistration():
    data = request.get_json()
    account_type = data['account-type']

    # Check if the account already exists
    # TODO: Add query & verification check
    check = True
    if check:   # Success
        # TODO: Compile relevant information into dictionary
        return jsonify({}), 200
    else:       # Failure
        # TODO: Compile relevant information into dictionary
        return jsonify({}), 409


@app.route('/verifyLogin', methods=["GET", "POST"])
def verifyLogin():
    data = request.get_json()
    
    # Check if the account exists
    # TODO: Add query & verification check
    check = True
    if check:   # Success
        # TODO: Compile relevant information into dictionary
        return jsonify({}), 200
    else:       # Failure
        # TODO: Compile relevant information into dictionary
        return jsonify({}), 409
    
@app.route('/getAssignments', methods=["GET"])
def getAssignments():
    # Get class assignments
    # TODO: Add query for getting assignments

    assignments = ['Assignment 1', 'Assignment 2', 'Assignment 3']

    return jsonify({
        'assignments': assignments,
    })

@app.route('/getStudents', methods=["GET"])
def getStudents():
    # Get class students
    # TODO: Add query for getting students

    students = [f'Student {i}' for i in range(1,11)]

    return jsonify({
        'students': students,
    })

app.secret_key = 'some other random key'


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)