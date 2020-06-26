from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)


@app.route('/', methods=['GET', 'POST'])
def get():
    if request.method == "GET":
        users = User.query.all()
        user = User(firstname='',lastname='',email='',password='')
        pagename = 'home'
        return render_template('home.html',pagename=pagename,users=users,user=user)
    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete= User.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.firstname = request.form['firstname']
        user.lastname = request.form['lastname']
        user.email = request.form['email']
        user.password = request.form['password']
        db.session.commit()
        return redirect('/')

    else:
        pagename = 'updatehome'
        users = User.query.all() 
        return render_template('home.html',pagename=pagename,user=user, users=users)


if __name__ == '__main__':
    app.run(debug=True)
