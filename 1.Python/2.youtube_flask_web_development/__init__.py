# coding=utf-8
__author__ = 'tmagalhaes'

#importancao do modulo de flask
from flask import Flask, render_template, url_for

#inicializacao do modulo flask
app = Flask(__name__)

#definicao accoes root path
@app.route('/')
def homepage():

    title = "Epic Tutorial"
    paragraph = ["I am learning so much fun stuff","I am the best guy in the world"]

    return render_template("index.html", title = title, paragraph=paragraph)

#Manipulação de if statement com o auxilio da variável pagetype
@app.route('/about')
def aboutpage ():

    title = "About this page"
    paragraph = ["bla bla bla bla memememe"]

    pagetype = "about"

    return render_template("about.html", title=title, paragraph=paragraph, pagetype=pagetype)


#inicializacao do webserver
if __name__ == "__main__":
    app.run()