import os

from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()

# TWILIO_API_KEY_SID = os.environ.get('TWILIO_API_KEY_SID')
TWILIO_API_KEY_SID = 'TWILIO_API_KEY_SID'
# TWILIO_API_KEY_SECRET = os.environ.get('TWILIO_API_KEY_SECRET')
TWILIO_API_KEY_SECRET = 'TWILIO_API_KEY_SECRET'
FROM = os.environ.get('FROM')


client = Client(TWILIO_API_KEY_SID, TWILIO_API_KEY_SECRET)





def sendMessage(senderId, message):

    whats = 'whatsapp:+'+senderId

    print(message+'             '+FROM+'              '+whats)


    res = client.messages.create(
        from_=FROM,
        body=message,
        to=whats
    )
    print(res.sid)
    return res
