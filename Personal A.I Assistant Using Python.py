# By The Neural Nut Bros. Pls don't forget to check our channel, The Neural Nut Bros.,.
#_______________________________________________________________ 
import pyttsx3 #For text to speech, command for installing it - 'pip install pyttsx3'
import speech_recognition as sr # For speech to text, command for installing it - 'pip install SpeechRecognition'
#Also install PyAudio, command for installing it - 'pip install pyaudio', but if it gives an error when you press enter after writing #this then write 'pip install pipwin' and then write 'pipwin install pyaudio' and hopefully it should be installed.
import wikipedia #So that we can unlock the capabilities of telling our personal assistant to search something on wikipedia.
import time
import datetime #to make it unlock the capabilities of telling the exact time, date. 
from webbrowser import open_new_tab #to make it unlock the capabilities of opening websites.
engine=pyttsx3.init('sapi5') # sapi5 is an API provided by microsoft.
voice=engine.getProperty('voices') # initializing the voices
engine.setProperty('voices',voice[0].id) #Setting the voice of my personal assistant, mine is David. 
myname="Jarvis"
times_not_ans=0  
now_time=datetime.datetime.now().strftime("%H:%M:%S") #stores the exact time in h:m:s(hrs, min, sec) format.
date_now=datetime.date.today() #stores the exact date in y:d:m(yr, date, month) format.
def say(text_data): #function to convert text to speech. It takes an argument which basically is a string or the text that has to be #converted into speech  
    engine.say(text_data) #says the text inside the parenthisis.
    engine.runAndWait() #stops until it says all the text, this is useful if u have written text on the next line, so if u dont write #this line it wont say the next line
