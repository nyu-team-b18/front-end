from flask import Flask, request, session, redirect, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    

@app.route('/logout', methods=["GET", "POST"])
def logout():
    # TODO: Destroy all session variables
    return jsonify({})


@app.route('/getAssignments', methods=["GET"])
def getAssignments():
    # Get class assignments
    # TODO: Add query for getting assignments

    assignments = [f'Assignment {i+1}' for i in range(3)]

    return jsonify({
        'assignments': assignments,
    })

@app.route('/getStudents', methods=["GET"])
def getStudents():
    # Get class students
    # TODO: Add query for getting students

    students = [
            {
                'name': f'Student {i}',
                'username': f'Username{i}'
            }
            for i in range(1,11)
        ]

    return jsonify({
        'students': students
    })

@app.route('/getAccountType', methods=["GET"])
def getAccountType():
    # Get account type
    # TODO: Check session for account type

    account_type = 'NONE'

    return jsonify({'account-type':account_type})

@app.route('/getAssignmentDetails', methods=["GET"])
def getAssignmentDetails():
    # GET args
    assignment_title = request.args.get('assignment')
    
    # Get assignment description and date
    # TODO: Check if signed in as a student or admin
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


@app.route('/getProfile', methods=["GET"])
def getProfile():
    # TODO: Get the account type from the session
    # TODO: Get the username from the session
    account_type = 'STUDENT'
    username = 'Username123'

    if account_type == 'STUDENT':
        # Get the account details
        # TODO: Add a query to query profile information from students
        name = "Student name 123"
        email = "Student email 456"
        bio = "Student bio 789"
    elif account_type == 'ADMIN':
        # Get the account details
        # TODO: Add a query to query profile information from admins
        name = "Admin name 123"
        email = "Admin email 456"
        bio = "Admin bio 789"
    else:
        # Get the account details
        # TODO: Add a query to query profile information from guests
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


@app.route('/updateProfile', methods=['GET', 'POST'])
def updateProfile():
    # TODO: Get the account type from the session
    # TODO: Get the username from the session
    account_type = 'ADMIN'
    username = 'Username123'

    data = request.get_json()
    name, email, bio = data['name'], data['email'], data['bio']

    if account_type == 'STUDENT':
        # Get the account details
        # TODO: Add a query to update profile information from students
        pass
    elif account_type == 'ADMIN':
        # Get the account details
        # TODO: Add a query to update profile information from admins
        pass
    else:
        # Get the account details
        # TODO: Add a query to update profile information from guests
        pass
    
    return jsonify({})


@app.route("/deleteAccount", methods=["GET", "DELETE"])
def deleteAccount():
    # TODO: Get the account type from the session
    # TODO: Get the username from the session
    account_type = 'ADMIN'
    username = 'Username123'

    if account_type == 'ADMIN':
        # TODO: Change all students under this admin to guest accounts

        # TODO: Delete this account from admin table
        pass
    elif account_type == 'GUEST':
        # TODO: Delete this account from guest table
        pass

    # TODO: Destroy all session variables

    return jsonify({})

@app.route("/getStudentInformation", methods=["GET"])
def getStudentInformation():
    # GET args
    student_username = request.args.get('username')

    # Get student information 
    # TODO: Add a query to get student details
    name = 'Johnathan Dope'
    email = 'johnnydoe11@gmail.com'
    bio = 'Hey, this is my super cool bio!'

    # Get all completed assignments
    # TODO: Add a query that gets all assignment titles completed by this student
    assignments = [f'Assignment {i}' for i in range(1,4)]

    return jsonify({
        'username': student_username,
        'name': name,
        'email': email,
        'bio': bio,
        'assignments': assignments
    })

@app.route("/dropStudent", methods=["GET", "POST"])
def dropStudent():
    data = request.get_json()
    student_username = data['username']

    # Move student account to guest account
    # TODO: Add a query to create a new guest account

    # Delete the old student account
    # TODO: Add a query to delete the old student account

    return jsonify({})


app.secret_key = 'some other random key'


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)