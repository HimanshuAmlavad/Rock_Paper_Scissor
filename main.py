
from flask import Flask, render_template , session

app = Flask(__name__)
app.secret_key = 'Rock_Paper_scissors'

@app.route('/' , methods = ['POST', 'GET'])
def home():
    return render_template('Game_page.html')

if __name__ =="__main__":
    app.run(debug=True)    
   