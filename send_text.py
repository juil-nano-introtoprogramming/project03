#!python
# Lesson 3.3: Use Classes
# Mini-Project: Send Text

from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token  = ""
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Never gonna give you up, never gonna let you down.",
    to="+10000000000",    # Replace with your phone number
    from_="+10000000000") # Replace with your Twilio number
print message.sid
