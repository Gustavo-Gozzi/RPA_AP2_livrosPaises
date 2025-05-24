from flask import Flask
from flask_sqlalchemy import SQLAlchemy

paises = Flask(__name__)
paises.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paises.db'
paises.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbpais = SQLAlchemy(paises)

livros = Flask(__name__)
livros.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
livros.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dblivro = SQLAlchemy(livros)
