from flask import Flask, session, render_template, request, redirect, url_for
from datetime import timedelta
from googletrans import Translator

translator = Translator()

app = Flask(__name__)
app.secret_key = "password"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/')
def home():
    greeting = _("Hello, World!")
    return render_template('index.html', greeting=greeting)


@app.route('/index2')
def home2():
    return render_template('index2.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.clear()
    return redirect(url_for('login'))


@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
