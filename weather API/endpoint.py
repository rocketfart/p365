import codecs
import sys

from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from findweather import findweather
from model import Base, weatherstation

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

engine = create_engine('sqlite:///weatherstation.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


def postforuser(city, his, user):
    location = request.args.get('city', '')
    his = request.args.get('his', '')
    w_info = findweather(location, his)
    if w_info != "Wrong input":
        weathers = weatherstation(description=unicode(w_info['description']),
                                  temperature=unicode(w_info['temperature']),
                                  pressure=unicode(w_info['pressure']),
                                  humidity=unicode(w_info['humidity']),
                                  user=unicode(user))
        session.add(weatherstation)
        session.commit()
        return jsonify(weathers.serialize)
    else:
        return jsonify({"error": "No weather Found for %s" % (location)})


def getuserrecord(user):
    record = session.query().filter_by(user='user')
    return jsonify([i.serialize for i in record])
