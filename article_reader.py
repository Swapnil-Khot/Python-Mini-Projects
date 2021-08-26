from newspaper import Article
import pyttsx3

article = Article("https://myriadsofmiscellaneousthoughts.in/2021/05/15/the-art-of-sarcasm/")
article.download()
article.parse()

# print(article.title)
# print(article.text)

computer=pyttsx3.init()
rate = computer.getProperty('rate')
computer.setProperty('rate',150)
computer.say("Title : " + article.title)
computer.say("Article : "+ article.text)
computer.runAndWait()
computer.stop()
