from django import forms
from .models import SendSMS
from django.conf import settings
from django import forms
from .models import addPhone


class SendSMSForm(forms.ModelForm):
    class Meta:
        model = SendSMS
        fields = ( 'body',)

class phone(forms.ModelForm):
    class Meta:
        model= addPhone
        fields= ["number"]
        


