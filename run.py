# from flask import Flask
from application import app
# from flask_ngrok import run_with_ngrok


if __name__ == '__main__':
    if app.config['DEBUG'] == True:
        # run_with_ngrok(app)
        app.run(debug=True)
    else:
        from waitress import serve
        serve(app, port=80)