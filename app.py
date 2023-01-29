from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'こんにちは、世界！今日も未来は明るい。'


if __name__ == '__main__':
    app.run()