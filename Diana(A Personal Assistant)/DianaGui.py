from tkinter import *
import pyttsx3
import speech_recognition as sr
import datetime
import os
from cv2 import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes
import pyautogui
import requests
import json
import instaloader
import PyPDF2
from tkinter import simpledialog
import operator
import wolframalpha
from PIL import ImageTk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


window = Tk()
global var
global var1

var = StringVar()
var1 = StringVar()

class wolfram():
    try:
        app = wolframalpha.Client("L6RG9Q-9W8EW4VA64")
    except Exception:
        print("some features are not working")

# text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# convert voice to text
def takeOrder():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        var.set("Listening....")
        window.update()
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        var.set("Recognizing....")
        window.update()
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception:
        return "none"
    var1.set(query)
    window.update()
    return query


# wish me
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        var.set("Good Morning shivam ,  its " + tt)
        window.update()
        speak(f"Good Morning ,shivam ,  its {tt}")
    elif hour >= 12 and hour < 18:
        var.set("Good Afternoon shivam ,  its " + tt)
        window.update()
        speak(f"Good Afternoon ,shivam , its {tt}")
    else:
        var.set("Good Evening shivam its " + tt)
        window.update()
        speak(f"Good Evening ,shivam, its {tt}")
    var.set("I Am diana ,  Sir How May I Help You")
    window.update()
    speak("I Am diana ,  Sir How May I Help You")


def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&category=&apiKey=761708ff92ac420f8ff8f08452313faf'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        var.set("today's "+day[i]+"news is:"+head[i])
        window.update()
        speak(f"today's {day[i]} news is: {head[i]} ")


