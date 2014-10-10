# coding=utf-8
from flask import Flask

app = Flask(__name__) #inicialização da variável de incialização da aplicação
app.config.from_object('config') #Leitura do ficheiro de configuração config.py

from app import views #chamada do módulo views que controla as acções de acordo com o input