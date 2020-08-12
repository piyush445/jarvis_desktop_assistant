import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[0].id)

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("piyush.nayan062@gmail.com","*************")
    server.sendmail("piyush.nayan062@gmail.com",to,content)
    server.close()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("good morning")

    elif hour>=12 and hour <=18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("i am jarvis sir, please tell me how may i help you")     

def takeCommand():
    #it takes microphone input from user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening.....")
        #  r.pause_threshold=1
         r.energy_threshold=50
         r.adjust_for_ambient_noise(source, duration=1)
         audio=r.listen(source)

    try:
        print("recognizing....")
        query= r.recognize_google(audio,language="en-US") 
        print(f"user said: {query} \n")
        
    
    except Exception as e:
        # print(e)
        print("say that again please")
        return "none"   
    return query  

if __name__=="__main__":
    wishMe()
    
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak(" Ok sir Searching wikipedia....")
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wipkipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            speak("ok sir")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("ok sir")
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            speak("ok sir")
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            speak("ok sir")
            music_dir= "D:\\songs\\favourite songs"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "time" in query:
            speak("ok sir")
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "open code" in query:
            speak("ok sir")
            codePath= "C:\\Users\\piyus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

        elif "send email"  in query:
            try:
                speak("what should i say sir")
                content=takeCommand()
                to= "pratyush.nayan@gmail.com"
                sendEmail(to,content)
                speak("email has been sent successfully, sir")

            except Exception as e:
                print(e)
                speak("sorry sir. i am not able to send this mail")





       