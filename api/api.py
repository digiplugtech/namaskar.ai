import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from config import global_config
from flask import request
bp = Blueprint('api', __name__, url_prefix='/api/v1')

@bp.route("/")
def get_all_tweets():
    return "This will add tweet"

@bp.route("/tweet",methods=['GET','POST'])
def post_tweet():
    if request.method == "POST":
        print("in add tweet");
        content_type = request.headers.get('Content-Type')
        print(content_type)
        tweet = request.json
        print(tweet)
        print(global_config.mycol.insert_one(tweet))
        return redirect(url_for('api.get_all_tweets'))
