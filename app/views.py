from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from app.models import SendSMS
from app.forms import SendSMSForm
from django.urls import reverse_lazy
from app.utils import send_twilio_message
from django.conf import settings 
import datetime
import jinja2
import requests
from bs4 import BeautifulSoup
from .forms import phone
import mysql.connector
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

# Create your models here.

def index(request): 
    return render(request, 'index.html')
def feed(request): 
    URL = 'https://ncdc.gov.ng/news/press'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='example')
    news_elems = results.find_all('div', class_='col-sm-10')
    data = []
    for news_elem in news_elems:
        title_elem = news_elem.find('h3')
        date_elem = news_elem.find('h4')
        # sub_elem = news_elem.find(id='text')
        link_elem = news_elem.find('a', class_='white-text')
        if None in (title_elem, date_elem, link_elem):
            continue
        title = print(title_elem.text.strip())
        date = print(date_elem.text.strip())
        link = print(link_elem.get('href'))
        space = print()
        title = title_elem.text.strip(),
        date =  date_elem.text.strip(),
        link = link_elem.get('href')
        data.append({'title': title, 'date': date, 'link': link, 'space': space})

    return render(request, 'feed.html', context={'data': data})
def upload(request): 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="aspilos_log"
    )

    mycursor = mydb.cursor()
    mobile_number = request.POST.get('mobile_number')
    print(mobile_number),
    sql = "INSERT INTO category2 (PHONE_NUMBER) VALUES (%s)"
    val = mobile_number,
    mycursor.execute(sql, val)
    mydb.commit()
    num = mycursor.rowcount
    output = str(mobile_number) + " " + str(num) + " Record inserted."
    context = {'mobile_number': mobile_number, 'output': output}
    return render(request,"upload.html", context)

def message(request): 
    return render(request, 'messages.html')
def statistics(request): 
    return render(request, 'statistics.html')

# class index(TemplateView):
    # template_name = "index.html"

# class feed(TemplateView):
    # template_name = "feed.html"

# class messages(TemplateView):
    # template_name = "messages.html"

# class upload(TemplateView):
    # template_name = "upload.html"
        

# class statistics(TemplateView):
    # template_name = "statistics.html"

    
class SendSmsCreateView(CreateView):
    model = SendSMS
    form_class = SendSMSForm
    template_name = 'messages.html'
    success_url = reverse_lazy('send_sms')

    def form_valid(self, form):
        number = form.cleaned_data['to_number']
        body = form.cleaned_data['body']
            # call twilio
        sent = send_twilio_message(number, body)
            # save form
        send_sms = form.save(commit=False)
        send_sms.from_number = settings.TWILIO_PHONE_NUMBER
        send_sms.sms_sid = sent.sid
        send_sms.account_sid = sent.account_sid
        send_sms.status = sent.status
        send_sms.sent_at = datetime.datetime.now()
        if sent.price:
            send_sms.price_unit = sent.price_unit
            send_sms.save()

        return super(SendSmsCreateView, self).form_valid(form)