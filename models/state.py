#!/usr/bin/python3
""" State Module for HBNB project. """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """
        returns the list of City instances with state_id equals
        to the current State.id
        """
        from models import storage
        alike_cities = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                alike_cities.append(city)
        return alike_cities
    
