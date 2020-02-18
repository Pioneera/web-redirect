import os
import logging
import sys

from flask import Flask,redirect

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

app = Flask(__name__)

redirect_type = int(os.environ.get('REDIRECT_TYPE', '302'))
redirect_target = os.environ.get('REDIRECT_TARGET', 'https://www.pioneera.com/')
listening_port=int(os.environ.get('PORT', 8080))

logging.debug('Adding redirection handling to target %s with code %d',redirect_target,redirect_type)

@app.route('/')
def generic_redirect():
    return redirect(redirect_target, code=redirect_type)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=listening_port)
