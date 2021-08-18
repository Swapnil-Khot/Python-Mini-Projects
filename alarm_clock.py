import datetime
import pyttsx3

date=pyttsx3.init()
currTime=datetime.datetime.now()
current=currTime.strftime("%I")+":"+currTime.strftime("%M")+":"+currTime.strftime("%S")+" "+currTime.strftime("%p")

print("Current Time : ",current)
print("It is 12 hour Clock\nTo set alarm enter the details")
while True:
    hour=input("Hours : ")
    minutes=input("Minutes : ")
    seconds=input("Seconds : ")
    period=input("Enter AM or PM : ").upper()

    if int(hour)<=12 and int(hour)>=1:
        if int(minutes)<=59 and int(minutes)>=00:
            if int(seconds)<=59 and int(seconds)>=00 :
                if period == "AM" or period=="PM":
                    break
                else:
                    print("\nSomething went WRONG : Period should be in AM or PM \n")
            else:
                print("\nSomething went WRONG : Seconds should be in range of 0 to 59\n")
        else:
            print("\nSomething went WRONG : Minutes should be in range of 0 to 59\n")
    else:
        print("\nSomething went WRONG : Hours should be in range of 1 to 12\n")


while True:
    currTime = datetime.datetime.now()
    currentHour = currTime.strftime("%I")
    currentMinute = currTime.strftime("%M")
    currentSecond = currTime.strftime("%S")
    currentPeriod = currTime.strftime("%p")
    if currentHour == hour and currentMinute == minutes and currentSecond == seconds and currentPeriod ==period:
        rate = date.getProperty('rate')
        date.setProperty('rate',150)
        date.say("Its the time to wake up")
        date.runAndWait()
        break
