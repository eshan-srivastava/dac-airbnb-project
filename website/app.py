import string
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    a = string(request.form['neighbourhood_group'])
    b = string(request.form['room_type'])
    c = int(request.form['minimum_nights'])
    d = int(request.form['availability_365'])
    e = model.predict([[a, b, c, d]])
    output = round(e[0], 2)
    return render_template('index.html', prediction_text='The prize of the hotel you looking for is')


if __name__ == "__main__":
    app.run()
