# 这是一个最牛逼的飞机大战（没有之一！！！）
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index2018():
	num = 100
	num3 = 300
	return 'hello world'


if __name__ == '__main__':
	app.run()
