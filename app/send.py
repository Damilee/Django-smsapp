from app.utils import send_twilio_message
sms = send_twilio_message('+2348137404158', 'Hello DMD, How are you doing?,')
print sms.sid


