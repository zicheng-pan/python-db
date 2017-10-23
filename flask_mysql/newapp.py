from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:109427@localhost/news'
db=SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<User %s>' % self.username

@app.route('/')
@app.route('/hello/<id>/')
def hello_world(id=None):
    return 'hello,world %s' %id

def addUser(id,username,email):
    news = News(username=username,email=email)
    db.session.add(news)
    db.session.commit()

@app.route('/emails')
def emails():
    addUser(id=1,username='xiaohong1',email='10129@qq.com')
    items = News.query.all()
    return render_template('table.html',items=items)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)