import requests
import datetime
import os
import subprocess
import webbrowser
import json
import wikipedia
import win32com.client
from colorama import Fore
import smtplib 
import pyttsx3
import imaplib
import pprint
import email

engine = pyttsx3.init()


    

class Mail():

	def send_gmail():
		username = "jide.bensonele@gmail.com"
		password = "Samuel@07"

		print(Fore.RED + "-"*60)
		print("EMAIL SENDER")
		print(Fore.RED + "-"*60)

		amount_of_emails = int(input("> How many emails would you like to send: "))

		for i in range(amount_of_emails):
			sent_from = username
			to = input("Enter email of recipient: ")
			subject = input("Enter subject of email: ")
			text = input("Enter content of email: ")

			message = """From: %s\nTo: %s\nSubject: %s\n\n%s
   			 """ % (sent_from, ", ".join(to), subject, text)


		try:
			server = smtplib.SMTP("smtp.gmail.com",587)
			server.ehlo()
			server.starttls()
			server.login(username,password)
			server.sendmail(sent_from,to,message)
			server.close()

			return "Successful"

		except Exception as e:
			print("Error: %s\n"% e)



	def read_gmail():
		print("-"*60)
		print("Email Reader")
		engine.say("Email Reader")
		engine.runAndWait()
		print("-"*60)

		host = "imap.gmail.com"
		gmail_username = "jide.bensonele@gmail.com"
		gmail_password = "Samuel@07"

		imap = imaplib.IMAP4_SSL(host)
		imap.login(gmail_username,gmail_password)
		imap.select("Inbox")

		resp_code, mails = imap.search(None, "ALL")
		print("Mail IDs : {}\n".format(mails[0].decode().split()))


		for mail_id in mails[0].decode().split()[-2:]:
			print("================== Start of Mail [{}] ====================".format(mail_id))
			engine.say("Start of Mail")
			resp_code, mail_data = imap.fetch(mail_id, '(RFC822)') ## Fetch mail data.
			message = email.message_from_bytes(mail_data[0][1]) 
			## Construct Message from mail data
			
			print("From       : {}".format(message.get("From")))
			engine.say("From       : {}".format(message.get("From")))
			print("To         : {}".format(message.get("To")))
			engine.say("To         : {}".format(message.get("To")))
			print("Bcc        : {}".format(message.get("Bcc")))
			engine.say("Bcc        : {}".format(message.get("Bcc")))
			print("Date       : {}".format(message.get("Date")))
			engine.say("Date       : {}".format(message.get("Date")))
			print("Subject    : {}".format(message.get("Subject")))
			engine.say("Subject    : {}".format(message.get("Subject")))
			
			print("Body       :")
			engine.say("Body")
			for part in message.walk():
				if part.get_content_type() == "text/plain":
					body_lines = part.as_string().split("\n")

					content_message = "\n".join(body_lines[:len(body_lines)])

					print(content_message)

					engine.say(content_message)

			print("================== End of Mail [{}] ====================\n".format(mail_id))

		engine.say("Closing selecting mailbox")
		engine.runAndWait()
        

def onStart():
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate-50)
    engine.say("Welcome Sam, This is your personal assistant Jarvis, ready to help")
    engine.runAndWait()
    
    engine.say("What would you like to do today")
    option = input("> What would you like to do today: ")
    if option == "send_mail":
        Mail.send_gmail()
        
    elif option == "read_gmail":
        Mail.read_gmail()
        
    else:
        engine.say("Error")
        print("Error")
        
onStart()

