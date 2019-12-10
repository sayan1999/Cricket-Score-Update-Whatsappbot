from twilio.rest import Client
import json

class Twilio_Client:

	def __init__(self, file):

		with open(file) as secret_file:
		    credentials = json.load(secret_file)
		
		self.account_sid = credentials["account_sid"]
		self.auth_token = credentials["auth_token"]
		self.from_no = credentials["from_no"]
		self.to_no = credentials["to_no"]
		self.client = Client(self.account_sid, self.auth_token)
	
	def send_message(self, message):
		return self.client.messages.create(body=message, from_=self.from_no, to=self.to_no)		