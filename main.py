from flask import Flask, render_template,jsonify # from packeg flask, 'Flask' class is called. jsonify is use to convet data(jobs) into json object.

app = Flask(__name__)  # app is an oobject of class Flask now. in parenthisis we have to give a name 

jobs=[{'id':1,
      'title':'Data Science',
      'location':'New Delhi',
      'Salary':'$10000'},
      {'id':2,
      'title':'Data analyst',
      'location':'Delhi',
      'Salary':'$9000'},
      {'id':3,
      'title':'Data engineer',
      'location':'Delhi NCR',
      'Salary':'$12000'},
      {'id':4,
      'title':'Data entry',
      'location':'Delhi',
      'Salary':'$6000'},
      {'id':5,
      'title':'Analyst Businees',
      'location':'Noida',
      'Salary':'$75000'},
      {'id':6,
      'title':'Software developer',
      'location':'Gurgrame',
      'Salary':'$18000'},
      {'id':7,
      'title':'Python developer',
      'location':'Mumbai'
      }
     ]

@app.route("/")
def hello_world():
  return render_template('home.html',job=jobs,company="Jatela")


@app.route("api/jobs") # api is stand to use here as it represent this url will not retuen HTML website.
def list_jobs():
  return jsonify(jobs)



if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)