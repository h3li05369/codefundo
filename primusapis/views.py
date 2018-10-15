from .models import *
from .serializers import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework.exceptions import ParseError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .fcm import send_message

from random import randint
import datetime


class Register(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            print(data)
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
            )
        response = {}
        u = User(username=data.get('mobile'))
        u.set_password(data.get('password'))
        u.save()
        response['U_ID'] = u.id


        p = Client(
            name=data.get('name'),
            mobile=data.get('mobile'),
            email=data.get('email'),
            address=data.get('address'),
            gender=data.get('gender'),
            user=u,
            )
        p.save()
        response['ID'] = p.id
        # t = Token(user=u)
        # t.save()
        # response['Token'] = t.key

        return JsonResponse(
            response, safe=False, content_type='application/json')

class Login(APIView):
    def get(self, request, format=None):
        up = User.objects.get(username='9568249796')
        print(up.password)
        response = {
            "username":up.username,
            "password":up.password
        }

        return JsonResponse(
            response, safe=False, content_type='application/json')


class Location(APIView):
    def post(self,request,format=None):
        try:
            data = request.data
            print(data)
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
                )


        u = User(username=data.get('mobile'))
        print(u)
        l = Location(
            latitude = data.get('log'),
            longitude = data.get('lat'),
            location_of = u,
            )
        print(l)
        l.save()
        now = datetime.datetime.now()

        response = {
            notification_of_location : now
        }

        return JsonResponse(
            response, safe=False, content_type='application/json')




class Marked_as_safe(APIView):
    def post(self,request,format=None):
        try:
            data = request.data
            print(data)
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
                )


        u = User(username = data.get('mobile'))
        print(u)
        client = Client.objects.get(user=u)
        print(client)
        c = client(
            status='S'
            )

        c.save()