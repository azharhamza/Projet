import os
from django.core.mail import send_mail
from django.db import models

from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.
class Dht11(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.temp)
    def save(self, *args, **kwargs):
        if self.temp > 40:
            from appiot.views import sendtele
            sendtele()
            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine le,' + str(self.dt),
                'azhar.yagoubi@gmail.com',
                ['azhar.elyagoubi@gmail.com'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)
