from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    # Make changes here
    return 'Hello World'
if __name__ == '__main__':
    # app.run(host, port, debug, options)
    app.run(host = "127.0.0.1", port = 5000)