# -*- coding: utf-8 -*-
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class weatherstation(Base):
    __tablename__ = 'weatherstation'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    temperature = Column(String)
    pressure = Column(String)
    humidity = Column(String)
    user = Column(String)

    # Add a property decorator to serialize information from this database
    @property
    def serialize(self):
        return {
            'description': self.description,
            'temperature': self.temperature,
            'pressure': self.pressure,
            'humidity':self.humidity,
            'id': self.id

        }


engine = create_engine('sqlite:///weatherstation.db')

Base.metadata.create_all(engine)
