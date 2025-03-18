from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Stranger! I hope you had a good day today. How are you feeling today?")
engine.runAndWait()

print("What's your mood today?")
phrase = input(">>>")
blob = TextBlob(phrase)

while blob.sentiment.polarity < 0.3:
   engine.say("Oh no! Please try to be more positive!")
   engine.runAndWait()
   phrase = input(">>>")
   blob = TextBlob(phrase)
print("Great! You can leave now. ")
engine.say("Way to go! Keep it up!")
engine.runAndWait()

