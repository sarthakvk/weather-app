from forms import myform
from flask import Flask, render_template, flash, redirect, url_for
from geopy.geocoders import Nominatim
from darksky.api import DarkSky
import requests
import keyring

def weather_json(arr):
    your_darksky_api=keyring.get_password('dark_sky_api','sarthak')
    url = 'https://api.darksky.net/forecast/'+your_darksky_api+'/'+str(arr[0])+','+str(arr[1])
    jsn = requests.get(url)

    result = jsn.json()
    return(result)

def current(arr):
    result = weather_json(arr)

    dic={} # Result Dictionary
    fer = result['currently']['temperature']
    cel = (fer-32)*(5/9) # Fahrenheit to Celsius conversion
    hum = int(result['currently']['humidity'] * 100) # Humidity on percentage
    dic["Overall Weather"]=result['currently']['summary']
    dic["Current Temperature in C"]="%.2f" % cel
    dic["Current Temperature in F"]="%.2f" %fer
    dic["Current Humidity"]=hum
    dic["Current Wind Speed"]=result['currently']['windSpeed']
    dic["Current Wind Pressure"]=result['currently']['pressure']
    return(dic)



API_KEY = keyring.get_password('dark_sky_api','sarthak')

darksky = DarkSky(API_KEY)


geolocator = Nominatim(user_agent="app.py",timeout=10)

app = Flask(__name__)

app.config['SECRET_KEY'] = "sbvfet32vob4q6vr87q6tc32b934e3qwdesdadasanxu98eb213x2asdaav"
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = keyring.get_password('recapcha_pub','sarthak')
app.config['RECAPTCHA_PRIVATE_KEY'] = keyring.get_password('recapcha_private','sarthak')
app.config['RECAPTCHA_OPTIONS']= {'theme':'white'}

@app.route("/",methods = ('GET','POST'))
def index():
    location = False
    forcast = False
    form = myform()
    if form.validate_on_submit():
        try:
            location = geolocator.geocode(form.location.data)
            forcast =  current([location.latitude, location.longitude])
            form.location.data = ""
        except:
            flash("Please enter your location")
            return redirect(url_for('index'))


    return render_template("index.html",form=form,location = location,forcast = forcast)


if __name__ == '__main__':
    app.run(debug=True)
