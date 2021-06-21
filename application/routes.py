from flask import redirect, url_for, render_template, request, Flask
from flask_ngrok import run_with_ngrok
from application import app
from application import actions
# from application import fastpunct

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # pun=fastpunct.punct_obj
    user_input = request.form['input_text']
    reorder = request.form['reorder']
    reorder = True if reorder=="true" else False
    # output=pun.punct(user_input)
    prediction = actions.predict(user_input, reorder)
    # prediction = actions.predict(output, reorder)
    # print(prediction)
    
    # print(prediction.values())
    # print(output)
    return prediction
    # return output