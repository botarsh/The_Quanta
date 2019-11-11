 from twilio.rest import Client

  account_sid = 'AC98b32d425865b0ce8e5313800a546dfd'
auth_token = 'be20f58b42bcf9a80581160bb90bcc46'

client = Client(account_sid, auth_token)
     num=['+917051788482','+919919977826']

  for i in range(0,len(num)):
        message = client.messages.create(num[i], from_="+16232330864",
                             body="Hello ")