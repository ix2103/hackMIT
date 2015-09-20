from flask import Flask
from flask import request
from flask import render_template
import processTweet as pt
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/output.JSON', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = pt.getJSON(text)
    return processed_text

if __name__ == '__main__':
    app.run()
