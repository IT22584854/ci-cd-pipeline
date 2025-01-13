from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello from CI/CD powerd Flask app! v2"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')