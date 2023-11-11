from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database_notice.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Notice(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(15), nullable = False)
    heading  = db.Column(db.String(30), nullable = False)
    description = db.Column(db.Text)

    def __repr__(self) -> str:
        return f"<Notice {self.heading}>"

# Pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/notice")
def noticeBoard():
    notices = Notice.query.all()
    notices = notices[::-1]
    return render_template("notice.html", notices = notices)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/teachers")
def teachers():
    return render_template("teachers.html")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == "POST":
        id = int(request.form['id'])
        date = str(request.form['date'])
        date = str(datetime.datetime.strptime(date, "%Y-%M-%d").strftime("%d/%m/%Y"))
        heading = str(request.form['heading'])
        description = str(request.form['description'])

        noticeElement = Notice(id = id, date = date, heading = heading, description = description)
        db.session.add(noticeElement)

        db.session.commit()

        return render_template("redirect.html")
    return render_template("admin.html")

@app.errorhandler(404 or 503)
def not_found(e):
  return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True, port=8080)