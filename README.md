# cricket-score-whatsappbot

 An application bot to update you with cricket scores in whatsapp with customizable configuration and preferences.
 
 **Sign up and get your keys from cricapi.com and twilio.com. Clone this code and run it to push updates of upcoming amd ongoing matches to your fav whatsapp account.**

## How to run

1. Install python3 on your machine.

2. Open a cricapi account and save your credentials in a file $HOME/.cricapi/config.json in following format.

{
	"url_get_all_matches":"https://cricapi.com/api/matches",
	"getscore":"https://cricapi.com/api/cricketScore",
	"apikey":"paste the key you got after creating your account",
	"unique_id" : null,
	"listed_teams" : ["India"]
}

**Add teams to listed_teams field you are intereted in.**

3. Open a twilio whatsapp account and save your credentials in a file $HOME/.twilio/secret.json in following format.

{
	"account_sid" : "xxxxxxxx",
	"auth_token" : "xxxxxxxx",
	"from_no" : "your twilio whatsapp no. here", 
	"to_no" : "the whatsapp no. you want to recieve updates at"
}

4. Navigate to project directory in terminal and run python main.py. (You might need to send a message 'Join catch-measure' from the whatsapp account you want to recieve updates at to your twilio whatsapp no. you will get after signing up.)

