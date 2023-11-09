from flask import Flask , render_template ,request
import pandas as pd
import numpy as np
import sklearn
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

with open("D:\Car Price Prediction preject\models\scaler.pkl",'rb') as file:
    scaler = pickle.load(file)
with open('D:\Car Price Prediction preject\models\prediction_obj.pkl','rb') as file:
    ridge = pickle.load(file)


@app.route('/')
def forent_page():
    return render_template('index.html')

@app.route('/predictdata',methods=['POST','GET'])
def predict_car_price():

    if request.method == 'POST':

        Present_Price = float(request.form.get('Present_Price'))
        Kms_Driven = float(request.form.get('Kms_Driven'))
        n_year = int(request.form.get('n_year'))

        Fuel_Type = request.form.get('Fuel_Type')

        if Fuel_Type=='Petrol':
            Fuel_Type = 1
            Fuel_Type = int(Fuel_Type)
        else:
            Fuel_Type = 0
            Fuel_Type = int(Fuel_Type)

        
        Seller_Type = request.form.get('Seller_Type')

        Seller_Type_Individual = 0
        Seller_Type_Dealer = 0


        if Seller_Type=='Dealer':
            Seller_Type_Dealer = 1       
           
        else:
            Seller_Type_Individual = 1


        Transmission = request.form.get('Transmission')

        Transmission_Automatic = 0
        Transmission_Manual = 0

        if Transmission=='Automatic':
            Transmission = 1
            Transmission_Automatic = 1
        else:
            Transmission_Manual = 1
            

        result = ridge.predict(scaler.transform([[Present_Price,Kms_Driven,n_year,Fuel_Type,Seller_Type_Dealer,Seller_Type_Individual,Transmission_Automatic,Transmission_Manual]]))

        
        return render_template("result.html",result=result)
    
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=500)
