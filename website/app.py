import string
from flask import Flask, render_template, request
import pickle

#constants for scaling input
AVMIN = 0
AVMAX = 5
MINNMIN = 1
MINNMAX = 1250

#means for calculated host listings count, reviews per month, number of reviews
CHLC = 0.019214
NREV = 0.081714
REVM = 0.075670

#reading model
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#for scaling availability 365
def minmax_avail365(av3):
    #bucket into 0-5 range
    if av3 <= 17.16666664: #2week
        av3t = 0
    elif av3 <= 2*17.16666664: #1month
        av3t = 1
    elif av3 <= 6*17.16666664: #3month
        av3t = 2
    elif av3 <= 12*17.16666664: #6month
        av3t = 3
    elif av3 <= 18*17.16666664: #9month
        av3t = 4
    elif av3 <= 24*17.16666664: #12month
        av3t = 5
    #scale minmax
    scaled_av = (av3t - AVMIN)/(AVMAX - AVMIN)
    return scaled_av

#for scaling minimum nights
def minmax_night(minn):
    scaled_minn = (minn - MINNMIN)/(MINNMAX - MINNMIN)
    return scaled_minn

#for assigning variables for neighbourhood group
def ng_decode(ng_user):
    #return ngB, ngM, ngQ, ngS, ngBronx
    if (ng_user == 'Manhattan'):
        return (0, 1, 0, 0, 0)
    elif (ng_user == 'Brooklyn'):
        return (1, 0, 0, 0, 0)
    elif (ng_user == 'Queens'):
        return (0, 0, 1, 0, 0)
    elif (ng_user == 'Staten Island'):
        return (0, 0, 0, 1, 0)
    elif (ng_user == 'Bronx'):
        return (0, 0, 0, 0, 1)

def rt_decode(rt_user):
    #return rt_p, rt_s, rt_e
    if (rt_user == 'Shared'):
        return (0, 1, 0) 
    elif (rt_user == 'Private'):
        return (1, 0, 0)
    else:
        return (0, 0, 1)
#loading site
@app.route("/")
def hello():
    return render_template('index.html')

#prediction goes here
@app.route("/predict", methods=['POST'])
def predict():
    #taking raw input from user
    a = string(request.form['neighbourhood_group'])
    b = string(request.form['room_type'])
    c = int(request.form['minimum_nights'])
    d = int(request.form['availability_365'])
    
    #scaling
    a36 = minmax_avail365(d)
    minight = minmax_night(c)
    ngB, ngM, ngQ, ngS, ngBronx = [i for i in ng_decode(a)]
    rt_p, rt_s, rt_e = [i for i in rt_decode(b)]
    
    #constructing processed inputs to put into model
    #minn, nrev, revm, chlc, a36, ngB, ngM, ngQ, ngS, N
    input_arr = [minight, NREV, REVM, CHLC, a36, ngBronx, ngB, ngM, ngQ, ngS, rt_e, rt_p, rt_s]
    outex = model.predict([input_arr])
    output = round(outex[0], 2)
    return render_template('index.html', prediction_text='The prize of the hotel you looking for is')

if __name__ == "__main__":
    app.run()
