from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('flight_rf.pkl','rb'))

@app.route('/')
@cross_origin()
def home():
      return render_template('home.html')

@app.route('/predict',methods =['GET','POST'])
@cross_origin()
def predict():
      if request.method=='POST':
            
            #Date_of_journey
            date_dep=request.form['Dep_Time']
            Journey_date=int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').day)
            Journey_month=int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').month)
            
            #Departure
            Dep_Hour=int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').hour)
            Dep_Minute=int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').minute)
            
            #Arrival
            date_arr=request.form['Arrival_Time']
            Arrival_Hour=int(pd.to_datetime(date_arr, format='%Y-%m-%dT%H:%M').hour)
            Arrival_Minute=int(pd.to_datetime(date_arr, format='%Y-%m-%dT%H:%M').minute)
            
            #Duration
            Duration_hours=abs(Arrival_Hour-Dep_Hour)
            Duration_mins=abs(Arrival_Minute-Dep_Minute)
            
            #Total Stops
            Total_Stops=int(request.form['Stops'])
            
            #Airline
            #AIR ASIA = 0 (not in column)
            airline=request.form['airline']
            if(airline=='Jet Airways'):
                  Jet_Airways = 1
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='IndiGo'):
                  Jet_Airways = 0
                  IndiGo = 1
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='Air India'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 1
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='Multiple carriers'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 1
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='SpiceJet'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 1
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='Vistara'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 1
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='GoAir'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 1
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='Multiple carriers Premium economy'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 1
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='Jet Airways Business'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 1
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            elif(airline=='Vistara Premium economy'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 1
                  Trujet = 0
                  
            elif(airline=='Trujet'):
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 1
                  
            else:
                  Jet_Airways = 0
                  IndiGo = 0
                  Air_India = 0
                  Multiple_carriers = 0
                  SpiceJet = 0
                  Vistara = 0
                  GoAir = 0
                  Multiple_carriers_Premium_economy = 0
                  Jet_Airways_Business = 0
                  Vistara_Premium_economy = 0
                  Trujet = 0
                  
            #Source
            #Bangalore = 0 (not in column)
            Source=request.form['Source']
            if(Source=='Delhi'):
                  s_Delhi= 1
                  s_Kolkata= 0
                  s_Mumbai= 0
                  s_Chennai= 0
                  
            elif(Source=='Kolkata'):
                  s_Delhi= 0
                  s_Kolkata= 1
                  s_Mumbai= 0
                  s_Chennai= 0
                  
            elif(Source=='Mumbai'):
                  s_Delhi= 0
                  s_Kolkata= 0
                  s_Mumbai= 1
                  s_Chennai= 0
                  
            elif(Source=='Chennai'):
                  s_Delhi= 0
                  s_Kolkata= 0
                  s_Mumbai= 0
                  s_Chennai= 1
                  
            else:
                  s_Delhi= 0
                  s_Kolkata= 0
                  s_Mumbai= 0
                  s_Chennai= 0
                  
            #Destination
            #Bangalore= 0 (not in column)
            Destination= request.form['Destination']
            if(Destination=='Cochin'):
                  d_Cochin= 1
                  d_Delhi= 0
                  d_New_Delhi= 0
                  d_Hyderabad= 0
                  d_Kolkata= 0
                  
            elif(Destination=='Delhi'):
                  d_Cochin= 0
                  d_Delhi= 1
                  d_New_Delhi= 0
                  d_Hyderabad= 0
                  d_Kolkata= 0
                  
            elif(Destination=='New_Delhi'):
                  d_Cochin= 0
                  d_Delhi= 0
                  d_New_Delhi= 1
                  d_Hyderabad= 0
                  d_Kolkata= 0
                  
            elif(Destination=='Hyderabad'):
                  d_Cochin= 0
                  d_Delhi= 0
                  d_New_Delhi= 0
                  d_Hyderabad= 1
                  d_Kolkata= 0
                  
            elif(Destination=='Kolkata'):
                  d_Cochin= 0
                  d_Delhi= 0
                  d_New_Delhi= 0
                  d_Hyderabad= 0
                  d_Kolkata= 1
                  
            else:
                  d_Cochin= 0
                  d_Delhi= 0
                  d_New_Delhi= 0
                  d_Hyderabad= 0
                  d_Kolkata= 0
                  
            prediction=model.predict([[Total_Stops,Journey_date,Journey_month,Dep_Hour,Dep_Minute,Arrival_Hour,Arrival_Minute,
                                       Duration_hours,Duration_mins,Jet_Airways,IndiGo,Air_India,Multiple_carriers,SpiceJet,
                                       Vistara,GoAir,Multiple_carriers_Premium_economy,Jet_Airways_Business,Vistara_Premium_economy,
                                       Trujet,s_Delhi,s_Kolkata,s_Mumbai,s_Chennai,d_Cochin,d_Delhi,d_New_Delhi,d_Hyderabad,
                                       d_Kolkata]])
            
            output=round(prediction[0],2)
            return render_template('home.html',prediction_text='Your Flight Price is Rs. {}'.format(output))
      return render_template('home.html')

if __name__=='__main__':
      app.run(debug=True)