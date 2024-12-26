import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/' , methods = ['POST', 'GET'])
def home():
    return render_template('Game_page.html')

if __name__ =="__main__":
    app.run(debug=True)    
   