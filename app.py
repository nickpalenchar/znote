from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'


@app.route('/')
def hello():   
    return render_template('new.html', user=session.get('user', None))


@app.route('/mocklogin')
def mock_login():
    session['user'] = { 'user': 'null' }
    return 'you are now logged in for testing purposes'

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run()
