from sqlalchemy import create_engine, text
import os # os(operating system variable)

db_connection_string = os.environ['db_connection_string']

# #db_connection_string="mysql+pymysql://xcjk4oomf61nyf1gr8ot:pscale_pw_9RrGLyTigQazcLhxVmxBfre1GlFpvkb85hwAnax8JPY@aws.connect.psdb.cloud/dikshant?charset=utf8mb4"      (never put any passwords in github)

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_job_from_db():
  with engine.connect() as conn:
    cursor = conn.execute(text("select * from jobs"))
    
    jobs = []
    
    # get column names from cursor object
    keys = [desc[0] for desc in cursor.cursor.description]
    
    for row in cursor.fetchall():
      jobs.append(dict(zip(keys, row)))
  return jobs








# engine = create_engine(
#   db_connection_string,
#   connect_args={
#     "ssl":{
#       "ssl_ca": "/etc/ssl/cert.pem"
#     }
#   })

# def load_job_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
    
#     jobs = []  #empty list define
#     # print( result.all());
#     for row in result.all():
#       # print(dict(row))
#       jobs.append(dict(row=row))   #putting each row data into dictionary than into list called jobs.
#     return jobs;







# # with engine.connect() as conn:
# #   result = conn.execute(text("select * from jobs")) # this is a sql quarry which will give a result
# #   print(result.all()) # result.all will display all the rows of above define quarry.type of result is class. type of result_all() is a list of python.
# # first_result_dict = dict(result.all[0]) # to convert list[0] into a dictionary


# # result_dicts =[]  # empty list define
# # for row in result.all():
# #   result_dicts.append(dict(row))   # putting each row data into dictionary than into list.

# # print (result_dicts)


