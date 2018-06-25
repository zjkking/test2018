from flask import Flask

app = Flask(__name__)


@app.route('/')
def index2018():
	num = 100
	return 'hello world'


if __name__ == '__main__':
	app.run()
