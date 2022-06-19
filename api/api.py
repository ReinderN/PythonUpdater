import flask_cors
import flask

app = flask.Flask(__name__)
flask_cors.CORS(app)


@app.route('/api/version')
def version():
    return flask.jsonify({'version': 2})


@app.route('/api/download')
def download():
    # return a zip file containing the update
    return flask.send_file('update.zip')


if __name__ == '__main__':
    app.run()
