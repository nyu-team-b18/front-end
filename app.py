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
    check = False
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

@app.route('/getAccountType', methods=["GET"])
def getAccountType():
    # Get account type
    # TODO: Check session for account type

    account_type = 'ADMIN'

    return jsonify({'account-type':account_type})

@app.route('/getAssignmentDetails', methods=["GET"])
def getAssignmentDetails():
    # GET args
    assignment_title = request.args.get('assignment')
    
    # Get assignment description and date
    # TODO: Add a query for getting the assignment details
    assignment_description = "Just an assignment, nothing to see here"
    assignment_date = "2023-05-04"
    return jsonify({
        'title': assignment_title,
        'description': assignment_description,
        'date': assignment_date
    })

@app.route('/updateAssignment', methods=["GET", "POST"])
def updateAssignment():
    if(request.method == 'POST'):
        data = request.get_json()
        title, description, date = data['title'], data['description'], data['date']

        # Update the assignment
        # TODO: Add query to update database at assignment title

    return jsonify({})


@app.route('/createAssignment', methods=["GET", "POST"])
def createAssignment():
    data = request.get_json()
    title, description, date = data['title'], data['description'], data['date']

    # Check if the assignment title already exists
    check = True

    # Create the assignment
    # TODO: Add query to create new assignment
    if check:   # Success
        # TODO: Compile relevant information into dictionary
        return jsonify({}), 200
    else:       # Failure
        # TODO: Compile relevant information into dictionary
        return jsonify({}), 409


@app.route('/getProfile', methods=["GET", "POST"])
def getProfile():
    # TODO: Get the account type from the session
    # TODO: Get the username from the session
    account_type = 'ADMIN'
    username = 'Username123'

    if account_type == 'STUDENT':
        # Get the account details
        # TODO: Add a query to query profile information from students
        name = "Student name 123"
        email = "Student email 456"
        bio = "Student bio 789"
    elif account_type == 'ADMIN':
        # Get the account details
        # TODO: Add a query to query profile information from students
        name = "Admin name 123"
        email = "Admin email 456"
        bio = "Admin bio 789"
    else:
        # Get the account details
        # TODO: Add a query to query profile information from students
        name = "Guest name 123"
        email = "Guest email 456"
        bio = "Guest bio 789"
    
    details = {
        'username': username,
        'name': name,
        'email': email,
        'bio': bio
    }

    return jsonify(details)


app.secret_key = 'some other random key'


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)