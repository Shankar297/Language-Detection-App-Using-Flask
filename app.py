from flask import Flask, render_template, request, url_for
from textblob import TextBlob

app = Flask('__name__')

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/change',methods = ['POST'])
def change():
    if request.method == 'POST':
        received_text = request.form['rawtext']
        text = TextBlob(received_text)
        if text=='':
            return render_template('home.html')
        lang = text.detect_language()
        if lang=='en':
            lang = 'English'
        elif lang =='mr':
            lang = 'Marathi'
        elif lang == 'te':
            lang ='Telugu'
        elif lang == 'bn':
            lang == 'Bengali'
        elif lang == 'hi':
            lang == 'Hindi'
        eng = text.translate(to='en')
    return render_template('home.html',received_text = received_text, lang = lang, eng = eng)
    

if __name__ =='__main__':
    app.run(debug=True)