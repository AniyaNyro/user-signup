from flask import Flask, request, redirect, render_template, session, flash
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

app.secret_key = "234askfj"
    
@app.route("/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        if not is_email(email) or email == "":
            flash(email + 'does not seem like an email address')
            return redirect('/')
        if password != verify:
            flash('passwords did not match')
            return redirect('/')
        if password == "":
           flash('You did not enter a password.')
           return redirect('/')   
        return render_template('signed-up.html', username=username)
    return render_template('signup.html')
        
def is_email(string):
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present

app.run()