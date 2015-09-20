from flask import Flask, redirect, url_for, session, request, render_template
import yelp
import keys

app = Flask(__name__)
app.debug = True

yelp_api = yelp.Api(consumer_key=MY_CONSUMER_KEY,
                    consumer_secret=MY_CONSUMER_SECRET,
                    access_token_key=MY_ACCESS_TOKEN,
                    access_token_secret=MY_ACCESS_SECRET)

@app.route('/')
def index():
    return render_template('index.html')
    #return redirect(url_for('login'))

@app.route('/map/<place>')
def map_place(place=None):
    output = []
    if(place != None):
        output = get_food(place)
    return render_template('map.html', place=place, output=output)

def get_food(place):
    search_results = yelp_api.Search(term="my search term", location="my location") # location and search term are required
    places = []
    for business in search_results.businesses:
        print business.name
        places.append(business.name)
    return places

if __name__ == '__main__':
    app.run()