def pdf_reader():
    book = open('C:/Users/SHIVAM JHA/Desktop/rapoapp/python.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book are {pages}")
    var.set("sir , what the page number i have to read")
    window.update()
    speak("sir , what the page number i have to read")
    pg = int(takeOrder().lower())
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def Run():
    btn0['state'] = 'disabled'
    btn1.configure(bg='orange')
    wish()
    while True:
        btn1.configure(bg='orange')
        query = takeOrder().lower()

        # logic building for task
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            var.set(" I opened notepad for you , sir")
            window.update()
            speak(" I opened notepad for you , sir")

        elif "close notepad" in query:
            var.set(" okay sir , i am closing notepad")
            window.update()
            speak("okay sir , i am closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open wordpad" in query:
            wpath = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wpath)
            var.set(" I opened wordpad for you , sir")
            window.update()
            speak(" I opened wordpad for you , sir")

        elif "close wordpad" in query:
            var.set(" okay sir , i am closing wordpad")
            window.update()
            speak("okay sir , i am closing wordpad")
            os.system("taskkill /f /im wordpad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")
            var.set(" I opened command prompt for you , sir")
            window.update()
            speak(" I opened command prompt for you , sir")

        elif "close command prompt" in query:
            var.set("okay sir , i am closing command prompt")
            window.update()
            speak("okay sir , i am closing command prompt")
            os.system("taskkill /f /im cmd.exe")  # cmd closing close vscode terminal also

        elif 'click photo' in query:
            try:
                stream = cv2.VideoCapture(0)
                grabbed, frame = stream.read()
                if grabbed:
                    cv2.imshow('pic', frame)
                    cv2.imwrite('pic.jpg',frame)
                    stream.release()
            except Exception:
                var.set("your default camera is already open on another software . so , i am unable to click photo ")
                window.update()
                speak("your default camera is already open on another software . so , i am unable to click photo ")
                pass

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            var.set("sir , your IP Address is "+ip)
            window.update()
            speak(f"sir , your IP Address is {ip}")

        elif "wikipedia" in query:
            var.set("searching wikipedia....")
            window.update()
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            var.set(results)
            window.update()
            speak(results)
            # print(results)

        elif "play music" in query:
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = "E:\\shiv"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            time.sleep(5)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            speak(" I am opening youtube for you , sir")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")
            speak(" I am opening facebook for you , sir")

        elif "open google" in query:
            var.set("what should i search on google , sir")
            window.update()
            speak("what should i search on google , sir")
            comm = takeOrder().lower()
            webbrowser.open(f"{comm}")
            speak("searching on google , sir")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            speak(" I am opening stackoverflow for you , sir")


        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("sir , it's "+strTime)
            window.update()
            speak(f"sir , it's {strTime}")

        # watsapp message code
        elif "message" in query:
            try:
                driver=webdriver.Chrome()
                driver.get("https://web.whatsapp.com/")
                speak ("please scan qr code")
                time.sleep(15)
                speak("whom do you want to sent message ?")
                name = takeOrder().lower()
                fal = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                fal.click()
                speak("what is the message you wanna sent ? , sir ")
                message = takeOrder().lower()
                myinput = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
                myinput.send_keys(message)
                myinput.send_keys(Keys.RETURN)
                time.sleep(7)
                speak("your message has been sent")
            except Exception :
                var.set("Sorry , i am not able to get that person , you must try again ")
                window.update()
                speak("Sorry , i am not able to get that person , you must try again ")

        elif " on youtube" in query:
            var.set("what should i search on youtube , sir")
            window.update()
            speak("what should i search on youtube , sir")
            command = takeOrder().lower()
            kit.playonyt(f"{command}")
            speak("searching on youtube , sir")
            time.sleep(8)

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke(language="en", category="all")
            var.set(joke)
            window.update()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t s")

        elif "restart the system" in query:
            os.system("shutdown /r /t s")

        elif "sleep mode in the system" in query:
            os.system("rund1132.exe powrprof.dil.SetSuspendState 0,1,0")  # not working

        elif "sleep" in query:
            var.set("i am going to sleep , sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("i am going to sleep , sir")
            break

        elif " window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            time.sleep(2)

        elif "where we are" in query:
            var.set("wait sir , let me check")
            window.update()
            speak("wait sir , let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = "http://api.ipstack.com/157.42.138.27?access_key=968e4d5d446e357863f0567bb6f43a1" #put appropriate key to work well
                geo_req = requests.get(url)
                geo_json = json.loads(geo_req.text)
                region = geo_json['region_name']
                country = geo_json['country_name']
                city = geo_json['city']
                var.set("sir i am not sure , but i think we are in "+city+" city of "+region+" region of "+country)
                window.update()
                speak(f"sir i am not sure , but i think we are in {city} city of {region} region of {country}")
            except Exception as e:
                var.set("sorry sir , due to network issue  , i am not able to find where we are")
                window.update()
                speak("sorry sir , due to network issue  , i am not able to find where we are")
                pass

        elif "instagram profile" in query:
            var.set("sir , please enter the user name correctly")
            window.update()
            speak("sir , please enter the user name correctly")
            name = simpledialog.askstring("input value", "ENTER THE USERNAME")
            webbrowser.open(f"www.instagram.com/{name}")
            time.sleep(10)
            var.set("sir would you like to download profile picture of this account?")
            window.update()
            speak("sir would you like to download profile picture of this account?")
            condition = takeOrder().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                var.set("i am done sir , profile picture is saved in your main folder")
                window.update()
                speak("i am done sir , profile picture is saved in your main folder")
            else:
                pass

        elif "screenshot" in query:
            var.set("sir , please let me know the file name of this screenshot file")
            window.update()
            speak("sir , please let me know the file name of this screenshot file")
            file_name = takeOrder().lower()
            var.set("please sir , hold the screen for few seconds , i am taking screenshot")
            window.update()
            speak("please sir , hold the screen for few seconds , i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{file_name}.png")
            var.set("i am done sir , the screenshot is saved in our main folder")
            window.update()
            speak("i am done sir , the screenshot is saved in our main folder")

        elif "calculation" in query:
            r = sr.Recognizer()

            with sr.Microphone() as source:
                var.set("What You Want To Calculate , Sir?")
                window.update()
                speak("What You Want To Calculate , Sir?")
                var.set("Listening....")
                window.update()
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            var.set(my_string)
            window.update()
            def get_operator_fn(op):
                return {
                    '+': operator.add, #plus
                    '-': operator.sub,  # minus
                    'x': operator.mul,  # multiplied by
                    'divided': operator.__truediv__,  # divided
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1,op2)
            var.set(eval_binary_expr(*(my_string.split())))
            window.update()
            speak("your result is ")
            speak(eval_binary_expr(*(my_string.split())))

        elif "read pdf" in query:
            pdf_reader()

        elif "tell me news" in query:
            var.set("please have patience , sir , i am fetching the latest news for you ")
            window.update()
            speak("please have patience , sir , i am fetching the latest news for you ")
            news()
            
        elif "terminate yourself" in query:
            var.set("thankyou for giving me opportunity to work for you , have a nice day sir")
            window.update()
            speak("thankyou for giving me opportunity to work for you , have a nice day sir")
            sys.exit()
        
        else:
            try:
                    res = wolfram.app.query(query)
                    var.set(next(res.results).text)
                    window.update()
                    speak(next(res.results).text)
            except Exception:
                speak("sorry , i didn't understand what you say   ")
                    
        speak("sir , waiting for your another command ")
    



    if __name__=="__main__":
        while True:
            permission = takeOrder().lower()
            if "wake up" in permission:
                Run()
            else:
                pass
            
            
                
            

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('DIANA')
window['bg']='#08a66c'

# set window icon
img = ImageTk.PhotoImage(file='vlogo.png')
window.wm_iconphoto(True, img)

label = Label(window, width = 1280, height = 840, bg='#08a66c')
label.pack()
window.after(0, update, 0)
window.resizable(False,False)

btn0 = Button(text = 'WISH ME',width = 20, command = wish, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'RUN',width = 20,command = Run, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()

