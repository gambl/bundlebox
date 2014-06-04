from flask import Flask, request

app = Flask(__name__)

@app.route("/verify", methods=["GET"])
def verify():
    '''Verify that the application is expecting notifactions from dropbox webhooks by returing the challenge'''

    return request.args.get('challenge')

@app.route("/hello")
def hello():
    '''Verify that the application is expecting notifactions from dropbox webhooks by returing the challenge'''

    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)
