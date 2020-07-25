from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 

def send_message():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+918264135668' 
                          ) 
 
    print(message.sid)