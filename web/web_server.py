from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


def start_server(debug=False):
    app.run(debug=debug)


if __name__ == '__main__':
    start_server()
