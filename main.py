from flask import Flask # from packeg flask, 'Flask' class is called

app = Flask(__name__)  # app is an oobject of class Flask now. in parenthisis we have to give a name 
@app.route("/")
def hello_world():
  return "Hello world "

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)