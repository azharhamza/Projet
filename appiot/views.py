import csv
import io
import reportlab
from multiprocessing.connection import Client
import telepot
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Dht11
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
from django.conf import settings


def home(request):
    return HttpResponse('bonjour tout le monde')


@login_required(login_url='acces')
def dht11(request):
    tab = Dht11.objects.order_by('id')
    tab1 = Dht11.objects.values()
    list2 = (list(tab1))[-1]
    temp1 = list2['temp']
    hum1 = list2['hum']
    dt1 = list2['dt']
    list1=(list(tab1))[-7:]

    if temp1 > 40 :
        sendtele()
        send_mail(
            'température dépasse la normale,' + str(temp1),
            'anomalie dans la machine le,' + str(dt1),
            'azhar.yagoubi@gmail.com',
            ['azhar.elyagoubi@gmail.com'],
            fail_silently=False,
        )

    s = {'tab': tab,"list1":list1,"list2":list2,"temp1":temp1,"hum1":hum1,"dt1":dt1}
    return render(request, 'dashboard.html', s)

@login_required(login_url='acces')

def sendtele():
    token = '2112940431:AAFvEGA8V0ZXvn0Jao1GsFW5UqMIdZe-qlk'
    rece_id = 2115040562
    bot = telepot.Bot(token)
    bot.sendMessage(rece_id, 'la température depasse la normale')
    print(bot.sendMessage(rece_id, 'OK.'))


def sendtele():
    token = '5441034440:AAEzwSx6Y616_dk1WTTu0waE94JazJJZkD4'
    rece_id = 5447950442
    bot = telepot.Bot(token)
    bot.sendMessage(rece_id, 'la température depasse la normale')
    print(bot.sendMessage(rece_id, 'OK.'))

@login_required(login_url='access')
def exp_csv(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Temperatue', 'Humidite', 'Date_Heure'])

    for index in Dht11.objects.all().values_list('temp', 'hum', 'dt'):
        writer.writerow(index)

    response['Content-Disposition'] = 'attachement; filename = "dht11.csv"'
    return response

def pdf(request):
    Data = Dht11.objects.all()
    buf = io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    txt = c.beginText()
    txt.setTextOrigin(inch, inch)
    txt.setFont("Helvetica", 14)
    lines = ['N' 'Temperature' 'Date']
    for line in lines:
        txt.textLine(line)
    c.drawText(txt)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='appiot.pdf')
