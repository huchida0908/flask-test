from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return 'こんにちは、世界！今日も未来は明るい。'


if __name__ == '__main__':
    app.run()