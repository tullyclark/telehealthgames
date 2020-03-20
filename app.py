import flask


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = config.flask_secret_key

if __name__ == '__main__':
	app.run(debug = config.debug)