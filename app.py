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
    promotions = Promotion.query.all()
    return render_template('index.html', promotions=promotions)

@app.route('/add', methods=['GET', 'POST'])
def add_promotion():

    stores = ['1', "w"]
    
    if request.method == 'POST':
        store_name = request.form['store_name']
        promotion_name = request.form['promotion_name']
        start_date = date.fromisoformat(request.form['start_date'])
        end_date = date.fromisoformat(request.form['end_date'])

        promotion = Promotion(store_name=store_name, promotion_name=promotion_name, start_date=start_date, end_date=end_date)
        db.session.add(promotion)
        db.session.commit()

        return redirect('/')

    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_promotion(id):
    promotion = Promotion.query.get(id)

    if request.method == 'POST':
        promotion.store_name = request.form['store_name']
        promotion.promotion_text = request.form['promotion_text']
        promotion.start_date = request.form['start_date']
        promotion.end_date = request.form['end_date']
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('update.html', promotion=promotion)

@app.route('/delete/<int:id>')
def delete_promotion(id):
    promotion = Promotion.query.get(id)
    db.session.delete(promotion)
    db.session.commit()
    return redirect(url_for('index'))




# @app.route('/')
# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()