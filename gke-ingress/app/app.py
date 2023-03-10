import logging
from flask import Flask, request, make_response

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    # get the session ID from the cookie, or generate a new one
    session_id = request.cookies.get('JESSIONID')
    if session_id is None:
        session_id = generate_session_id()
        logging.debug('******************************************Generated new session ID: %s', session_id)
    else:
        logging.debug('******************************************Using existing session ID: %s', session_id)


    # set the session ID as a cookie in the response with the name "JESSIONID"
    response = make_response('Hello, world!')
    response.set_cookie('JESSIONID', session_id)
    logging.debug('**********************************************Set JESSIONID cookie: %s', session_id)
    return response

def generate_session_id():
    # generate a unique session ID using a library like uuid
    import uuid
    session_id = str(uuid.uuid4())
    logging.debug('**********************************************Generated new session ID: %s', session_id)
    return session_id

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
