from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  #'Hello, Flask!'

@app.route('/about')
def about():
    return render_template('about.html') #'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


