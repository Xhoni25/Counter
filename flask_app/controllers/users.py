from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/play')
def addLike():
    if 'counter'in session:
        session ['counter']= session ['counter'] + 1
        return render_template('counter.html')
    session['counter']= 0
    return render_template ('counter.html')

@app.route('/reset')
def resetLikes():
    session.clear()
    return redirect('/play')