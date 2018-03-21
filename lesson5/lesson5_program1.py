
"""
    udacity fsnd
    lesson 5 practice problem
    sending sms to mobile via twilio  
"""




from twilio.rest import Client

#Account Authorization and Auth Token from twilio.com/user/account
account_sid = "*******************************"
auth_token = "********************************"
client = Client(account_sid, auth_token)

message = client.messages.create(body="Test messeage? Twilio client App",
                                     to="+918*********",   # Receiver Number
                                     from_="+12*******") # Twilio Number
print(message.sid) 
