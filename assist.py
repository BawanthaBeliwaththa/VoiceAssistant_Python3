# I Made This For Linux Users.

import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
from urllib.request import urlopen

engine = pyttsx3.init('espeak') #windows users "sapi5", mac users "".
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id) #you can use any voice id

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good")
		speak("Morning")
		speak("Sir")

	elif hour>= 12 and hour<18:
		speak("Good")
		speak("Afternoon")
		speak("Sir")

	else:
		speak("Good")
		speak("Evening")
		speak("Sir")

	assname =("jarvis") #asssistant name
	speak("I")
	speak("Am")
	speak("Your")
	speak("Assistant")
	speak("mister")
	speak(assname)

def usrname():
		speak("What")
		speak("should")
		speak("I")
		speak("call")
		speak("you")
		speak("Sir")
		uname = takeCommand() #User/Your name
		speak(uname)
		columns = shutil.get_terminal_size().columns
	
		print("#####################".center(columns))
		print("Welcome", uname.center(columns))
		print("mister", uname.center(columns))
		print((uname), uname.center(columns))
		print("#####################".center(columns))
	
		speak("How")
		speak("Can")
		speak("I")
		speak("Help")
		speak("You")
		speak("Sir")
def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-us')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query


if __name__ == '__main__':
	clear = lambda: os.system('cls')
	

	clear()
	wishMe()
	usrname()
	
	while True:
		
		query = takeCommand().lower()
		

		if 'hay' in query:
			speak ("hello")

		elif 'wish' in query:
			hour = int(datetime.datetime.now().hour)
			if hour>= 0 and hour<12:
				speak("Good")
				speak("Morning")
				speak("Sir")

			elif hour>= 12 and hour<18:
				speak("Good")
				speak("Afternoon")
				speak("Sir")

			else:
				speak("Good")
				speak("Evening")
				speak("Sir")

		elif 'stop' in query:
			speak('Okay')
			speak('bye')
			exit()

		elif 'youtube' in query:
			speak("Here it's Youtube\n")
			webbrowser.open("youtube.com")

		elif 'yahoo' in query:
			speak("Here it's yahoo\n")
			webbrowser.open("yahoo.com")

		elif 'my page' in query:
			speak("Here you go\n")
			webbrowser.open("https://weareligeion.wordpress.com/")

		elif 'google' in query:
			speak("Here it's Google\n")
			webbrowser.open("google.com")

		elif 'github' in query:
			speak("Here you go to Git Hub. Happy coding")
			webbrowser.open("github.com")

		elif 'music' in query or "song" in query:
			speak("Here")
			speak("You")
			speak("go")
			speak("with")
			speak("music")
			music_dir = "/home/bawantha/Music/"
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[1]))

		elif 'time' in query:
			strTime = datetime.datetime.now().strftime("% H:% M:%")
			speak("Sir")
			speak("the")
			speak("time")
			speak("is")
			speak(f"{strTime}")


		elif 'how are you' in query:
			speak("I")
			speak("am")
			speak("okay")
			speak("sir")
			speak("and")
			speak("How")
			speak("about")
			speak("You")
			speak("sir")

		elif 'fine' in query or "good" in query:
			speak("That")
			speak("is")
			speak("good")
			speak("to")
			speak("know")


		elif "your name" in query or "What is your name" in query:
			speak("My")
			speak("friends")
			speak("call")
			speak("Me")
			speak('Achintha')
			print("My friends call me", 'Achintha')

		elif 'exit' in query:
			speak("Thanks")
			speak("for")
			speak("giving")
			speak("me")
			speak("your")
			speak("Time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I")
			speak("have")
			speak("been")
			speak("created")
			speak("by")
			speak("Bawantha")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If")
			speak("You")
			speak("Talk")
			speak("Then")
			speak("You")
			speak("Are")
			speak("A")
			speak("Human")


		elif "why you came to world" in query:
			speak("Thanks")
			speak("To")
			speak("Bawantha")
			speak("and")
			speak("It")
			speak("is")
			speak("a")
			speak("secret")


		elif 'is love' in query:
			speak("It")
			speak("is") 
			speak("7th") 
			speak("sense")
			speak("that")
			speak("destroy")
			speak("all")
			speak("other")
			speak("senses")

		elif "who are you" in query:
			speak("I")
			speak("am")
			speak("Your")
			speak("Virtual")
			speak("Assistant")
			speak("created")
			speak("by")
			speak("Bawantha")

		elif 'reason for you' in query:
			speak("I")
			speak("Think")
			speak("it's")
			speak("for")
			speak("fun")


		elif 'news' in query:
			speak("Your")
			speak("News")
			speak("tab")
			speak("is")
			speak("opened")
			speak("in")
			speak("Your")
			speak("browser")
			webbrowser.open("https://www.dailymirror.lk") #for news I used this




		elif "don't listen" in query or "stop listening" in query:
			speak("how")
			speak("many")
			speak("times")
			speak("sir")
			a = int(takeCommand())
			time.sleeps(a)
			print(a)

		elif "where I am" in query:
			query = query.replace("where is", "")
			location = query
			speak("User")
			speak("asked")
			speak("to")
			speak("locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")


		elif "new note" in query:
			speak("What")
			speak("Should")
			speak("I")
			speak("Write")
			speak("Sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir")
			speak("should")
			speak("I")
			speak("include")
			speak("Date")
			speak("And")
			speak("Time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing")
			speak("Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read(6))


		elif "weather" in query:
#credits @https://openweathermap.org/			                                   
#kandy is a town that having a weather station (:-)
                                            
			api_key = "232013a11f35be8b9d01a206abbb3a26"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak("Kandy") 
			print("Kandy : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()
			
			if x["cod"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
			else:
				speak(" City Not Found ")

		elif "wiki" in query:
			speak("Watch")
			speak("at")
			speak("your")
			speak("webbrowser")
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How")
			speak("are")
			speak("you")
			speak("Sir")
		elif 'fine' in query or "good" in query:
			speak("That")
			speak("is")
			speak("good")
			speak("to")
			speak("know")
			speak("sir")
		
		elif 'firefox' in query:
			speak("firefox")
			speak("is")
			speak("opend")
			webbrowser.open("www.google.com")


# YOU CAN ADD MANY MORE FEATURES...
	
