from flask import Flask, session, jsonify
from model import User

app = Flask(__name__)

def login(user: User):
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

def protected(user: User):
    if user in session:
        return jsonify({'message': 'This is a protected resource!'}), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401

#@bp.route('/logout')
#def logout():
#    session.pop('user', None)
#    return jsonify({'message': 'Logged out successfully'})

