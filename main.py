from flask import Flask, render_template, jsonify  # from packeg flask, 'Flask' class is called. jsonify is use to convet data(jobs) into json object.
from Database import load_job_from_db  # to access other python files. (Database.py)


app = Flask(__name__)  # app is an oobject of class Flask now. in parenthisis we have to give a name


@app.route("/")
def hello_world():
  jobs = load_job_from_db()
  return render_template('home.html', job=jobs, company="Jatela")


@app.route("/api/jobs") # api is stand to use here as it represent this url will not returnHTML website."/" is important in starting.
def list_jobs():           # this function will show data in json formate.
  jobs = load_job_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)



# # this is a python standard that what framework we are using we have to provide them in this requirements.txt file.
# flask
# gunicorn : to put a flask application into production we have to use gunicorn.