#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request, render_template

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/hello/<string:text>')
@app.route('/hello')
def hello_world(text=None):
    return '"Hello world! Этот сайт приветствует пользователя."' + (' With param ' + text if text else '')


@app.route('/')
@app.route('/home')
def root():
    return flask.render_template(
        'index.html'
    )

@app.route('/sum/<int:a>/<int:b>')
def sum (a, b):
    return ("Сумма двух чисел: " + str(a) + " + " + str(b) + " = " + str(a + b))

@app.route('/sub/<int:a>/<int:b>')
def subtraction (a, b):
    return ("Разность двух чисел: " + str(a) + " - " + str(b) + " = " + str(a - b))

@app.route('/multiply/<int:a>/<int:b>')
def multiplication (a, b):
    return ("Произведение двух чисел: " + str(a) + " * " + str(b) + " = " + str(a * b))

@app.route('/division/<int:a>/<int:b>')
def division (a, b):
    if b != 0:
        return ("Частное двух чисел: " + str(a) + " / " + str(b) + " = " + str(a / b))
    else:
        return("Ошибка, нельзя делить на ноль")

@app.route('/gcd/<int:a>/<int:b>')
def gcd(a, b):
    if a != 0 and b != 0:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return ("НОД двух чисел: " + str(a))
    if a == 0:
        return ("НОД двух чисел: " + str(b))
    if b == 0:
        return ("НОД двух чисел: " + str(a))

@app.route('/exp/<int:a>/<int:b>')
def exponentiation (a, b):
    return ("Возведение первого числа в степень второго: " + str(a) + " ^ " + str(b) + " = " + str(a ** b))

@app.route('/name', methods = ['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        name_param=request.args.get('name')
    elif request.method == 'POST':
        name_param=request.form.get('name')

    if name_param==None:
        name_param="Анонимус"

    return flask.render_template(
        'name.html',
        name=name_param,
        method=request.method
    )

if __name__ == '__main__':
   app.run(debug = True)
