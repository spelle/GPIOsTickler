from flask import Flask, request, render_template, url_for, session, redirect, abort, make_response

app = Flask( __name__ )

# set the secret key.  keep this really secret:
app.secret_key = 'S3cr37_K3y!'

lps = { 'tux' : 'tux' , 'thorgal' : 'aegirsson' , 'gaston' : 'lagaffe' }

@app.route( '/welcome' )
def welcome() :
    if 'username' in session :
        resp = make_response(render_template('welcome.html'))
        resp.set_cookie('username', session['username'])
        return resp
        return 'Identification reussie, {0} !\n'.format(session['username'])
    else :
        return redirect(url_for('logout'))

@app.route( '/login', methods=['GET','POST'] )
def login() :
    if request.method == 'POST' :
        for u in lps.keys() :
            if u == request.form['user'] and lps[u] == request.form['passwd'] :
                session['username'] = request.form['user']
                return redirect(url_for('welcome'))
        return redirect(url_for('logout'))
    else :
        return render_template('login.html')

@app.route( '/' )
def index():
    if 'username' in session :
        return redirect(url_for('welcome'))
    else :
        return redirect(url_for('login'))

@app.route( '/logout' )
def logout():
    # remove the username from the session if it's there
    session.pop('username ', None)
    return redirect(url_for('index'))

if __name__ == '__main__' :
    app.run()
