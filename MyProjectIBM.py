import tweepy 
from textblob import TextBlob

#A twitter application is created from twitters website and u will get these credentials
consumer_key = "Here goes your consumer Key"
consumer_secret= "Here, consumer secret"
access_token= "xxxxxxx" 
access_token_secret= "xxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

#The tweets will be extracted from a user with a username

extractor = twitter_setup() 

#create a tweet list as follows: 
tweets = extractor.user_timeline(screen_name="username", count=200) 
print("Number of tweets extracted: {}.\n".format(len(tweets))) 

#print the most recent 5 tweets: 
print("5 recent tweets:\n") 
for tweet in tweets[:5]: 
   print(tweet.text,"\n")

#to correct any grammatical mistakes

blob = TextBlob(tweet.txt) 
blob.correct()
print(blob.sentences)

#Store the values in mood and publicm list
i=0
for sent in blob.sentences:
   mood[i]= sent.sentiment.polarity
   publicm[i]= sent.sentiment.subjectivity
   i+=1
     
"""Sentiment polarity ranges from [-1,1] and subjectivity from [0,1] &
   To find avg mood and how that tweet is based on public """

avgmood= sum(mood)/i
avgpublic= sum(publicm)/i

if(avgmood,avgpublic>0.5):
   print("Stay positive like this and spread Positivity")
elif(avgmood<0.5 and avgpublic>0.5):
   print("Do not stress up yourselves, Rules will change and so the world")
elif(avgmood>0.5 and avgpublic<0.5):
   print("Keep up with this sentiment")
elif(avgmood,avgpublic<0.5):
   print("Hey! you know you aren't the one with the problems, if you fear with these problems in ur life, what you will do in future?? think about family and well wishers of u, we all want u to be happy")
   print("Just take a nap while listening to it")
   print("https://youtu.be/7GSre2_s2uo")
else:
   print("Some error in evaluation")
   
#Thank you.. from Vikas Vishwakarma 3rd Sem I section 1726351

   
