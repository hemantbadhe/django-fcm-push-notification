from django.shortcuts import render
from fcm_django.models import FCMDevice
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def send_notification(request):
    FCMDevice.objects.all().send_message(title="This is title", body="This is a notification body")
    return Response({'message': 'success'})
