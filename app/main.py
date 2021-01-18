from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_wordl():
    return("Hola Mundo, soy python!")

@app.route('/bye')
def byeworld():
    return("adios mundo cruel")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
