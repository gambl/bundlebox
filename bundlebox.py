from flask import Flask, request
from hashlib import sha256
import hmac
import threading
import json

app = Flask(__name__)

@app.route("/webhook", methods=["GET"])
def verify():
    '''Verify that the application is expecting notifactions from dropbox webhooks by returing the challenge'''

    return request.args.get('challenge')


@app.route("/webhook", methods=["POST"])
def log_request():
  "Just log the request at the moment"

   # Make sure this is a valid request from Dropbox
  signature = request.headers.get('X-Dropbox-Signature')
  if signature != hmac.new(APP_SECRET, request.data, sha256).hexdigest():
      abort(403)

  print json.dumps(request.data,indent=4)

#  for uid in json.loads(request.data)['delta']['users']:
        # We need to respond quickly to the webhook request, so we do the
        # actual work in a separate thread. For more robustness, it's a
        # good idea to add the work to a reliable queue and process the queue
        # in a worker process.
        #threading.Thread(target=process_user, args=(uid,)).start()


  return ''


@app.route("/hello")
def hello():
    '''Verify that the application is expecting notifactions from dropbox webhooks by returing the challenge'''

    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)
