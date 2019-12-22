import json
import copy
import requests
from datetime import datetime
import time

class CricAPI:	
	
	def __init__(self, file):

		with open(file) as config_file:
		    data = json.load(config_file)

		self.url_get_all_matches = data["url_get_all_matches"]
		self.getscore = data["getscore"]
		self.apikey = data["apikey"]
		self.unique_id = data["unique_id"]
		self.listed_teams = data["listed_teams"]
		self.iter_data=""
		self.score=[]
		self.match_time=""
	
	def get_unique_id_and_score(self):
				
		uri_params={"apikey":self.apikey}
		resp=requests.get(self.url_get_all_matches,params=uri_params)
		resp_dict=resp.json()

		for match in resp_dict["matches"]:
			if (match["team-1"] in self.listed_teams or match["team-2"] in self.listed_teams):
				todays_date = datetime.today().strftime("%Y-%m-%d")
				self.UTC_match_time = datetime.strptime(match["dateTimeGMT"].replace('T', ' ').replace('Z', ''), '%Y-%m-%d %H:%M:%S.%f')
				offset = datetime.fromtimestamp(time.time()) - datetime.utcfromtimestamp(time.time())
				self.match_time = self.UTC_match_time + offset
				self.unique_id=match["unique_id"]
				self.get_score()
				self.score.append(self.iter_data)
		

	def get_score(self):
		
		uri_params={"apikey":self.apikey,"unique_id":self.unique_id}
		resp=requests.get(self.getscore,params=uri_params)
		data_json=resp.json()
		print(data_json)	
		self.iter_data=""

		if not(data_json["matchStarted"]):
			self.iter_data = data_json["team-1"]\
			+ " vs " + data_json["team-2"] + "\nUPCOMING on\n" + str(self.match_time).replace(' ', ' at ').split('.')[0]
			return
		
		try:
			self.iter_data ="Current score: \n\t" + data_json["stat"]
		except KeyError as e:
			print("keyerror: ", e)

		try:
			self.iter_data = self.iter_data + "\n\t" + data_json["score"]
		except KeyError as e:
			print("keyerror: ", e)

		self.iter_data = self.iter_data + "\n\t" + "started on " + str(self.match_time).replace(' ', ' at ').split('.')[0]