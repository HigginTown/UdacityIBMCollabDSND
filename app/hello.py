"""
Recommendation System Flask APP for Udacity Collaboration


Spark ALS Version

"""

from flask import Flask, render_template, request, jsonify
import atexit
import cf_deployment_tracker
import os
import json
import requests

# additional imports from us
from watson_machine_learning_client import WatsonMachineLearningAPIClient 
import operator
from creds import wml_credentials, user_map_articles, article_map, user_map_collabs, collab_name_map

# start the app
app = Flask(__name__)

client = None

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))


@app.route('/')
def home():
    return render_template('index.html')


    
@app.route('/api/visitors', methods=['POST'])
def put_visitor():
    """Gets the top recommendations for a given user
    """
    # catch invalid usernames and recommend random articles if invalic
    try:
        # connect to the client
        print("Attempting to connect...")
        wml_client = WatsonMachineLearningAPIClient(wml_credentials)

        # debugging
        # print(wml_credentials)
        # Get the article scores for every user, sort them, and serve them

        # fetch the username 
        user = request.json['name']
        user_id = user_map_articles[user]


        # get the keys for all the article ids
        all_articles = list(article_map.keys())

        # create a request
        input_json = {
        'fields': ["indexed_email", "article_id"],
        'values': [[user_id,float(article_id)] for article_id in all_articles]} # list comprehension points to all articles

        # score
        predictions = client.deployments.score(scoring_url, input_json)

        # we are only interested in the prediction and article_id
        vals = [(p[1], p[-1]) for p in predictions['values']]

        # sort the tuples
        vals.sort(key=operator.itemgetter(1))

        # return the titles
        titles = [article_map[v[0]] for v in vals[-5:]]

        # pretty print
        ret = (''.join(["{}. {} \n".format(i+1, t) for i,t in enumerate(titles)]))
        return ret

    except:
        # return random ones now 
        # Student TODO students can change to most popular
        import random
        article_titles = list(article_map.values())
        random.shuffle(article_titles)
        titles = article_titles[:5]
        ret = (''.join(["{}. {} \n".format(i+1, t) for i,t in enumerate(titles)]))
        return ret

            
@app.route('/api/collaborators', methods=['POST'])
def get_collaborators():
    """
    Get the collaborator scores for every user, sort them, and serve them
    """
    try:
        # test with all collabs being only a few fields
        user = request.json['name']
        # user_id = user_map[user]
        user_id = 24
        
        all_collabs = [884, 5881, 218, 8081, 7997]

        # create a request
        input_json = {
        'fields': ["user_indexed", "collaborator_indexed"],
        'values': [[user_id,float(collab)] for collab in all_collabs]}


        # scoring url taken from wml
        scoring_url = "https://ibm-watson-ml.mybluemix.net/v3/wml_instances/8d680d1b-4091-4be7-9023-05d551059662/published_models/63ec3440-d837-44ac-8c23-b6e9b2415dc5/deployments/31793705-ed46-422d-9607-df01d4aeb66d/online"

        # score
        predictions = client.deployments.score(scoring_url, input_json)

        # we are only interested in the prediction and article_id
        vals = [(p[1], p[-1]) for p in predictions['values']]

        # sort the tuples
        vals.sort(key=operator.itemgetter(1))

        return list(reversed(vals[-5:]))
    except:
        return "User not found"


if __name__ == '__main__':
    # set debugger to `False` when deploying to Cloud
    app.run(host='0.0.0.0', port=port, debug=True)
