# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC98b32d425865b0ce8e5313800a546dfd'
auth_token = 'be20f58b42bcf9a80581160bb90bcc46'

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=("Hey there, need help this is my live location. Follow the link- {}".format("url")),
                     from_='+16232330864',
                     to='+918283920044',
                     media_url=['https://demo.twilio.com/owl.png']
                 )

print(message.sid)
