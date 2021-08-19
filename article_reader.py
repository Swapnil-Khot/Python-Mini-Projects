from newspaper import Article
import pyttsx3

article = Article("https://arunachaltimes.in/index.php/2021/08/11/nes-gives-away-academic-excellence-awards-scholarships/")
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