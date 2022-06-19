import flask_cors
import flask

app = flask.Flask(__name__)
flask_cors.CORS(app)


@app.route('/api/version')
def version():
    """This function returns the current version
    that is stored on the server.

    Returns:
        json: The current version on the server.
    """
    return flask.jsonify({'version': 2})


@app.route('/api/download')
def download():
    """This function returns update.zip

    Returns:
        file: update.zip
    """
    return flask.send_file('update.zip')


if __name__ == '__main__':
    app.run()
