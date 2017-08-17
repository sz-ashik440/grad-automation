from twilio.rest import Client
from constants import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, OWN_PHONE_NO, TWILIO_PHONE_NO


def send_message(message_body):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.api.account.messages.create(
        to=OWN_PHONE_NO,
        from_=TWILIO_PHONE_NO,
        body=message_body
        )
    print('Message has been sent')

def main():
    send_message('hello to twilio')

if __name__=='__main__':
    main()