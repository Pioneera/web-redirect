import os

from flask import Flask,redirect

app = Flask(__name__)

@app.route('/')
def generic_redirect():
    redirect_type = os.environ.get('REDIRECT_TYPE', '302')
    redirect_target = os.environ.get('REDIRECT_TARGET', 'https://www.pioneera.com/')
    return redirect(redirect_target, code=redirect_type)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
