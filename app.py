from flask import Flask, redirect, url_for, session, request, render_template

app = Flask(__name__)
app.debug = True

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
    return []

if __name__ == '__main__':
    app.run()