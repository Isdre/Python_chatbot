import json
import pickle
import random

with open("responses.json","r",encoding='UTF-8') as f:
    responses = json.load(f)

with open("chatbot.pkl","rb") as f:
    vectorizer, brain = pickle.load(f)

# brain = joblib.load('chatbot.joblib')

# test = vectorizer.transform(["cześć"])
# print(test)
# w = brain.predict(test)
# print(w)

def response_me(message):
    # print("answering")
    m = vectorizer.transform(message)
    tag = brain.predict(m)[0]
    # print(responses[tag])
    return random.sample(responses[tag],1)
