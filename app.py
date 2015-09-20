from flask import Flask, redirect, url_for, session, request, render_template
import yelp
from keys import MY_CONSUMER_KEY, MY_CONSUMER_SECRET, MY_ACCESS_TOKEN, MY_ACCESS_SECRET, GOOGLE_CODE
import googlemaps
import urllib

app = Flask(__name__)
app.debug = True


yelp_api = yelp.Api(consumer_key=MY_CONSUMER_KEY,
                    consumer_secret=MY_CONSUMER_SECRET,
                    access_token_key=MY_ACCESS_TOKEN,
                    access_token_secret=MY_ACCESS_SECRET)
gmaps = googlemaps.Client(key=GOOGLE_CODE)
@app.route('/')
def index():
    return render_template('index.html', APIKEY=GOOGLE_CODE, PLACE="Seattle, WA")
    #return render_template('new_index.html', APIKEY=GOOGLE_CODE, PLACE="Seattle, WA")
    #return redirect(url_for('login'))

@app.route('/map/<place>')
def map_place(place=None):
    output = []
    if(place != None):
        if(len(place) == 5):
           output = get_food(place)
    return render_template('map.html', place=place, output=output, process_map=process_map, APIKEY=GOOGLE_CODE)

def getKey(item):
    return item[0].rating

def get_food(place):
    search_results = yelp_api.Search(term="tacos", location=place) # location and search term are required
    places = []
    for business in search_results.businesses:
        #dump(business)
        places.append((business, business.location))
        dump(business.location)

    places = sorted(places, key=getKey, reverse=True)
    return places

def process_map(param):
    return str(param['latitude']) +", "+  str(param["latitude"])

def dump(obj):
  for attr in dir(obj):
    print "obj.%s = %s" % (attr, getattr(obj, attr))

if __name__ == '__main__':
    app.run()