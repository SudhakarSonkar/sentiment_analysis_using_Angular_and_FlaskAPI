import json
from typing import OrderedDict
import requests
from re import T
from flask import Flask
from flask import request
from textblob import TextBlob
from flask_cors import  CORS, cross_origin

app= Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': 'http://localhost:4200/'}})

def review(data):
    feedback=data
    print(feedback)
    blob=TextBlob(feedback['text'])
    list=[]
    list.append(blob.sentiment)
    return list


def formatoutput(score):
    if score[0][0] > 0:
        output = OrderedDict({
            "total_review":1,
            "positive_review":1,
            "negative_review":0,
            "neutral_review":0,
            "result":"Positive"
            })
    elif score[0][0] < 0:
        output=OrderedDict({
            "total_review":1,
            "positive_review":0,
            "negative_review":1,
            "neutral_review":0,
            "result":"Negative"
        })
    else:
        output=OrderedDict({
            "total_review":1,
            "positive_review":0,
            "negative_review":0,
            "neutral_review":1,
            "result":"Neutral"
        })

    return output



@app.route('/sentiment',methods=['POST'])
@cross_origin(origins=['http://localhost:4200'])
def get():
        data = request.get_json()
        score=review(data)
        result=formatoutput(score)
        return result

if __name__ == "__main__":
    app.run(debug = True)