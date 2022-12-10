import datetime # library for date and time
from pytz import timezone # to select timezone of INDIA (or any other country)
import smtplib # library used to send mails
from email.message import EmailMessage 
#import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
#import pywhatkit
import requests
from newsapi import NewsApiClient
import pyjokes
import string 
import random
import psutil
import nltk
import numpy as np

#Punkt Tokenizer
nltk.download('punkt')
#WordNet Dictionary
nltk.download('wordnet') 
nltk.download('omw-1.4')

lemmer=nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def time():
  Time = datetime.datetime.now(timezone('Asia/Calcutta')).strftime("%H:%M:%S") # H-> Hour, M-> Minutes, S-> Seconds
  ans = ("The current time is : " + Time)
  return ans

def day():
  Day = datetime.datetime.now().strftime("%A")
  ans = ("The current day is : " + Day)
  return ans

def date():
  Year = int(datetime.datetime.now().year)
  Month = int(datetime.datetime.now().month)
  Date = int(datetime.datetime.now().day)
  ans = ("The current date is : " + str(Date) + " " + str(Month) + " " + str(Year))
  return ans


def wishme():
    hour = datetime.datetime.now(timezone('Asia/Calcutta')).hour
    if hour >= 6 and hour < 12:
        ans=("Good morning!")
    elif hour >= 12 and hour < 18:
        ans=("Good afternoon!")
    elif hour >= 18 and hour < 24:
        ans=("Good evening!")
    else:
        ans=("Good night!")
    return ans

def takeInput():
  var = input("\nPlease tell me how can i help you? : ")
  return str(var)

# need to pass two parameters ("content", "to") as function variables
def sendEmail(receiver, subject, content):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls() #tls -> transport layer security(used to make email secure)
  server.login("efahi56189@gmail.com", "56189efahi") #sender mail and mail id password required
  email = EmailMessage()
  email['From'] = "efahi56189@gmail.com"
  email['To'] = receiver
  email['Subject'] = subject
  email.set_content(content)
  server.send_message(email)
  server.close() 

  # enable less secure apps in gmail account to run this function

def sendWhatsMsg(phone_no, message):
  Message = message
  wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
  sleep(10)
  # puautogui.press('enter')

def searchGoogle(query):
  wb.open('https://www.google.com/search?q='+query)

def news():
  newsapi = NewsApiClient(api_key = '99ccfefa3dfe4abc824d337eaa9e4a8a')
  topic = request.args.get('topic')
  data = newsapi.get_top_headlines(q=topic, language='en', page_size=5)
  newsdata = data['articles']
  newlist = [("Latest news updates about the topic " + topic + " are : ")]
  for x,y in enumerate(newsdata):
    newlist.append(f'{x}{y["description"]}')
  return newlist 

def passwordGen():
  s1 = string.ascii_uppercase
  s2 = string.ascii_lowercase
  s3 = string.digits
  s4 = string.punctuation

  passlength = 10
  s = []
  s.extend(list(s1))
  s.extend(list(s2))
  s.extend(list(s3))
  s.extend(list(s4))
  random.shuffle(s)

  newpass = ("".join(s[0:passlength]))
  ans = ("The generated password is : " + newpass)
  return ans

def flip():
  coin = ['head', 'tail']
  toss = []
  toss.extend(coin)
  random.shuffle(toss)
  toss = ("".join(toss[0]))
  ans = ("output of flipped coin is a "+toss)
  return ans

def roll():
  die = ['1', '2', '3', '4', '5', '6']
  roll = []
  roll.extend(die)
  random.shuffle(roll)
  roll = ("".join(roll[0]))
  ans = ("output of the die rolled is "+roll)
  return ans

def cpu():
  usage = str(psutil.cpu_percent())
  ans = ("CPU is at "+ usage)
  return ans

def bot(msg):
  wishme()
  GREET_INPUTS = ("hello", "hi", "greetings", "sup", "whatsup", "hey", "how", "namaste", "how")
  GREET_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me", "hello! How are you?", "*nods*", "hi! How are you?"]
  while True:
    inp = msg.lower()
    query = LemNormalize(inp)
    flag = True
    List = []
    # operations 
    if 'quit' in query:
      break

    if 'time' in query:
      flag = False
      List.append(time())

    if 'day' in query:
      flag = False
      List.append(day())

    if 'date' in query:
      flag = False
      List.append(date())

    if 'email' in query:
      flag = False
      try:
        receiver = request.args.get('receiver')
        subject = request.args.get('subject')
        content = request.args.get('content')
        sendEmail(receiver, subject, content)
        return("email has been sent")
      except Exception as e:
        return("404")
      continue

    if 'message' in query:
      flag = False
      user_name = {
          'vivek' : '+91 94623 28117'
      }
      try:
        receiver = input("Please enter receiver's name : ")
        name = receiver.lower()
        phone_no = user_name[name]
        message = input("Please enter content of the msg : ")
        sendWhatsMsg(phone_no, message)
        print("message has been sent")
      except Exception as e:
        print(e)
      continue

    if 'wikipedia' in query:
      flag = False
      inp = inp.replace("wikipedia", "")
      result = wikipedia.summary(inp, sentences = 3)
      List.append("The search result is : " + result)

    if 'google' in query:
      flag = False
      inp = inp.replace("google", "")
      result = wikipedia.summary(inp, sentences = 2)
      List.append("The search result is : " + result)

    if 'weather' in query:
      flag = False
      city = request.args.get('city')
      url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=24a0a5534a7ced33763b94acb9e7d058'

      res = requests.get(url)
      data = res.json()

      weather = data['weather'] [0] ['main']
      temp = data['main']['temp']
      temp = round((temp - 32)*5/9)
      desp = data['weather'] [0] ['description']
      List.append("The current weather is : " + weather)
      List.append("The current temperature is : " + str(temp))

    if 'news' in query:
      flag = False
      List.append(news())

    if 'joke' in query:
      flag = False
      List.append("here is the joke : " + pyjokes.get_joke())

    if 'password' in query:
      flag = False
      List.append(passwordGen())

    if 'flip' in query:
      flag = False
      List.append(flip())

    if 'roll' in query:
      flag = False
      List.append(roll())

    if 'cpu' in query:
      flag = False
      List.append(cpu())

    if flag:
      for word in query:
        if word in GREET_INPUTS:
          return (random.choice(GREET_RESPONSES))
    else:
      return (List)

    if flag:
      return ("Didn't understand what you are trying to say, please try again!")

from flask import Flask, request,jsonify

import numpy as np


app= Flask(__name__)

@app.route('/')
def home():
    return "Welcome to ChatBot"

@app.route('/bot', methods=['POST'])
def get_bot_response():
    userText = request.args.get('msg')
    
    result=bot(userText)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",)

