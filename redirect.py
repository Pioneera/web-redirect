import os
import logging

from flask import Flask,redirect

app = Flask(__name__)

redirect_type = int(os.environ.get('REDIRECT_TYPE', '302'))
redirect_target = os.environ.get('REDIRECT_TARGET', 'https://www.pioneera.com/')
listening_port=int(os.environ.get('PORT', 8080))

logging.debug('Adding redirection handling to target %s with code %d',redirect_target,redirect_type)

@app.route('/')
def root():
    return redirect(redirect_target, code=redirect_type)

@app.route('/<path:page>')
def anypage(page):
    return redirect('{new_url}#{page}'.format(page=page, new_url=redirect_target), code=redirect_type)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=listening_port)
