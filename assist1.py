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
from clint.textui import progress
from bs4 import BeautifulSoup
from urllib.request import urlopen

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good morning sir")


	elif hour>= 12 and hour<18:
		speak("Good afternoon sir")


	else:
		speak("Good evening sir")

	assname =("Achintha")
	speak("I am your assistant mister")
)
	speak(assname)

def usrname():
		speak("What should I call you sir")

		uname = takeCommand()
		speak("Bawantha")
		speak(uname)
		columns = shutil.get_terminal_size().columns
	
		print("#####################".center(columns))
		print("Welcome", uname.center(columns))
		print("mister", uname.center(columns))
		print("Bawantha", uname.center(columns))
		print("#####################".center(columns))
	
		speak("How can i help you sir")

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
		print("Loading your AI personal assistant Achintha")
		speak("Loading your AI personal assistant Achintha")

		wishMe()
		return "none"

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
				speak("Good morning sir")

			elif hour>= 12 and hour<18:
				speak("Good afternoon sir")


			else:
				speak("Good evening sir")


		elif 'stop' in query:
			speak('Okay bye')
)
			exit()

		elif 'youtube' in query:
			speak("Here it's youtube")
)
			webbrowser.open("youtube.com")

		elif 'yahoo' in query:
			speak("Here it's yahoo")
			webbrowser.open("yahoo.com")

		elif 'my page' in query:
			speak("Here you go")

			webbrowser.open("https://weareligeion.wordpress.com/")

		elif 'google' in query:
			speak("Here it's google")
			webbrowser.open("google.com")

		elif 'git hub' in query:
			speak("Here it's github Happy cding sir")
			webbrowser.open("github.com")

		elif 'music' in query or "song" in query:
			speak("Here you go with music")

			music_dir = "Music"
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[1]))

		elif 'time' in query:
			strTime = datetime.datetime.now().strftime("% H:% M:%")
			speak("Sir the time is f"{strTime}")



		elif 'how are you' in query:
			speak("I am Okay sir and how about you")


		elif 'fine' in query or "good" in query:
			speak("That's good to know sir")



		elif "your name" in query or "What is your name" in query:
			speak("My friends call me"'achintha')

			print("My friends call me", 'Achintha')

		elif 'exit' in query:
			speak("Thanks for giving me your time sir")

			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have being created by bawantha")

			
		elif 'joke' in query:
			speak(pyjokes.get_joke())

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then you are a human")



		elif "why you came to world" in query:
			speak("Thanks to bawantha and It's a secret")



		elif 'is love' in query:
			speak("It is the sense that destroyed all other senses")


		elif "who are you" in query:
			speak("I am your assistantcreated by bawantha")


		elif 'reason for you' in query:
			speak("I think it's for fun")



		elif 'news' in query:
			speak("Your news tab is opend one your browser")

			webbrowser.open("https://www.dailymirror.lk")




		elif "don't listen" in query or "stop listening" in query:
			speak("how many times sir ")

			a = int(takeCommand())
			time.sleeps(a)
			print(a)

		elif "where I am" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to locate")

			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")


		elif "new note" in query:
			speak("What should I write sir")
)
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir should I include date and time also ")

			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing notes")

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
			speak("Watch at your browser sir")

			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
            speak("how are you sir")

		elif 'fine' in query or "good" in query:
			speak("That's good to know sir")

			
