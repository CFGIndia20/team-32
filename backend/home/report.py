from twilio.rest import Client


account_sid = 'AC52a9306d59834457559c9eb0782ad4d1'
auth_token = '57b8743a9aeee1fbe3b0b2325a8db214'
client = Client(account_sid, auth_token)

def send_message(body,number):

    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=body,
                              to=number
                          )

    print(message.sid)

