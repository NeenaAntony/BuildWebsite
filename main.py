from flask import Flask,render_template,url_for

app=Flask(__name__)

## Create Index Page
@app.route('/')
def indexPage():
    first_name='All'
    favorite_Color=['White','Green','Yellow','Orange']
    return render_template('index.html',fname=first_name,fav_Color=favorite_Color)

## Create About Page
@app.route('/about')
def aboutPage():
    return render_template('about.html')


app.run(port=5001,debug=True)