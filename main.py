import os

from flask import Flask,render_template
from flask import Blueprint
from api import api
import yaml
import argparse
from pymongo import MongoClient
from db import databases,db_mongodb
from config import global_config


app = Flask(__name__)


bp = Blueprint('api',__name__,url_prefix="/api/v1")

app.register_blueprint(api.bp)


def read_config_yaml(filename:str):
    try:
        with open(filename) as f:
            return yaml.safe_load(f)
    except:
        print("Unable to read file")


def init_db(db_host:str,db_port:str,db_type:str) -> object:
    if db_type == 'mongodb':
        CONNECTION_URI_STRING = db_mongodb.MongoNDB(db_host,db_port).conn_string

        client = MongoClient(CONNECTION_URI_STRING)

        return client


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    """
    Parse arguement
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-env",type=str,help="mention the environment")
    args = parser.parse_args()
    config = vars(args)

    environment = config['env']
    # print(environment)

    data = ''
    """
    Load config files for dev
    """
    if environment == 'dev':
        data = read_config_yaml(os.path.join(os.getcwd(),'env/namaskar.dev.yaml'))
        # print(data)
    print("Dev Config data is {0}".format(data))


    """
    Initializing the database
    """

    db_conn = init_db(data['database']['mongodb']['host'],
                      data['database']['mongodb']['port'],
                      'mongodb')

    # print(db_conn)

    db = db_conn[data['database']['mongodb']['db']]

    # print(db)

    mycol = db[data['database']['mongodb']['tweet_collection']]

    # print(mycol)

    global_config.db_conn = db_conn
    global_config.db = db
    global_config.mycol = mycol

    app.run(data['server']['host'],port=data['server']['port'],debug=True,threaded=True)
