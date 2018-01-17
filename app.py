from flask import Flask, render_template

app = Flask(__name__)


@app.route('/ms5513', methods=['GET'])
def ms5513():
    return render_template('ms5513.html')

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