def listen(): #this is to convert the speech to text. 
    global times_not_ans # declaring this variable as a global variable, now we can change it's contents.
    print("Listening...") # prints this to tell the the user that now he can start speaking. 
    r=sr.Recognizer()
    with sr.Microphone() as source: # declaring the input src which is the mic. Select ur mic otherwise it will give an error.
        audio=r.listen(source) #now it's gonna listen to our src.
        said=""
        try: # I have put a try except block so that listens to what we say, but if it is unable to listen to what the user is saying #it will print a msg instead of giving an error. that won't look good. 
            print("Recognizing...") # so that the user knows that his speech is being processed.
            said=r.recognize_google(audio)
            print(said) # it will print what u said.
            if "hello" in said: #if it finds the string "hello" in the text than its gonna introduce itself.
                print(f"Hi, i'm {myname}, your personal assistant, what can I do for u?") #using an 'f' string it prints and says its #name. using this method I created a simple chatbox.
                say(f"Hi, i'm {myname}, your personal assistant, what can I do for u?")
                listen()
            elif "who developed you" in said or "who were you developed by" in said:
                print("I was developed by my master Ishan, who is an enthusiast and a hobbyist.")
                say("I was developed by my master Ishan, who is an enthusiast and a hobbyist.")
                listen()
            elif "who is your favourite robot" in said:
                print("My favourite robot is R2D2 from star wars, transformers is also good but he ain't got that mojo")
                say("My favourite robot is R2D2 from star wars, transformers is also good but he ain't got that mojo")
                listen()
            elif "who is your favourite entrepreneur" in said:
                print("My favourite entrepreneur is Elon Musk")
                say("My favourite entrepreneur is Elon Musk")
                listen()
            elif "what's your favourite movie" in said or "what is your favourite movie" in said or "your favourite movie is" in said or "your favourite movie" in said:
                print("my favourite movie is I robot")
                say("my favourite movie is I robot")
                listen()
            elif "who is your favourite actor" in said or "your favourite actor is" in said or "your favourite actor" in said:
                print("My favourite actor is a Al Pacino")
                say("My favourite actor is a Al Pacino")
                listen()
            elif "what's your favourite song" in said or "what is your favourite song" in said or "your favourite song is" in said or "your favourite song" in said:
                print("My favourite song is The Robots from the Kraftwerk")
                say("My favourite song is The Robots from the Kraftwerk")
                listen()
            elif "who is your favourite rapper" in said or "your favourite rapper is" in said or "your favourite rapper" in said:
                print("My favourite rapper is Eminem, will the real slim shady please stand up, haha")
                say("My favourite rapper is Eminem, will the real slim shady please stand up, haha")
                listen()
            elif "which API did you use for speech recognition" in said:
                print("I used the Google API for my speech recognition technology")
                say("I used the Google API for my speech recognition technology")
                listen()
            elif "which API did you use for speaking" in said:
                print("I used the Sapi5 API from Microsoft, and my voice is David, please tell me to change my voice when you want me to, I will surely do it?")
                say("I used the Sapi5 API from Microsoft, and my voice is David, please tell me to change my voice when you want me to, I will surely do it?")
                listen()
            elif "your favourite game" in said or "what's your favourite game" in said or "what is your favourite game" in said:
                print("My favourite game is Tetris")
                say("My favourite game is Tetris")
                listen()            
            elif "what's your name" in said or "your name is" in said or "what is your name" in said:
                print("My name is {}".format(myname))
                say("My name is {}".format(myname))
                listen()
            elif "Wikipedia" in said: #if it finds wikipedia in said then:
                print("Okay, searching answers ...")
                say("Okay, searching answers...") 
                said=said.replace("wikipedia", "")
                results=wikipedia.summary(said, sentences=2) #finds the first 2 sentences about the results about what u asked and #stores it in a variable 
                say("According to Wikipedia")
                print(results)
                say(results)
                listen() #says the results and then listens.
            elif "what's the time" in said or "what is the time" in said:
                print(f"The time is {now_time}")# using an 'f' string says the time and then tells the time, and the same is with the #date
                say(f"The time is {now_time}")
                listen()
            elif "what's today's date" in said or "what is the date today" in said or "what is the date" in said or "what is today's date" in said or "what's the date" in said:
                print(f"Today is {date_now}")
                say(f"Today is {date_now}")
                listen()
            elif "open YouTube" in said: #Checks for the string in text.
                print("Okay, opening YouTube...")
                say("Okay, opening YouTube...") 
                open_new_tab("https://www.youtube.com/") #opens the website with the url inside the double quotes inside the #parenthesis. Same is for all the website, the only difference is that the url is different.  
            elif "open Amazon" in said:
                print("Okay, opening Amazon")
                say("Okay, opening Amazon")
                open_new_tab("https://www.amazon.com/")
            elif "open Google" in said:
                print("Okay, opening Google")
                say("Okay, opening Google")
                open_new_tab("https://www.google.com/")
            elif "open stack overflow" in said:
                print("Okay, opening stack overflow")
                say("Okay, opening stack overflow")
                open_new_tab("https://stackoverflow.com/")
            elif "open instructables" in said:
                print("Okay, opening instructables")
                say("Okay, opening instructables")
                open_new_tab("https://www.google.com/search?sxsrf=ALeKk010KURlOwfKChWyWOLdJBuPvIjmaQ%3A1600095782674&ei=JoZfX6PlKKXDpgfm5YqwCg&q=instructables+projects&oq=ins&gs_lcp=CgZwc3ktYWIQAxgBMgQIIxAnMgQIIxAnMgQIIxAnMgUIABCRAjILCAAQsQMQgwEQkQIyCAgAELEDEIMBMgQIABBDMgoIABCxAxCDARBDMgQIABBDMgQIABBDOgcIIxCwAhAnOgcIIxDqAhAnOgUIABCxA1D5H1iZNWDqSWgBcAB4BIABkQKIAZwMkgEFMC44LjGYAQCgAQGqAQdnd3Mtd2l6sAEKwAEB&sclient=psy-ab")
            elif "open my inbox" in said:
                print("Okay, opening your inbox")
                say("Okay, opening your inbox")
                open_new_tab("https://mail.google.com/mail/u/0/?ogbl#inbox")
            elif "open my gmail trash messages" in said or "open trash gmail in said" in said or "open trash emails" in said:
                print("Okay, opening messages in trash from your gmail")
                say("Okay, opening messages in trash from your gmail")
                open_new_tab("https://mail.google.com/mail/u/0/?ogbl#trash")
            elif "show my starred emails" in said or "open my starred emails" in said or "open starred emails" in said or "open starred messages" in said:
                print("Okay, opening your starred emails")
                say("Okay, opening your starred emails")
                open_new_tab("https://mail.google.com/mail/u/0/#starred")
            elif "open my snoozed emails" in said or "open snoozed emails" in said:
                print("Okay, opening your snoozed emails")
                say("Okay, opening your snoozed emails")
                open_new_tab("https://mail.google.com/mail/u/0/#snoozed")
            elif "open the emails the I've sent" in said or "open the emails the I have sent" in said or "show the emails the I've sent" in said or "show the emails the I have sent" in said or "open sent emails" in said:
                print("Okay, opening emails that you have sent")
                say("Okay, opening emails that you have sent")
                open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#sent")
            elif "open chats in my email" in said:
                print("Okay, opening the chats in your email")
                say("Okay, opening the chats in your email")
                open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#chats")
            elif "open scheduled emails" in said or "open emails that are scheduled" in said or "open the emails that are scheduled" in said or "open the scheduled emails" in said:
                print("Okay, opening the scheduled emails")
                say("Okay, opening the scheduled emails")
                open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#scheduled")
            elif "open all the mails" in said:
                print("Okay, opening all the mails")
                say("Okay, opening all the mails")
                open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#all")
            elif "open spam emails" in said or "open the emails that are in the spam section" in said:
                print("Okay, opening spam emails")
                say("Okay, opening spam emails")
                open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#spam")
            elif "open tinkercad circuits" in said:
                print("Okay, opening tinkercad circuits")
                say("Okay, opening tinkercad circuits")
                open_new_tab("https://www.tinkercad.com/dashboard?type=circuits&collection=designs")
            else:
                listen()
        except:
            print("Sorry, couldn't get that")
            say("Sorry, couldn't get that")
            times_not_ans+=1
            if times_not_ans<5:
                listen()
            else:
                time.sleep(0.02)
                print("You have not answered from a long time, seems like you don't need my help for the time being")
                say("You have not answered from a long time, seems like you don't need my help for the time being")
                listen()
    return said
listen()