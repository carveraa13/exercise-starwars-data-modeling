import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    fullname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favcharacter = relationship('CharacterFavorite')
    favplanet = relationship('PlanetFavorite')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String)
    height = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(25))
    likeuser = relationship('CharacterFavorite')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(50))
    population = Column(Integer)
    climate = Column(String(25))
    terrain = Column(String(25))
    surface_water = Column(Integer)
    likeuser = relationship('PlanetFavorite')
    

class CharacterFavorite(Base):
    __tablename__ = 'characterfavorite'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.id'))
    characterid = Column(Integer, ForeignKey('character.id'))


class PlanetFavorite(Base):
    __tablename__ = 'planetfavorite'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.id'))
    planetid = Column(Integer, ForeignKey('planet.id'))

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')