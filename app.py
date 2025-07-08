# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 11:36:58 2025

@author: Nasimjon
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
responses = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    name = request.form['name']
    club = request.form['club']
    responses[name] = club
    return redirect(url_for('results'))

@app.route('/results')
def results():
    psg_votes = sum(1 for vote in responses.values() if vote.lower() == 'psg')
    bayern_votes = sum(1 for vote in responses.values() if vote.lower() == 'bayern')
    total = psg_votes + bayern_votes

    if total == 0:
        psg_percent = bayern_percent = 0
    else:
        psg_percent = round((psg_votes / total) * 100, 1)
        bayern_percent = round((bayern_votes / total) * 100, 1)

    return render_template('results.html',
                           responses=responses,
                           psg=psg_votes,
                           bayern=bayern_votes,
                           psg_percent=psg_percent,
                           bayern_percent=bayern_percent,
                           total=total)

if __name__ == '__main__':
    app.run(debug=True)
