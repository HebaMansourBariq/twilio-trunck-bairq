from twilio.rest import Client
from dotenv import load_dotenv
import requests
import os

load_dotenv('.env')

account_sid = os.getenv('TWILIO-SID')
auth_token  = os.getenv('TWILIO-TOKEN')

client = Client(account_sid, auth_token)

def get_call_recording(caller_sid:str):
    recording_uri = client.calls.list(from_=caller_sid)[-1].uri.replace(".json", ".mp3")
    media_url = f'https://api.twilio.com{recording_uri.replace(".json", ".mp3")}'
    response = requests.get(media_url, auth=(account_sid, auth_token))
    if response.status_code=='200':
        return {'issuccessful': False, 'content': response.content}
    else:
        return {'issuccessful': False}


get_call_recording('unknown')




