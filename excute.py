from flask import Flask
app = Flask(__name__)

@app.route('/mio')
def tmp():
   return 'palle'

@app.route('/')
def hello_world():
   return '<a href="/switch">Prova</a>'

if __name__ == '__main__':
   app.run()


