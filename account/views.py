from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token

# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Profile
from account.serializers import RegisterSerializer


class SenderRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Profile.objects.create(user=user, is_sender=True)


class BuyerRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Profile.objects.create(user=user, is_sender=False)


class LoginView(APIView):
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK, )
            else:
                return Response({'detail': 'User account is not active'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    # def post(self, request):
    #     user = authenticate(username=request.data['username'], password=request.data['password'])
    #     if user:
    #         token, created = Token.objects.get_or_create(user=user)
    #         return Response({'token': token.key})
    #     else:
    #         return Response({'error': 'Invalid credentials'}, status=401)