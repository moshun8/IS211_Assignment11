#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 11 Flask'''

from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)

toDoList = []
emailPattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

@app.route('/')
def hello_world():
    return render_template('index.html', toDoList=toDoList)

@app.route('/submit', methods=['POST'])
def submit():

    email = request.form['email']
    newItem = request.form['newItem']
    priority = request.form['priority']

    if re.match(emailPattern, email) is None:
        return redirect('/')
    elif len(newItem) == 0:
        return redirect('/')
    elif priority not in ('low', 'medium', 'high'):
        return redirect('/')
    else:
        toDoList.append((email, newItem, priority))
        return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    toDoList[:] = []
    return redirect('/')

if __name__ == "__main__":
    app.run()