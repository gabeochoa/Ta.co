from flask import Flask, redirect, url_for, session, request, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')
    #return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()