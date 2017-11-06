from flask import Flask, jsonify, request, abort, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from usermodel import Base, User
from endpoint import getuserrecord,postforuser
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

engine = create_engine('sqlite:///users.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@auth.verify_password
def verify_password(username, password):
    user = session.query(User).filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@app.route('/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        print "missing arguments"
        abort(400)

    if session.query(User).filter_by(username=username).first() is not None:
        print "existing user"
        user = session.query(User).filter_by(username=username).first()
        return jsonify({'message': 'user already exists'}), 200

    user = User(username=username)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify(
        {'username': user.username}), 201

@app.route('/weather', methods = ['POST'])
@auth.login_required
def all_restaurants_handler():
    if request.method == 'POST':
        # MAKE A NEW weather AND STORE IT IN DATABASE
        location = request.args.get('city', '')
        his = request.args.get('his', '')
        user=g.user.id
        postforuser(location,his,user)

@app.route('/api/users/<int:id>')
def get_user(id):
    user = session.query(User).filter_by(id=id).one()
    if not user:
        abort(400)
    return jsonify({'username': user.username})

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hey, this is your history %s' % getuserrecord(g.user.id)})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)