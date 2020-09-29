
import os
import speech_recognition as sr
import pyautogui
import webbrowser
import socket as s
from speedtest import Speedtest
import requests
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
import pyjokes
import pyttsx3
import datetime
import smtplib
import win10toast
from pytube import YouTube
import pyshorteners
import wikipedia
import time
import socket

toaster=win10toast.ToastNotifier()
toaster.show_toast('Python','This is currently working',duration=5)

# initialisation
engine=pyttsx3.init()

# testing

def speak(audio) :
	engine.say(audio)
	engine.runAndWait()

def takeCommand() :
# when you want to take text as a input
	query=input("Enter------>")
	return query

# when you want to take human voice as input
"""	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold=1
		audio=r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_goole()
		print(query)
	except Exception as e:
		print(e)
		speak("Say that again please")
		return "None"
	return query
"""
print("Enter your name--->")
speak("hii myself alexa whats your name?")
name=takeCommand()
print("Synonym in your servicing",name)
speak("Synonym in your servicing  "+name)

while True:
	print("\nDo you want to continue--->")	
	speak("do you want to continue")
	msg=takeCommand()
	print(msg)
	if(msg!="no"):
		speak("how can i help you"+name)
		str=takeCommand()
		x=(str.lower())
		word="alexa" 
		first_word=x.split()[0]
		if word==first_word:  #wake word ALEXA 

			if (("what" in x) or ("know" in x) or ("tell" in x)) and (("meaning" in x) or ("mean" in x)):
				words=str.split()
				word=words[-1]
				dictionary=PyDictionary()
				print(dictionary.meaning(word))
				speak(f'{dictionary.meaning(word)}')
			
			elif (("what" in x) or ("know" in x) or ("tell" in x)) and (("synonyms" in x) or ("synonym" in x)):
				words=str.split()
				word=words[-1]
				dictionary=PyDictionary()
				print(dictionary.synonym(word))
				speak(f'{dictionary.synonym(word)}')
			
			elif (("what" in x) or ("know" in x) or ("tell" in x)) and (("antonyms" in x) or ("antonym" in x) or ("opposite" in x)):
				words=str.split()
				word=words[-1]
				dictionary=PyDictionary()
				print(dictionary.antonym(word))
				speak(f'{dictionary.antonym(word)}')	
		
			elif (("what" in x) or ("know" in x) or ("tell" in x)) and (("temperature" in x) or ("weather" in x)):
				print("Tell me the place of which you want to know the temperature--->")
				speak("which place you would like to know the weather")
				search=takeCommand()
				url=f"https://www.google.com/search?&q=weather+of+{search}"
				r=requests.get(url)
				s=BeautifulSoup(r.text, "html.parser")
				update=s.find("div", class_="BNeawe").text
				print(update)
				speak("Right now the temperature of+search+ is +update")

			elif (("what" in x) or ("know" in x) or ("tell" in x) or ("show" in x)) and ("time" in  x):
				Time = datetime.datetime.now().strftime("%I:%M:%S")
				print("Time:",Time)
				speak("The current time is")
				speak(Time)

			elif (("what" in x) or ("know" in x) or ("tell" in x) or ("show" in x)) and ("date" in  x):
				year = int(datetime.datetime.now().year)
				month = int(datetime.datetime.now().month)
				day = int(datetime.datetime.now().day) 
				print("Date:",day,"/",month,"/",year)
				speak("The current date is")
				speak(day)
				speak(month)
				speak(year)
			
			elif (("what" in x) or ("know" in x) or ("tell" in x) or ("show" in x)) and (("ip" in x) and ("my" in x)):
				hostname=socket.gethostname()
				ip_address=socket.gethostbyname(hostname)
				print("Your desktop IP address is:",ip_address)
				speak("your desktop ip address is"+ip_address)

			elif (("what" in x) or ("know" in x) or ("tell" in x) or ("show" in x)) and ("ip" in x):
				speak(name+"enter the name of website whose ip address you want to know")
				print("Website name whose ip address you want to know:")
				host=takeCommand()			
				print(f'IP of {host} is {s.gethostbyname(host)}')
				speak("IP of "+host+"is"+s.gethostbyname(host))

			elif (("what" in x) or ("know" in x) or ("tell" in x) or ("show" in x)) and (("connection" in x)and("speed" in x)):
				st=Speedtest()
				dow=st.download()
				upl=st.upload()
				print("Your Connection Download speed is:",dow)
				speak(f'Your Connection Download speed is{dow}')
				print("Your Connections Upload speed is:",upl)
				speak(f'Your Connection Upload speed is{upl}')

			elif (("short" in x) or ("shorten" in x)) and ("url" in x):
				speak("enter the url you want to shorten")
				url=input("Enter the url:")
				try:
					s=pyshorteners.Shortener()
					print("Your shortened url is ->",s.tinyurl.short(url))
					speak(f'Your shortened url is ->{s.tinyurl.short(url)}') 
				except Exception as e:
					print(e)
					speak("there's no such url")

			elif (("download" in x) and ("video" in x)) or ("youtube" in x):
				speak("enter the url of the video you want to download")
				url=input("Enter the url:")	
				video=YouTube(url)
				print(video.title)
				speak(f'downloading {video.title}')
				youtube=video.streams.first()
				youtube.download(r'C:\Users\muskan\Desktop')
				print("......Video Downloaded...Check Your Desktop......")

			elif ("remember" in x) and (("asked" in x) or ("tell" in x) or ("told" in x)) and ("what" in x):
				remember=open('msg.txt','r')
				print("You asked me to remember",remember.read())
				speak("This is what you asked me to remember")

			elif "remember" in x:
				speak("what should i remember")	
				msg=takeCommand()
				print("You asked me to remember",msg)
				speak("you asked me to remember"+msg)
				remember=open('msg.txt','w')
				remember.write(msg)
				remember.close()

			elif (("create" in x) or ("make" in x)) and (("folder" in x) or ("directory" in x)):
				print("Where you want to create the folder")
				speak("Where you want to create the folder")
				place_of_folder=takeCommand()
				print("Give a name to this folder")
				speak("Give a name to this folder")
				name_of_folder=takeCommand()
				path=("C:\\Users\\muskan\\"+place_of_folder+"\\")
				print("Ok, Creating the folder named "+name_of_folder+" in your " +place_of_folder)
				speak("Ok     Creating the folder named "+name_of_folder+" in your " +place_of_folder)
				os.system("mkdir "+path+name_of_folder)

			elif (("create" in x) or ("make" in x)) and ("file" in x):
				print("Where you want to create a file")
				speak("Where you want to create a file")
				place_of_file=takeCommand()
				print("Give a name to this file with it's extension/type")
				speak("Give a name to this file with it's extension or type")
				name_of_file=takeCommand()
				path=("C:\\Users\\muskan\\"+place_of_file+"\\")
				print("Ok, Creating the file named "+name_of_file+" in your " +place_of_file)
				speak("Ok     Creating the file named "+name_of_file+" in your " +place_of_file)
				os.system("type nul >"+path+name_of_file)

			elif (("delete" in x) or ("remove" in x)) and (("folder" in x) or ("directory" in x)):
				print("From where you want to remove the folder")
				speak("From where you want to remove folder")
				place_folder=takeCommand()
				print("Give the name of the folder")
				speak("Give the name of the folder")
				name_folder=takeCommand()
				path=("C:\\Users\\muskan\\"+place_folder+"\\")
				print("Ok, Removing the folder named "+name_folder+" from your " +place_folder)
				speak("Ok     Removing the folder named "+name_folder+" from your " +place_folder)
				os.system("rmdir "+path+name_folder)

			elif (("delete" in x) or ("remove" in x)) and ("file" in x):
				print("From where you want to remove the file")
				speak("From where you want to remove the file")
				place_file=takeCommand()
				print("Give the name of the file")
				speak("Give the name of the file")
				name_file=takeCommand()
				path=("C:\\Users\\muskan\\"+place_file+"\\")
				print("Ok, Removing the file named "+name_file+" from your " +place_file)
				speak("Ok     Removing the file named "+name_file+" from your " +place_file)
				os.system("del "+path+name_file)			

			elif "wikipedia" in x:
				str=input("Enter the name of the topic you want to read wikipedia:")
				speak("Enter the name of the topic you want to read wikipedia....")
				print()
				try:
					print(wikipedia.summary(str, sentences=5))
					speak(f'{wikipedia.summary(str, sentences=2)} and so on')
				except Exception as e:
					print(e)
					speak("There's no such topic on wikipedia")



			elif("run" in x) or ("start" in x) or ("launch" in x) or ("open" in x) or ("execute" in x) or ("play" in x) or ("tell" in x) or ("give" in x) or ("show" in x) or ("set" in x) or ("inside" in x) or ("restart" in x) or ("take" in x) or ("see" in x) or ("hi" in x) or ("hey" in x) or ("hello" in x):   #launch words   

				if ("notepad" in x) or ("editor" in x):  #default text editor
					print("Running notepad.....")
					speak("running notepad")
					os.system("notepad")

				elif ("bluetooth" in x) :
					print("Enable it if not enabled")
					speak("enable it if not enabled")
					time.sleep(2)
					os.system("start ms-settings:bluetooth")
					time.sleep(4.7)
					os.system(" start fsquirt")

				elif ("browser" in x) or ("chrome" in x):  #default browser
					print("Launching chrome.....")
					speak("launching chrome")
					os.system("chrome")

				elif "firefox" in x:
					print("Launching firefox.....")
					speak("launching firefox")
					os.system("firefox")

				elif ("google" in x)and ("launch" in x):
					print("Opening google search engine website in chrome.....")
					speak("opening google search engine website in chrome")
					os.system("chrome google.com")

				elif "yahoo" in x:
					print("Opening yahoo search engine website in chrome.....")
					speak("opening yahoo search engine website in chrome")
					os.system("chrome yahoo.com")

				elif "bing" in x:
					print("Opening bing search engine website in chrome.....")
					speak("opening bing search engine website in chrome")
					os.system("chrome bing.com")

				elif "vlc" in x:  
					print("Running vlc.....")		
					speak("running vlc")  
					os.system("vlc")

				elif "shareit" in  x:
					print("Here you go.....")
					speak("here you go")
					os.system("shareit")

				elif ("virtualbox" in  x) or ("virtualbox" in x):
					print("Here you go for virtulization.....")
					speak("here you go for virtulization")
					os.system("virtualbox")

				elif ("pdf reader" in  x) or ("pdf viewer" in x):
					print("Start reading.....")
					speak("start reading")
					os.system("pdfreader")

				elif "calculator" in  x:
					print("Launching calculator.....")
					speak("launching calculator")
					os.system("calc")

				elif "drawboard" in  x:
					print("Here you go.....")
					speak("here you go")
					os.system("start drawboardpdf:")

				elif "paint" in  x:
					print("Start painting.....")
					speak("start painting")
					os.system("start ms-paint:")

				elif "onenote" in  x:
					print("Here you go.....")
					speak("here you go")
					os.system("start onenote")

				elif "outlook" in  x:
					print("Here you go.....")
					speak("here you go")
					os.system("start outlook")

				elif "sublime" in  x:
					print("Running sublime text editor.....")
					speak("running sublime text editor")
					os.system("subl.exe")

				elif ("powerpoint" in  x) or ("ms-powerpoint" in x):
					print("Opening powerpoint.....")
					speak("opening powerpoint")
					os.system("start powerpnt")

				elif ("word" in  x) or ("ms-word" in x):
					print("Launching ms-word.....")
					speak("launching ms word")
					os.system("start winword")

				elif ("ms-excel" in  x) or ("excel" in x):
					print("Launching ms-excel.....")
					speak("launching ms excel")
					os.system("start excel")

				elif ("ms-access" in  x) or ("access" in x):
					print("Launching ms-access.....")
					speak("launching ms access")
					os.system("start access")

				elif ("avast" in  x) or ("anti-virus" in x) or ("anti virus" in x):
					print("Here you go.....")
					speak("here you go")
					os.system("avastui")

				elif "obs" in x:
					print("Executing obs.....")
					speak("executing OBS")
					os.system("obs64")

				elif ("music" in  x) or ("gaana" in x):
					print(name,"do you want to listen music from your default groove music player")
					speak(name+"do you want to listen music from your default groove music player")
					input=takeCommand()
					if (input=="yes"):
						print("Launching groove music application")
						speak("launcing groove music application")
						os.system("start mswindowsmusic:")
					else:
						print("Start listen music in youtube")
						speak("start listening music in youtube ")
						os.system("chrome https://youtube.com")

				elif ("camera" in  x) or ("webcam" in x) or ("camcorder" in x):
					print("Opening your camera....")
					speak("opening your camera")
					os.system("start microsoft.windows.camera:")

				elif ("3dbuilder" in  x) or ("builder3d" in x) or ("3d builder" in x):
					print("Here you go.....")
					speak("here you go")
					os.system("start com.microsoft.builder3d:")

				elif ("messaging" in  x) or ("chatbox" in x) or ("chat" in x) or ("chatting" in x) or ("whatsapp" in  x):
					print("Should i launch your whatsapp application")
					cmd=takeCommand()
					if (cmd=="no"):
						print("Opening your ms-chat now you can start messaging.....")
						speak("start messaging")
						os.system("start ms-chat:")
					else:
						print("Start chatting.....")	
						speak("start chatting in whatsapp")
						os.system("whatsapp")

				elif ("store" in  x) or ("window-store" in x):
					print("Opening window store.....")
					speak("opening window store")
					os.system("start ms-windows-store:")

				elif ("network" in  x) or ("networks" in x) or ("connections" in x) or ("connection" in x):
					print("Your available networks are.....")
					speak("your available networks are")
					os.system("start ms-availablenetworks:")

				elif "calendar" in  x:
					print("Here you go.....")
					speak("here you go")
					os.system("start outlookcal:")

				elif ("candy crush" in  x) or ("soda saga" in x):
					print("Start playing.....")
					speak("start playing ")
					os.system("start candycrushsodasaga:")

				elif "projection" in x:
					print("Here you go.....")
					speak("here you go")
					os.system("start ms-projection:")

				elif "cortana" in  x:
					print("Start interacting with cortana.....")
					speak("start interacting with cortana ")
					os.system("start ms-cortana:")

				elif "feedback" in  x:
					print("Launching feedback-hub.....")
					speak("launching feedback hub")
					os.system("start feedback-hub:")

				elif (("mail" in  x) or ("email" in x)) and ("outlook" in x):
					print("Here you go.....")
					speak("here you go")
					os.system("start outlookmail:")

				elif ("maps" in  x) or ("map" in x) or ("roots" in x):
					print("Here you go.....")
					speak("here you go")
					os.system("start ms-drive-to:")

				elif "edge" in  x:
					print("Launching edge.....")
					speak("launching edge")
					os.system("start microsoft-edge:")

				elif "news" in  x:
					print("Latest news are here for you.....")
					speak("latest news are here for you")
					os.system("start bingnews:")

				elif "solitaire" in  x:	
					print("Start playing.....")
					speak("start playing")
					os.system("start xboxliveapp-1297287741:")

				elif ("media" in x) or ("player" in x):
					print("Launching windows media player.....")
					speak("launching windows media player")
					os.system("wmplayer")		

				elif "whiteboard" in x:
					print("Here you go.....")
					speak("here you go")
					os.system("start ms-whiteboard-cmd:")

				elif "people" in  x:
					print("Here you go.....")
					speak("here you go")
					os.system("start ms-people:")

				elif ("photos" in  x) or ("picture" in x) or ("gallary" in x) or ("album" in x):
					print("Explore your gallary.....")
					speak("explore your gallary")
					os.system("start ms-photos:")

				elif "tips" in  x:
					print("Here you go.....")
					speak("this application will give you some tips regarding your windows 10")
					os.system("start ms-get-started:")

				elif "twitter" in  x:
					print("Start twitting.....")
					speak("start twitting")
					os.system("start twitter:")

				elif ("3dviewer" in  x) or ("3dpreview" in x) or ("3d viewer" in x) or ("3d preview" in x):
					print("Here you go.....")
					speak("here you go")
					os.system("start com.microsoft.3dviewer:")

				elif ("record" in  x) or ("call recording" in x) or ("recording" in x):
					print("Start recording.....")
					speak("start recording")
					os.system("start ms-callrecording:")

				elif "recycle bin" in x:
					print("Opening recycle bin.....")
					speak("Opening recycle bin")
					os.system("start shell:RecycleBinFolder")

				elif ("this pc" in  x) or ("my pc" in x) or ("my computer" in x):
					print("Opening this pc.....")
					speak("Opening this pc")
					os.system("start explorer shell:mycomputerfolder")

				elif ("jupyter notebook" in  x) or ("jupyter" in x):
					print("Opening jupyter notebook.....")
					speak("Opening jupyter notebook")
					os.system("jupyter notebook")

				elif "youtube" in x:
					print("Starting Youtube")
					speak("Starting Youtube")
					print("What do you want to search")
					speak("what do you want to search")
					search=takeCommand()
					print("Searching")
					speak("Searching")
					webbrowser.open("https://www.youtube.com/results?search_query=" + search)

				
				elif ("defender" in  x) or ("windowsdefender" in x):
					print("Start securing your windows.....")
					speak("start securing your windows")
					os.system("start windowsdefender:")
			
				elif ("clock" in  x) or ("alarm" in x):
					print("Here you go.....")
					speak("here you go")
					os.system("start ms-clock:")

				elif "screenshot" in x:
					img=pyautogui.screenshot()
					img.save("C:\\Users\muskan\Desktop\screenshot\screen.png")
					print("Screenshot taken")
					speak("Screenshot taken")

				elif (("laptop" in x) or ("desktop" in x)) and ("restart" in x):
					print("Are you confirm to restart your desktop")
					conf=takeCommand()
					if (conf=="yes"):
						print("Restarting your desktop")
						speak("restarting your desktop")
						os.system("shutdown /r /t 1")
					else:
						print("Ok")
						speak("ok")
			
				elif ("systeminfo" in x) or ("about" in x) or ("system" in x) or ("system information" in x):
					print("Here's your desktop information.....")
					speak("your desktop information is here")
					os.system('cmd /k "systeminfo"')

				elif "xbox" in  x:
					print("Launching xbox.....")
					speak("launching xbox")
					os.system("start xbox:")

				elif "help" in  x:
					print("Opening your help center.....")
					speak("opening your help center")
					os.system("start ms-contact-support:")

				elif ("settings" in  x) or ("control panel" in x):
					print("Opening your control panel.....")
					speak("start settings")
					os.system("start ms-settings:")
		
				else:
					print("Please elaborate your statement...")
					speak("please elaborate your statement...")
			
			
			elif ("send" in x) and ("email" in x):
				speak("enter you email id")
				gmail_add=input("your email id:")
				speak("enter yor password")
				gmail_pass=input("your password:")
				speak("enter email address you want to send email to")
				mail_to=input("recepeint email id:")
				speak("tell me your message")
				msg=takeCommand()
				try:
					s=smtplib.SMTP('smtp.gmail.com', 587)
					s.starttls()
					s.login(gmail_add, gmail_pass)
					print("Login success")
					speak("Successfully login")
					s.sendmail(gmail_add, mail_to,msg)
					print("Email has been successfully sent to", mail_to)
					speak("Successfully sent")
					s.quit()
				except Exception as e:
					print(e) 
					speak("Unable to send the email Authentication problem")
	
			elif ("how" in x) or ("which" in x) or ("when" in x) or ("do" in x) or ("who" in x) or ("whom" in x) or ("whose" in x) or ("why" in x) or ("whether" in x) or ("where" in x) or ("list" in x):
				line=x
				s2=line.split(None, 1)[1]
				print("Please wait while i am searching.....")
				speak("Please wait while i am searching")
				url=f"https://www.google.com/search?&q={s2}"
				r=requests.get(url)
				s=BeautifulSoup(r.text, "html.parser")
				update=s.find("div", class_="BNeawe").text
				print(update)
				speak(update)
				print("Want to know more.....")
				speak("Want to know more.....")
				more=takeCommand()
				if (more!="no"):
					print("Opening your search in your default browser.....")
					speak("Opening your search in your default browser")
					webbrowser.open(url)
				else:
					print("Ok")
					speak("Ok fine enough")	
			
			elif("how are you" in x):
				print("I am fine. What about you?")
				speak("I am fine. What about you"+name)
				i=takeCommand()
				if("i" in i) and (("good" in i) or ("great" in i) or ("fine" in x) or ("amazing" in i) or ("fantastic" in i) or ("superb" in i)):
					print("Good to here that")
					speak("good to here that")
				elif(("not fine in i") or ("bad" in i)):
					print("Wanna listen a joke")
					speak("Wanna listen a joke??")
					j=takeCommand()
					if ("yes" in j) or ("ya" in j) or ("sure" in j):
						print("write a joke")
					else:
						print("Ok")
						speak("Ok")

			elif ("you in x") and ("are" in x) and (("great in x") or ("awesome" in p)):
				print("Thank You. All credits goes to my creator Komal Suthar")
				speak("Thank You. All credits goes to my creator Komal Suthar")

			elif (("dont" in x) or ("do not" in x) or ("don't" in x)) and (("execute" in x) or ("open" in x) or ("start" in x) or ("launch" in x) or ("run" in x)):
				print("Ok I will not launch it.")
				speak("Ok I will not launch it.") 

			elif ("exit" in  x) or ("quit" in x) or ("close" in x) or ("stop" in x) or ("turn off" in x) or ("shut down" in x):  #this will let u go out of alexa 
				break

			else:
				print("Please elaborate your statement...")
				speak("please elaborate your statement...")

		else:
			speak("Wake me up by telling the first word of your statement---alexa---")
			print("Wake me up by telling the first word of your statement---alexa---")
			print()

	else:
		hour = datetime.datetime.now().hour 
		if hour>=6 and hour<=12 :
			print("Thankyou for using me. Have a good morning")
			speak("Thankyou for using me. Have a good morning")
		elif hour>=12 and hour<=18 :
			print("Thankyou for using me. Have a good afternoon")
			speak("Thankyou for using me. Have a good afternoon")
		elif hour>=18 and hour<=24 :
			print("Thankyou for using me. Have a good evening")
			speak("Thankyou for using me. Have a good evening")
		else:
			print("Thankyou for using me. Have a good night")
			speak("Thankyou for using me. Have a good night")
		break
