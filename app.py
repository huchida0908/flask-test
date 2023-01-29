from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///promotions.db'
db = SQLAlchemy(app)

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)
    promotion_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

@app.route('/')
def index():
    # promotions = Promotion.query.all()
    # return render_template('index.html', promotions=promotions)
    return "ffffff"

if __name__ == '__main__':
    app.run()