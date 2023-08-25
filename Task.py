
import datetime
import webbrowser
import os
from Speak import Say
from Listen import Listen

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say("the current time is ")
    Say(time)
    
def Date():
    date  = datetime.date.today()
    Say(date)

def introduce():
    Say("allow me to introduce myself ")
    Say("I am JARVIS a virtual artificial intelligence")
    Say("created by Joel")
    Say("I am here to assist you  with variety of task since the best as I can 24 hours a day and 7 days a week")
    Say("how can I help you sir")

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)
    Date()

def Drive():
     Say("ok sir, opening your google drive")
     webbrowser.open('https://drive.google.com/drive/my-drive')
     Say("opened your personel drive in the browser")


def Github():
     Say("ok sir, opening your Git hub account")
     webbrowser.open('https://github.com/joeljcodes')
     Say("opened your git hub account in the browser")

def College():
     Say("ok sir, opening your moodle account")
     webbrowser.open('http://117.221.21.2:1025/')
     Say("please enter the user name and password for login")

def whatsap():
     Say("ok sir, opening whatsap web in the browser")
     webbrowser.open('https://web.whatsapp.com/')
     Say("done sir")

def exit():
      Say('closing the currently opened window ')
      browserExe = "msedge.exe"
      os. system("taskkill /f /im "+browserExe)
      Say("done sir")

def music():
    Say('ok sir opening spotify on the web browser')
    webbrowser.open('https://open.spotify.com/')
    Say('done sir')

def climate():
    Say("ok sir, opening the climate pictorial representation")
    webbrowser.open('https://www.msn.com/en-us/weather/forecast/in-Kanayannur,KL?loc=eyJsIjoiS2FuYXlhbm51ciIsInIiOiJLTCIsImMiOiJJbmRpYSIsImkiOiJJTiIsImciOiJlbi11cyIsIngiOiI3Ni4yOTQiLCJ5IjoiMTAuMDA1In0%3D&ocid=ansmsnweather&weadegreetype=F')    
    Say("Expect partly sunny skies.")
    Say("wind speed is 3 mhp, Humidity is 56 percentage,overall climate is partly sunny")
    Say("stay hydrated")

def instagram():
    Say("ok sir opening your instagram account in the browser")
    webbrowser.open("https://www.instagram.com/")
    Say("done sir")

def calender():
    Say("opening your google calender")
    webbrowser.open('https://calendar.google.com/calendar/u/0/r?pli=1')
    Say("done sir")


    
def NonInputExecution(query):

    query = str(query)
    
    if "time" in query:
        Time()
        
    elif "climate" in query:
        climate()
        
    elif "date" in query:
        Date()
        
    elif "day" in query:
        Day()
    
    elif "music" in query:
        music()
    
    elif "climate" in query:
        climate()
        
    elif "drive" in query:
        Drive()
    
    elif "git" in query:
        Github()
    
    elif "college" in query:
        College()
    
    elif "whatsap" in query:
        whatsap()
    
    elif "exit" in query:
        exit()
    
    elif "instagram" in query:
        instagram()
    
    elif "introduce" in query:
        introduce()
    
    elif 'calender' in query:
        calender()
    
  
    
    elif "quit" in query:
        Say("I am turning to the offline mode sir ")
        Say("you can call me when ever you want")
        Say("Have a nice day sir!")
        quit()
    
    
def InputExecution(tag,query):
    
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("what is","")
        import wikipedia
        result = wikipedia.summary(name,2)
        Say(result)
    

   
        
    
        
