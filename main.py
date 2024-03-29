import json
import cricapi.cricapi as cricapi
from pathlib import Path
import twilio_help.twilio_help as twilio_help

home = str(Path.home())

s=cricapi.CricAPI(home + '/.cricapi/config.json')
s.get_unique_id_and_score()

message = ""

if s.score == []:
	message="No India match today."
else:
	for s in s.score:
		message += s + "\n\n"


cli = twilio_help.Twilio_Client(home + '/.twilio/secret.json')
cli.send_message(message)


