import io
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

warnings.filterwarnings('ignore')

# Reading in the corpus
with open('chatbot.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

# Tokenization
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# Preprocessing
lemmer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "how are you")
GREETING_RESPONSES = ["hello!", "hi!", "hey!", "hi there!", "hello! how can i help you?", "hi! what can i do for you?"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generating response
def response(user_response):
    infinibot_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        infinibot_response = "I am sorry! I don't understand you."
    else:
        infinibot_response = sent_tokens[idx]
    sent_tokens.pop(-1)
    return infinibot_response

# Chatbot Interaction
flag = True
print("INFINIBOT: My name is Infinibot. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while flag:
    user_response = input().lower()
    if user_response != 'bye':
        if user_response in ['thanks', 'thank you']:
            flag = False
            print("INFINIBOT: You are welcome.")
        else:
            if greeting(user_response) is not None:
                print("INFINIBOT: " + greeting(user_response))
            else:
                print("INFINIBOT: " + response(user_response))
    else:
        flag = False
        print("INFINIBOT: Bye! Take care.")
