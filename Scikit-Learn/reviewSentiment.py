# Problem Statement -> Using Naive Bayes (work on textual data(data in text formate))
'''A company is looking to develop a text classification model to categorize customer reviews into positive and
negative sentiments. They want to use Naive Bayes Classification to automatically analyze and classify the
reviews they receive, aiming to understand customer satisfaction levels and rentiments. The company desires
a model that can accurately predict whether a customer review expresses a positive or negative sentiment.'''

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

reviews = ["The product the very good", 
           "Its working is excellent",
           "Terrible customer service",
           "I absolutely love this product",
           "My order arrived two weeks late, and the packaging was damaged",
           "The product quality is poor and cheap"]
sentiments = np.array([1,1,0,1,0,0]) # 0 is negative and 1 is positive reviews

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

classifier = MultinomialNB()
classifier.fit(X, sentiments)

def classify_user_review(user_review):
    user_review_vertorizer = vectorizer.transform([user_review])
    prediction = classifier.predict(user_review_vertorizer)
    if prediction[0] == 1:
        return "Positive Sentiment!"
    else:
        return "Negative Sentiment!"

print()
user_review = input("Enter the customer review: ")
result = classify_user_review(user_review)

print()
print(f"The customer review '{user_review}' is classified as '{result}'")
print()
