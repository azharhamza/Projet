from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dht11
from .serializer import DHT11serialize

@api_view(['GET'])
def Dlist(request):
    all_data = Dht11.objects.all()
    data = DHT11serialize(all_data, many=True).data
    return Response({'data': data})
class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11serialize