from django.conf import settings
import twilio
from twilio.rest import Client
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="aspilos_log")

cursor = db.cursor()
cursor.execute("SELECT PHONE_NUMBER FROM category2")
results = cursor.fetchall()
for i in zip(*results):
    number = list(i)
    number1 = '+2348076548894'
    #print (number)

def send_twilio_message(to_number, body):
    client = Client(
        settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    return client.messages.create(
        body=body,
        to=number,
        from_=settings.TWILIO_PHONE_NUMBER
    )