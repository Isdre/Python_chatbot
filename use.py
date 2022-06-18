import json
import pickle
import sklearn
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

with open("responses.json","r",encoding='UTF-8') as f:
    response = json.load(f)

with open("chatbot.pkl","rb") as f:
    brain = pickle.load(f)

test = brain.predict(vectorizer.transform(["cześć"]))
print(test)