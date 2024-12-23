# from textblob import TextBlob

# testimonial = TextBlob("The food was great!")
# print(testimonial.sentiment)

# from flair.models import TextClassifier
# from flair.data import Sentence

# classifier = TextClassifier.load('en-sentiment')
# sentence = Sentence('The food was great!')
# classifier.predict(sentence)

# # print sentence with predicted labels
# print('Sentence above is: ', sentence.labels)


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
sentence = "The food was great!"
vs = analyzer.polarity_scores(sentence)
print("{:-<65} {}".format(sentence, str(vs)))